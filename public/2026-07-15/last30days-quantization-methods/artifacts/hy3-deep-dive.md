# 🔬 Deep Dive: dan098/hy3 — NVMe-Streamed MoE for Consumer Hardware

**GitHub:** https://github.com/dan098/hy3  
**Freshness:** 1 commit, created yesterday (July 14, 2026)  
**License:** Apache 2.0  
**Language:** Pure C (single file) + optional CUDA kernel  
**Stars:** 0 (brand new, just dropped)

---

## What It Is

hy3 is a **pure-C inference engine** that runs **Tencent Hy3 (295B-parameter MoE, ~21B active/token)** on a **consumer machine** — 16 GB VRAM + 30 GB RAM + NVMe. The GPU is optional; the entire engine runs on CPU.

```bash
$ SNAP=/nvme/hy3_i4g ./hy3 --serve
  == Hy3 C engine (avx2) == STREAM efmt=int4 cap=37 dense=int8 | load 17s RSS 9.0GB
  › The capital of France is
  ◆ Paris. The capital of Germany is Berlin.
```

---

## The Core Idea: Memory Hierarchy Split

A 295B MoE only activates ~21B parameters per token, and the routed experts change each token. hy3 exploits this with a **3-tier memory hierarchy**:

| Tier | What | Where | Size |
|------|------|-------|------|
| **Resident** | Dense part (attention QKV/O, shared expert, router, embeddings, LM head) | **RAM**, int8 per-row | ~9 GB |
| **Streamed** | Routed experts (80 layers × 192 experts) | **NVMe disk**, int4 group-128 | ~155 GB on disk |
| **Cached** | Recently used experts | **LRU cache in RAM** + OS page cache | Auto-sized from `MemAvailable` |

The engine never OOMs — the cache size is automatically set from free RAM.

---

## Architecture Detail

### Model Architecture (Hy3 / HYV3ForCausalLM)
- **GQA attention**: 64 query heads, 8 KV heads, head_dim=128
- **Per-head QK-norm applied before RoPE** (NORM_THEN_ROPE — rare, faithful to Hy3)
- **DeepSeek-V3-style sigmoid router** with expert-bias correction, normalized top-8 routing, routed-scaling factor
- **1 shared expert** per MoE layer
- **First dense layer** before the MoE stack
- **80 layers × 192 experts** = 15,360 expert matrices

### Quantization Scheme
- **Dense part**: int8 per-row (or bf16 passthrough with `HY3_DENSE=bf16`)
- **Routed experts**: int4 group-128 (packed 2 nibbles/byte) — the default
- **Alternative**: int8 per-row experts (`--ebits 8`) — 2× higher fidelity, 2× slower, ~290 GB disk
- **MTP layer** experts forced to int8

### AVX2 Kernels (in `c/hy3.c`)
- `mm_f32` — standard float32 matmul with FMA
- `mm_i8` — int8 per-row dequant + FMA
- `mm_i4` — int4 packed nibble unpack + FMA (the workhorse)
- `mm_bf16` — bf16 passthrough
- `dot_i4g` — int4 group-128 dot product with per-group scale

---

## Measured Performance

| Metric | Value |
|--------|-------|
| Model on disk (int4 group-128) | ~162 GB |
| Resident RAM (dense int8) | ~9 GB |
| Load time | ~17 s |
| Decode speed | ~0.4–0.6 tok/s (warm) |
| NVMe (parallel 19 MB reads) | ~5.9 GB/s O_DIRECT |
| Test hardware | Threadripper 7960X (24c), 30 GB RAM, Samsung 990 PRO NVMe |

**Key insight:** Decode is I/O-bound — faster NVMe + more RAM for expert cache directly increase speed.

---

## How It Works (Token-by-Token)

For each token:
1. **Embed** → RMSNorm
2. **For each layer:**
   - RMSNorm → GQA attention (per-head QK-norm, RoPE) → residual add
   - RMSNorm → **MoE**
     - Sigmoid router → expert-bias → top-8 selection
     - Read uncached experts from NVMe **in parallel** (high queue depth)
     - AVX2 int4 kernel: `down(silu(gate·x)·(up·x))` for each expert
     - Add shared expert → sum
   - LRU cache learns hot experts over time
3. **Final:** RMSNorm → lm_head → logits

---

