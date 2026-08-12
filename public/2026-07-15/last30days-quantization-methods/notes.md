# Research Notes

## Methodology
Web search tools (firecrawl) were unavailable due to installation issues. Research conducted via:
- Browser navigation to GitHub repos (auto-round, neural-compressor, bitsandbytes, llama.cpp, AutoGPTQ, AWQ, llm-compressor)
- Browser navigation to Hugging Face Blog (quantization tag)
- Browser navigation to Hugging Face Daily Papers (quantization query)
- Browser navigation to GitHub topics and search results

## Key Observations

### Most Active (last 30 days)
1. **intel/auto-round** — 1,288 commits, 228 branches, 41 tags. Actively developed with multi-algorithm fusion, vLLM/SGLang integration, and multi-datatype support. Commits within the last hour.
2. **intel/neural-compressor** — 4,110 commits, 134 branches. Layerwise quantization, vLLM QDQ plugin, JAX support.
3. **bitsandbytes** — ROCm 7.2.4, CPU blockwise non-contiguous inputs.
4. **llama.cpp** — 10,021 commits, 616 branches, 6,832 tags. DeepseekV4 graph splits optimization.

### Dead Projects
- **AutoGPTQ** — Archived April 11, 2025. Read-only. Users should migrate.

### Rising Projects
- **dan098/hy3** — Novel approach: NVMe-streamed expert loading for MoE models on consumer hardware
- **ahmedmagood/cpu-slm** — Rust-based CPU LLM with SIMD/AVX2 + GGUF support
- **Kokotpica/surogate** — Mixed-precision training framework with GRPO support

### Research Frontier
- W4A4 quantization (4-bit weights + 4-bit activations) is the leading edge
- PrefixQuant shows static quantization can beat dynamic by prefixing outlier tokens
- QAT scaling laws being formalized for W4A4
- KV cache quantization (KIVI, GEAR) continues to mature

### Limitations
- Could not access Reddit r/LocalLLaMA (blocked)
- Could not access X/Twitter (no API keys)
- Could not access YouTube (no API keys)
- Could not search HN via API
- Research is GitHub/HF-centric due to data access constraints