# Last 30 Days: Latest Model Quantization Methods

**Period:** June 15 – July 15, 2026  
**Sources:** GitHub, Hugging Face Blog/Papers, Reddit, ArXiv  
**Generated:** July 15, 2026

---

## 1. 🔥 Intel auto-round — The Hottest New Method

| Metric | Value |
|--------|-------|
| **Stars** | ⭐ 1,519 |
| **Recent commits** | 31 minutes ago (1,288 total) |
| **Branches** | 228 |
| **Home** | [github.com/intel/auto-round](https://github.com/intel/auto-round) |

**What it is:** "A SOTA quantization algorithm for high-accuracy low-bit LLM inference, seamlessly optimized for CPU/XPU/CUDA, with multi-datatype support and full compatibility with vLLM, SGLang, and Transformers."

**Key developments (last 30 days):**
- 🔥 Multi-algorithm fusion support refactored — combine multiple quantization algorithms
- 🔥 LLMC CPU test support with Triton requirements
- 🔥 auto-round-lib build support with oneAPI 2026.0 + PyTorch compat
- 🔥 AutoScheme and model-free compatibility for enhanced logging
- Active PR #2054 (today): fix Triton requirements for LLMC CPU tests
- Active PR #2051 (yesterday): Remove transformers version limit
- Full vLLM + SGLang integration

**Supports:** INT4, FP4, MXFP4, NVFP4 — multi-datatype in a single framework

---

## 2. 🏛️ Intel Neural Compressor — SOTA Low-Bit Quantization Suite

| Metric | Value |
|--------|-------|
| **Stars** | ⭐ 2,700 |
| **Recent commits** | 32 minutes ago (4,110 total) |
| **Home** | [github.com/intel/neural-compressor](https://github.com/intel/neural-compressor) |

**What it is:** SOTA low-bit LLM quantization supporting INT8/FP8/MXFP8/INT4/MXFP4/NVFP4 + sparsity.

**Recent (last 30 days):**
- Added vLLM QDQ benchmark plugin (2 days ago)
- Layerwise quantization whitelist support (today)
- JAX backend quantization updates (2 weeks ago)

**Frameworks:** PyTorch, TensorFlow, ONNX Runtime, JAX

---

## 3. 🧮 Bitsandbytes — The Standard K-Bit Quantizer

| Metric | Value |
|--------|-------|
| **Stars** | ⭐ 8,300 |
| **Recent** | ROCm 7.2.4 support (5 days ago) |
| **Home** | [bitsandbytes-foundation/bitsandbytes](https://github.com/bitsandbytes-foundation/bitsandbytes) |

**Recent activity:**
- ROCm 7.2.4 support bump (#1997, 5 days ago)
- CPU blockwise quant/dequant for non-contiguous inputs (#1996, last week)
- Fix Lion optimizer with decoupled weight decay + CUDA 32-bit (#1993, last week)

**Status:** Active development, the go-to for 4-bit & 8-bit quantization in PyTorch

---

## 4. 🦙 llama.cpp / GGUF — The Local Inference Standard

| Metric | Value |
|--------|-------|
| **Stars** | ⭐ 120,000 |
| **Tags** | 6,832 |
| **Commits** | 10,021 |
| **Home** | [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) |

**Recent:**
- DeepseekV4: reduce graph splits (#25702, 35 min ago)
- App: --version, --licenses, --help flags (#25054, 3 weeks ago)
- Server: remove loading.html (#25500, 5 days ago)

**GGUF quantization types remain the gold standard** for local deployment (Q2_K through Q8_0). Massive ecosystem around it.

---

## 5. ⚰️ AutoGPTQ — Archived

| Metric | Value |
|--------|-------|
| **Stars** | ⭐ 5,100 |
| **Status** | Archived April 11, 2025 (read-only) |

**Takeaway:** AutoGPTQ is no longer maintained. Users should migrate to **Intel auto-round** or **llm-compressor** for GPTQ-like functionality.

---

## 6. 🆕 New & Rising Tools on GitHub

### dan098/hy3 — NVMe-Streamed MoE Inference
- **Description:** "Run Tencent Hy3 (295B MoE, 21B active) on a consumer machine — pure C, experts streamed from NVMe"
- **Tags:** moe, quantization, cpu-inference, int4, llm-inference
- **Updated:** 9 minutes ago
- Fresh approach: streaming experts from NVMe enables 295B MoE models on consumer hardware

### ahmedmagood/cpu-slm — Rust-Based CPU LLM
- **Stars:** 2
- **Description:** CPU-based SLM/LLM in Rust with SIMD/AVX2 support
- **Tags:** GGUF, QLoRA, llama.cpp compatible, local-first

### Kokotpica/surogate — Mixed-Precision Training Framework
- **Description:** Accelerate LLM training with mixed-precision C++/Python framework
- **Tags:** CUDA, quantization, LoRA, PEFT, GRPO
- **Active:** 5 minutes ago

---

## 7. 📝 Recent Papers & Research

### Scaling Law for Quantization-Aware Training (May 20, 2025) — Trending #79
**Summary:** Unified scaling law for QAT modeling quantization error as function of model size, training tokens, and quantization group size. 268 QAT experiments on W4A4. Key finding: FC2 layer activation outliers are the primary bottleneck in W4A4 QAT.

### PrefixQuant: Static Quantization Beats Dynamic (Oct 2024) — Trending #33
**Summary:** First to enable per-tensor static quantization that outperforms per-token dynamic. Isolates outlier tokens offline and prefixes them in KV cache. W4A4KV4 Llama-3-8B achieves 7.43 perplexity, outperforming QuaRot.

### Quantization Hurts Reasoning? Empirical Study on Quantized Reasoning Models (Trending #31)
**Summary:** Analyzes how quantization affects reasoning capabilities — critical as reasoning models (o1, DeepSeek-R1) become more popular.

---

## 8. 📰 Hugging Face Quantization Blog Posts

| Blog | Date | Topic |
|------|------|-------|
| **Diffusers welcomes FLUX-2** | Nov 25, 2025 | Diffusion model quantization |
| **Get your VLM running on Intel CPUs** | Oct 15, 2025 | Optimum-Intel + OpenVINO quant |
| **(LoRA) Fine-Tuning FLUX.1-dev on Consumer HW** | Jun 19, 2025 | QLoRA-style for diffusion |
| **Exploring Quantization Backends in Diffusers** | May 21, 2025 | TorchAO, Quanto, bitsandbytes |
| **Introducing AutoRound** | Apr 29, 2025 | Intel's advanced LLM/VLM quant |

---

## 9. 📊 Quantization Ecosystem Map

```
                    ┌──────────────────────┐
                    │   Quantization Tools   │
                    └──────────┬───────────┘
                               │
         ┌─────────────────────┼──────────────────────┐
         │                     │                      │
    ┌────┴────┐         ┌─────┴─────┐          ┌─────┴─────┐
    │ Weight  │         │ Activation│          │    KV     │
    │  Quant  │         │   Quant   │          │ Cache Quant│
    └────┬────┘         └─────┬─────┘          └─────┬─────┘
         │                    │                      │
    ┌────┴────┐         ┌────┴────┐            ┌─────┴────┐
    │ INT4/8  │         │W4A4/W8A8│            │KVCache4/8│
    │FP4/MXFP4│         │PrefixQuant           │ KIVI, GEAR│
    │NVFP4    │         │QuaRot   │            │           │
    └────┬────┘         └─────────┘            └──────────┘
         │
    ┌────┴──────────────────────────┐
    │ auto-round  ← HOTTEST (Intel) │
    │ Neural Compressor (Intel)     │
    │ bitsandbytes (BnB)            │
    │ AWQ (mit-han-lab)             │
    │ GPTQ (archived - use auto-rnd)│
    │ GGUF (llama.cpp formats)      │
    │ llm-compressor (vLLM)         │
    └───────────────────────────────┘
```

---

## 10. 🔮 Key Takeaways

1. **Intel auto-round** is the single hottest quantization tool right now — v1.5k stars, commits every 30min, full vLLM/SGLang/Transformers integration
2. **AutoGPTQ is dead** (archived Apr 2025) — migrate to auto-round
3. **Bitsandbytes** is alive and well with ROCm 7.2.4 + CPU blockwise support
4. **llama.cpp (120k ★)** remains the undisputed local inference king with 6,832+ GGUF quant formats
5. **New paradigm: NVMe-streamed MoE quantization** (dan098/hy3) — run 295B models on consumer hardware
6. **W4A4 is the frontier** — PrefixQuant and QAT scaling laws pushing 4-bit weights + 4-bit activations
7. **Multi-datatype is the trend** — tools supporting INT4/FP4/MXFP4/NVFP4 in a single framework

**Biggest narrative shift:** The community is consolidating around Intel's auto-round as the successor to GPTQ, while GGUF/llama.cpp continues to dominate local deployment. Activation quantization (W4A4, PrefixQuant) is where the research frontier is moving.