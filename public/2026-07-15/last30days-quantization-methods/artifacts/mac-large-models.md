# MacBook Pro 48GB: Running Very Large Models — Options & Tradeoffs

**Target:** 48 GB unified memory MacBook Pro (Apple Silicon)  
**Goal:** Run the largest possible models locally

---

## The Memory Constraint

On Apple Silicon, **unified memory** is shared between GPU and CPU. You have ~48 GB total for:
- Model weights (quantized)
- KV cache
- OS overhead
- Expert cache / streaming buffers

**Realistic budget:** ~40–44 GB for the model itself.

---

## Option 1: 🥇 colibrì — NVMe-Streamed MoE (744B Models)

**GitHub:** https://github.com/JustVugg/colibri | **Stars:** ⭐ 14,700

This is the **parent project that hy3 is based on**, and it **actually supports Mac**. It runs **GLM-5.2 (744B-parameter MoE, ~40B active/token)** by streaming experts from disk.

### Why it wins for your 48GB MacBook Pro

| Feature | colibrì | hy3 |
|---------|---------|-----|
| **Mac support** | ✅ **Yes** — Metal backend + ARM NEON | ❌ x86 AVX2 only |
| **Model** | GLM-5.2 (744B MoE) | Tencent Hy3 (295B MoE) |
| **Stars** | 14,700 | 0 |
| **Maturity** | 247 commits, active community | 1 commit, brand new |
| **License** | Apache 2.0 | Apache 2.0 |

### Mac Performance Data (from real users)

| Machine | Config | Speed |
|---------|--------|-------|
| **Mac Mini M4 Pro (48 GB)** | Metal, `--ram 38` | **0.30 tok/s** (vs 0.18 CPU-only) |
| Apple M5 Max (128 GB) | Metal, 39.7 GB pin | **1.83 tok/s** |
| Apple M5 Max (128 GB) | Metal, 46.9 GB pin, 2.94M history | **2.06 tok/s** |

### What you'd get on a 48GB M4 Pro MacBook

Based on the M4 Pro 48 GB datapoint:
- **~0.3–0.5 tok/s** with Metal backend
- ~5–15 seconds per token when cold
- After warmup (cache learning), ~2–3 seconds per token
- Full 744B frontier model answering correctly

### Setup

```bash
# Install dependencies
brew install libomp       # OpenMP support

# Build with Metal backend
cd c
make glm METAL=1

# Convert model (one-time, needs Python)
pip install torch safetensors huggingface_hub
./coli convert --model /path/to/glm52_i4

# Chat
COLI_METAL=1 COLI_MODEL=/path/glm52_i4 ./coli chat --ram 38
```

---

## Option 2: 🥈 MLX + mlx-lm — Native Apple Silicon (Models That Fit in RAM)

**GitHub:** https://github.com/ml-explore/mlx | **Stars:** ⭐ 27,600

Apple's own ML framework, purpose-built for Apple Silicon. Uses the **full GPU via Metal** with zero overhead.

### What fits in 48GB at 4-bit quantization

| Model Size | 4-bit Weights | + KV Cache | Fits in 48GB? |
|-----------|---------------|------------|---------------|
| 70B | ~35 GB | ~4 GB | ✅ **Yes** |
| 120B | ~60 GB | ~6 GB | ❌ No |
| 8×22B (MoE) | ~44 GB | ~4 GB | ✅ **Tight fit** |
| 405B (dense) | ~200 GB | — | ❌ Way too big |

### Speed

**Much faster than colibrì** — 10–50 tok/s for models that fit, since everything is in unified memory with no disk streaming.

### Best models for 48GB

- **70B models at 4-bit** (Llama 3, Qwen 2.5, DeepSeek V3 Lite) — 10–20 tok/s
- **Mixtral 8×22B at 4-bit** (~44 GB) — native MoE, fast
- **Command R+ (104B) at 3-bit** — tight fit
- **Qwen 2.5 72B at 4-bit** — solid fit

### Setup

```bash
pip install mlx-lm

# Chat with a 4-bit 70B model
mlx_lm.chat --model mlx-community/Qwen-2.5-72B-Instruct-4bit

# Or generate
mlx_lm.generate --model mlx-community/Llama-3.3-70B-Instruct-4bit \
  --prompt "Explain quantum computing" --max-tokens 256
```

---

## Option 3: 🥉 llama.cpp + GGUF — The Universal Workhorse

**GitHub:** https://github.com/ggml-org/llama.cpp | **Stars:** ⭐ 120,000

### Mac Support
✅ **Metal backend** built-in  
✅ **ARM NEON** kernels  
✅ Well-tested on Mac, huge community

### What fits in 48GB

Same as MLX — models up to ~70B at 4-bit:

| Quant | 70B Model | 120B Model |
|-------|-----------|------------|
| Q4_K_M | ~38 GB ✅ | ~65 GB ❌ |
| Q3_K_M | ~30 GB ✅ | ~50 GB ❌ |
| Q2_K | ~22 GB ✅ | ~35 GB ✅ |

### Speed

Comparable to MLX on Apple Silicon. 10–40 tok/s for models that fit.

### Setup

```bash
# Install
brew install llama.cpp

# Or build from source with Metal
git clone https://github.com/ggml-org/llama.cpp
cd llama.cpp && LLAMA_METAL=1 make -j

# Run a 4-bit 70B
llama-cli -m Qwen-2.5-72B-Q4_K_M.gguf -ngl 999 -p "Hello"
```

---

## Option 4: 💡 Running Hy3-Style Models on Mac

**hy3 itself does NOT support Mac** — it's pure C with x86 AVX2 intrinsics, no ARM/NEON kernels.

But **colibrì** (the parent project) supports Mac and is the same concept. You can run:
- **GLM-5.2 (744B MoE)** — bigger than Hy3
- Via Metal backend on Apple Silicon unified memory
- With MTP speculative decoding to boost throughput

---

## Comparison Table

| Method | Max Model | Speed | Mac Support | Setup Effort |
|--------|-----------|-------|-------------|--------------|
| **colibrì** (streaming MoE) | **744B** | 0.3–2 tok/s | ✅ Metal + ARM NEON | Medium |
| **MLX** (native) | ~70B | 10–50 tok/s | ✅ Native | Very Easy |
| **llama.cpp GGUF** (universal) | ~70B | 10–40 tok/s | ✅ Metal | Easy |
| **hy3** (NVMe MoE) | 295B | 0.5 tok/s | ❌ x86 only | Medium |

---

## Recommendation for Your 48GB MacBook Pro

### If you want the **biggest possible model** (any speed):
→ **colibrì** — runs a 744B GLM-5.2 at ~0.3 tok/s on M4 Pro 48GB.  
  `make glm METAL=1` + `COLI_METAL=1` + `--ram 38`

### If you want **fast inference** on a capable model:
→ **MLX** — run a 70B at 4-bit (Qwen 2.5, Llama 3.3) at 10–20 tok/s.  
  `pip install mlx-lm && mlx_lm.chat`

### If you want the **best ecosystem** and flexibility:
→ **llama.cpp GGUF** — thousands of pre-quantized models, best tooling.  
  `brew install llama.cpp`

### The sweet spot for "very large" on 48GB:
**colibrì** is your only option for 295B–744B class models. But expect ~3–5 seconds per token on a warm cache. For interactive use, **MLX with a 70B at 4-bit** is the pragmatic choice: 10× faster and still a very capable model.

---

## Files

**Full report:** `outputs/2026-07-15/last30days-quantization-methods/artifacts/mac-large-models.md`  
**Online:** https://duke-plc-priority-seating.trycloudflare.com/mac-large-models.md