## Repo Layout

```
c/
├── hy3.c                 single-file engine (forward, streaming, cache, kernels, serve) — 1500+ lines
├── st.h                  safetensors reader
├── json.h                JSON parser
├── compat.h              POSIX/Windows shims
├── convert_hy3.py        FP8/BF16 → int4/int8 streaming container (resumable, shard-by-shard)
├── openai_hy3_server.py  OpenAI-compatible HTTP gateway (stdlib only, no deps)
├── hy3_chat.py           one-shot / REPL chat client
├── make_hy3_oracle.py    tiny-random HYV3 fixture for token-exact validation
├── hy3_cuda.cu           optional CUDA int4 expert kernel + self-test
└── Makefile
```

---

## CUDA Kernel (Optional GPU Tier)

`hy3_cuda.cu` provides a CUDA int4 expert kernel for GPU-resident "hot" experts. Tested on **RTX 5060 Ti** (sm_120). Includes a self-test that validates GPU output against the CPU path. The GPU acts as an additional tier — experts that are frequently used can be pinned in VRAM, bypassing NVMe reads entirely.

---

## Conversion Pipeline

`convert_hy3.py` handles model preparation:
1. Downloads `tencent/Hy3-FP8` shard by shard (resumable)
2. Dequantizes every FP8 tensor using its per-tensor `weight_scale`
3. Re-quantizes routed experts to int4 group-128 (or int8)
4. Deletes each source shard as it goes (disk-bounded)
5. Everything else (attention, router, shared MLP, embed, norms) → bf16 passthrough

**One-command setup:**
```bash
python convert_hy3.py --repo tencent/Hy3-FP8 --out /nvme/hy3_i4g --ebits 4 --group 128 --stream
```

---

## Strengths

✅ **Frontier-class model on consumer hardware** — 295B parameters, no data-center GPU needed  
✅ **Faithful implementation** — validated token-exact against transformers reference  
✅ **No runtime dependencies** — pure C, no Python, no BLAS at inference time  
✅ **Resumable conversion** — disk-bounded, shard-by-shard, tolerant of interruptions  
✅ **OpenAI-compatible API** — drop-in replacement for any OpenAI client  
✅ **Auto-sizing** — never OOMs, expert cache sized from available RAM  
✅ **Optional GPU tier** — CUDA kernel for hot experts  
✅ **Apache 2.0 license**  

---

## Limitations

❌ **Slow decode** — 0.4–0.6 tok/s, I/O-bound by NVMe bandwidth  
❌ **Requires fast local NVMe** — no network mounts, ~160 GB free  
❌ **x86-64 only** — AVX2 required, no ARM/RISC-V support  
❌ **No batch inference** — single-token decode only  
❌ **Brand new project** — 1 commit, 0 stars, no community yet  
❌ **No Windows support** (yet) — POSIX shims exist but untested  
❌ **30 GB RAM minimum** — excludes most laptops  

---

## How It Compares to Alternatives

| Method | Hardware | Speed | Quality | Effort |
|--------|----------|-------|---------|--------|
| **hy3** (NVMe streamed) | Consumer PC + NVMe | 0.5 tok/s | Int4 group-128 | High (conversion) |
| **llama.cpp GGUF** | Consumer PC | 10–50 tok/s | Q4_K_M ~ 4-bit | Low (download) |
| **vLLM + AWQ** | 1× A100 (80 GB) | 100+ tok/s | AWQ 4-bit | Medium |
| **API (OpenAI/Claude)** | Cloud | Fast | Native | None |

**hy3 fills a unique niche:** the only way to run a 295B-class model on a ~$3,000 PC without cloud GPUs. It's not fast, but it *works*.

---

## Bottom Line

**hy3 is the most ambitious consumer-hardware LLM project I've seen in 2026.** It's:

- **Technically impressive** — pure C, AVX2 kernels, NVMe streaming, faithful Hy3 forward
- **Practically usable** — OpenAI-compatible server, one-command setup
- **Very early** — 1 commit, no community, unproven at scale

It's not a replacement for llama.cpp for everyday use, but it's the **only way to run a 295B MoE model on a consumer PC** — which is a genuinely remarkable achievement.

**Watch this project.** If it gets community adoption (quantization improvements, ARM support, batching), it could reshape what's possible on local hardware.