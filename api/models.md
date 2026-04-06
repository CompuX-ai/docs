# Available Models on CompuX

CompuX routes requests to 100+ models across six major providers through a single OpenAI-compatible API. Every model listed here works with the same base URL (`https://api.compux.ai/v1`) and the same SDK — change the `model` parameter and you are done.

**Key Takeaways:**

* **100+ Models** — Access OpenAI, Anthropic, Google, Mistral, Meta, and open-source models from one API key.
* **Same SDK** — Use the OpenAI Python/TypeScript/Go SDK. No provider-specific libraries needed.
* **Smart Routing** — CompuX automatically selects the fastest, cheapest available provider unless you override with `X-CompuX-Provider`.
* **Cost Savings** — All models are 25-50% cheaper than direct pricing through [compute credit financing](../concepts/compute-credits.md).
* **Real-Time List** — Call `GET /v1/models` to get the current list with live pricing.

## How to List Models

```bash
curl https://api.compux.ai/v1/models \
  -H "Authorization: Bearer $COMPUX_API_KEY"
```

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["COMPUX_API_KEY"],
    base_url="https://api.compux.ai/v1",
)

for model in client.models.list():
    print(f"{model.id} — {model.owned_by}")
```

## Chat Completion Models

### OpenAI Models

| Model ID | Context | Input (per 1M tokens) | Output (per 1M tokens) | Vision | Tools | Streaming |
|----------|---------|----------------------|------------------------|--------|-------|-----------|
| `gpt-5.4` | 1.1M | $2.50 | $15.00 | Yes | Yes | Yes |
| `gpt-5.4-pro` | 1.1M | $30.00 | $180.00 | Yes | Yes | Yes |
| `gpt-4o` | 128K | $2.50 | $10.00 | Yes | Yes | Yes |
| `gpt-4o-mini` | 128K | $0.15 | $0.60 | Yes | Yes | Yes |
| `gpt-4-turbo` | 128K | $10.00 | $30.00 | Yes | Yes | Yes |
| `o3` | 200K | $10.00 | $40.00 | Yes | Yes | Yes |
| `o3-mini` | 200K | $1.10 | $4.40 | No | Yes | Yes |
| `o4-mini` | 200K | $1.10 | $4.40 | Yes | Yes | Yes |
| `gpt-4.1` | 1M | $2.00 | $8.00 | Yes | Yes | Yes |
| `gpt-4.1-mini` | 1M | $0.40 | $1.60 | Yes | Yes | Yes |
| `gpt-4.1-nano` | 1M | $0.10 | $0.40 | Yes | Yes | Yes |

### Anthropic Models

| Model ID | Context | Input (per 1M tokens) | Output (per 1M tokens) | Vision | Tools | Streaming |
|----------|---------|----------------------|------------------------|--------|-------|-----------|
| `claude-opus-4-6-20260205` | 1M | $5.00 | $25.00 | Yes | Yes | Yes |
| `claude-sonnet-4-6-20260217` | 1M | $3.00 | $15.00 | Yes | Yes | Yes |
| `claude-opus-4-20250514` | 200K | $15.00 | $75.00 | Yes | Yes | Yes |
| `claude-sonnet-4-20250514` | 200K | $3.00 | $15.00 | Yes | Yes | Yes |
| `claude-haiku-3-5-20241022` | 200K | $0.80 | $4.00 | Yes | Yes | Yes |

### Google Models

| Model ID | Context | Input (per 1M tokens) | Output (per 1M tokens) | Vision | Tools | Streaming |
|----------|---------|----------------------|------------------------|--------|-------|-----------|
| `gemini-3.1-pro` | 200K+ | $2.00 | $12.00 | Yes | Yes | Yes |
| `gemini-3.1-flash-lite` | 200K+ | $0.25 | $1.50 | Yes | Yes | Yes |
| `gemini-2.5-pro` | 1M | $1.25 | $10.00 | Yes | Yes | Yes |
| `gemini-2.5-flash` | 1M | $0.15 | $0.60 | Yes | Yes | Yes |
| `gemini-2.0-flash` | 1M | $0.10 | $0.40 | Yes | Yes | Yes |

### Mistral Models

| Model ID | Context | Input (per 1M tokens) | Output (per 1M tokens) | Vision | Tools | Streaming |
|----------|---------|----------------------|------------------------|--------|-------|-----------|
| `mistral-large-3` | 256K | $2.00 | $6.00 | Yes | Yes | Yes |
| `mistral-large-latest` | 128K | $2.00 | $6.00 | No | Yes | Yes |
| `mistral-medium-latest` | 128K | $2.70 | $8.10 | No | Yes | Yes |
| `mistral-small-latest` | 128K | $0.20 | $0.60 | No | Yes | Yes |
| `codestral-latest` | 256K | $0.30 | $0.90 | No | Yes | Yes |

### Meta (Open-Source) Models

| Model ID | Context | Input (per 1M tokens) | Output (per 1M tokens) | Vision | Tools | Streaming |
|----------|---------|----------------------|------------------------|--------|-------|-----------|
| `llama-4-maverick` | 1M | $0.20 | $0.60 | Yes | Yes | Yes |
| `llama-4-scout` | 10M | $0.15 | $0.45 | Yes | Yes | Yes |
| `llama-3.3-70b` | 128K | $0.10 | $0.30 | No | Yes | Yes |
| `llama-3.1-8b` | 128K | $0.05 | $0.10 | No | No | Yes |

### DeepSeek Models

| Model ID | Context | Input (per 1M tokens) | Output (per 1M tokens) | Vision | Tools | Streaming |
|----------|---------|----------------------|------------------------|--------|-------|-----------|
| `deepseek-v4` | 1M | $0.30 | $0.50 | Yes | Yes | Yes |
| `deepseek-r1` | 128K | $0.55 | $2.19 | No | No | Yes |
| `deepseek-v3` | 128K | $0.27 | $1.10 | No | Yes | Yes |

## Embedding Models

| Model ID | Provider | Dimensions | Max Input | Cost (per 1M tokens) |
|----------|----------|------------|-----------|---------------------|
| `text-embedding-3-large` | OpenAI | 3072 | 8191 | $0.13 |
| `text-embedding-3-small` | OpenAI | 1536 | 8191 | $0.02 |
| `text-embedding-ada-002` | OpenAI | 1536 | 8191 | $0.10 |

## Model Selection Guide

### By Use Case

| Use Case | Recommended Model | Why |
|----------|-------------------|-----|
| **Production chat** | `gpt-5.4` or `claude-sonnet-4-6-20260217` | Best quality/cost balance (Q1 2026) |
| **High-volume, low-cost** | `gpt-4o-mini` or `gemini-2.5-flash` | Under $1/M tokens, fast |
| **Complex reasoning** | `gpt-5.4` or `claude-opus-4-6-20260205` | 1M+ context, adaptive thinking |
| **Code generation** | `deepseek-v4` (81% SWE-bench) or `gemini-3.1-pro` (80.6%) | Q1 2026 coding leaders |
| **Long context** | `gemini-2.5-pro` (1M) or `llama-4-scout` (10M) | Million+ token windows |
| **Budget-conscious** | `deepseek-v4` ($0.30/M) or `llama-4-scout` ($0.08/M) | Frontier quality at budget pricing |
| **Vision/multimodal** | `gpt-4o` or `gemini-2.5-pro` | Image understanding |
| **Embeddings** | `text-embedding-3-small` | Best value for search/RAG |

### By Budget

| Monthly Budget | Best Model Mix | Estimated Requests |
|---------------|----------------|-------------------|
| Under $100 | `gpt-4o-mini` + `llama-3.1-8b` | ~500K requests |
| $100-500 | `gpt-4o` + `gpt-4o-mini` routing | ~200K requests |
| $500-2000 | `claude-sonnet-4-20250514` + `gpt-4o` | ~100K requests |
| $2000+ | Full model access + routing optimization | Unlimited |

## Provider Routing

By default, CompuX routes each request to the optimal provider based on:

1. **Cost** — Cheapest available provider for the requested model
2. **Latency** — Fastest response time from current region
3. **Availability** — Active providers with capacity

Override routing with the `X-CompuX-Provider` header:

```bash
curl https://api.compux.ai/v1/chat/completions \
  -H "Authorization: Bearer $COMPUX_API_KEY" \
  -H "X-CompuX-Provider: anthropic" \
  -H "Content-Type: application/json" \
  -d '{"model": "claude-sonnet-4-20250514", "messages": [{"role": "user", "content": "Hello"}]}'
```

## Model Aliases

CompuX supports shorthand aliases for common models:

| Alias | Resolves To |
|-------|-------------|
| `gpt-4o` | Latest GPT-4o version |
| `claude-sonnet` | Latest Claude Sonnet (currently 4.6) |
| `claude-opus` | Latest Claude Opus (currently 4.6) |
| `gemini-pro` | Latest Gemini Pro (currently 3.1) |
| `mistral-large` | Latest Mistral Large (currently 3) |

Pin to a specific version for reproducibility:

```python
# Alias (auto-updates)
model="gpt-4o"

# Pinned (stable)
model="gpt-4o-2024-08-06"
```

## Feature Support Matrix

| Feature | OpenAI | Anthropic | Google | Mistral | Meta |
|---------|--------|-----------|--------|---------|------|
| Chat completions | Yes | Yes | Yes | Yes | Yes |
| Streaming | Yes | Yes | Yes | Yes | Yes |
| Function calling | Yes | Yes | Yes | Yes | Partial* |
| Vision (images) | Yes | Yes | Yes | No | Partial** |
| JSON mode | Yes | Yes | Yes | Yes | No |
| System messages | Yes | Yes | Yes | Yes | Yes |
| Seed (deterministic) | Yes | No | No | No | No |

*\*Partial function calling (Meta): Supported on Llama 4 Maverick and Llama 3.3-70B. Not supported on Llama 3.1-8B. Sending `tools` to an unsupported model returns `400 invalid_request`.*

*\*\*Partial vision (Meta): Supported on Llama 4 Maverick and Llama 4 Scout. Not supported on Llama 3.x models.*

## Related Resources

- [API Reference](api-reference.md) — Endpoint documentation
- [Pricing](pricing.md) — Credit costs and conversion rates
- [Rate Limits](rate-limits.md) — Per-model request limits
- [LLM Routing](../concepts/llm-routing.md) — How multi-provider routing works
- [LLM API Pricing Comparison](../compare/llm-api-pricing-comparison.md) — CompuX vs direct pricing