<p align="center">
  <a href="README.md">English</a> |
  <a href="README.zh-CN.md">中文</a> |
  <a href="README.ja.md">日本語</a> |
  <a href="README.de.md">Deutsch</a> |
  <a href="README.uk.md">Українська</a>
</p>

<p align="center">
  <img src="https://compux.ai/logo.svg" alt="CompuX" width="200">
</p>

<h3 align="center">AI Compute Credit Marketplace</h3>

<p align="center">
  Convert $1M in financing into $1.25-1.5M in compute credits.<br>
  OpenAI-compatible API. Multi-provider. No lock-in.
</p>

<p align="center">
  <a href="https://github.com/CompuX-ai/compute-credit-financing/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License"></a>
  <a href="https://compux.ai"><img src="https://img.shields.io/badge/website-compux.ai-brightgreen" alt="Website"></a>
  <a href="https://docs.compux.ai"><img src="https://img.shields.io/badge/API_Docs-docs.compux.ai-blue" alt="API Docs"></a>
  <a href="https://compux.net"><img src="https://img.shields.io/badge/Learn-Knowledge_Base-orange" alt="Learn"></a>
  <a href="https://twitter.com/compux_ai"><img src="https://img.shields.io/twitter/follow/compux_ai" alt="Twitter"></a>
  <a href="https://www.linkedin.com/company/compux"><img src="https://img.shields.io/badge/LinkedIn-CompuX-0A66C2?logo=linkedin" alt="LinkedIn"></a>
</p>

---

## What is CompuX?

CompuX is a **three-sided marketplace** connecting AI startups, compute providers, and capital partners. We turn financing into compute credits at a 25-50% multiplier -- $1M becomes $1.25-1.5M in usable compute.

**Drop-in OpenAI replacement.** Change one line of code:

```python
# Before (OpenAI)
from openai import OpenAI
client = OpenAI(api_key="sk-...")

# After (CompuX) -- same SDK, same API, 25-50% cheaper
from openai import OpenAI
client = OpenAI(
    api_key="your-compux-key",
    base_url="https://api.compux.ai/v1"
)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Hello from CompuX!"}]
)
```

## Why CompuX?

- **25-50% cost savings** through compute credit financing (not discounts -- real financial multiplier)
- **OpenAI-compatible API** -- drop-in replacement, zero code changes
- **Multi-provider** -- OpenAI, Anthropic, Google, Mistral, open-source models
- **Blockable credits** -- collateralized compute that lenders can freeze/unfreeze
- **No lock-in** -- switch providers anytime, keep your credits

## Documentation

### API Reference

Everything you need to integrate CompuX into your application:

| Page | What you'll learn |
|------|-------------------|
| [Quickstart](api/quickstart.md) | Get running in 5 minutes — Python, TypeScript, Go, cURL |
| [API Reference](api/api-reference.md) | Endpoints, parameters, request/response schemas |
| [Available Models](api/models.md) | 100+ models across 6 providers with pricing |
| [Authentication](api/authentication.md) | API keys, scopes, rotation, sandbox environment |
| [Error Handling](api/errors.md) | HTTP status codes, error schema, retry logic |
| [Rate Limits](api/rate-limits.md) | RPM/TPM limits by plan, rate limit headers |
| [Pricing](api/pricing.md) | Plans, credit costs, financing multipliers, calculator |

### Code Examples

| Example | Language | What it shows |
|---------|----------|---------------|
| [quickstart.py](examples/quickstart.py) | Python | Basic chat completion |
| [quickstart.ts](examples/quickstart.ts) | TypeScript | Chat, streaming, multi-model comparison |
| [streaming.py](examples/streaming.py) | Python | Real-time token streaming |
| [error_handling.py](examples/error_handling.py) | Python | Retry logic with exponential backoff |
| [async_client.py](examples/async_client.py) | Python | High-throughput async with concurrency control |
| [function_calling.py](examples/function_calling.py) | Python | Tool use / function calling |
| [langchain_integration.py](examples/langchain_integration.py) | Python | LangChain + CompuX integration |

### Knowledge Base (Learn)

Deep-dive articles on AI compute economics, financing, and infrastructure:

| Section | Pages | What you'll learn |
|---------|-------|-------------------|
| [Concepts](concepts/) | 34 | Compute credits, token operators, GPU economics, LLM routing |
| [Comparisons](compare/) | 9 | CompuX vs OpenRouter, Together AI, Lambda Labs, venture debt |
| [Use Cases](use-cases/) | 7 | Startups, lenders, GPU providers, dev tools |
| [FAQ](faq/) | 10 | Pricing, integration, collateral, getting started |

## Quick Start

### 1. Get your API key

Sign up at [app.compux.ai](https://app.compux.ai/register) and create an API key.

### 2. Make your first request

```bash
curl https://api.compux.ai/v1/chat/completions \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4o",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

### 3. Use with any OpenAI-compatible SDK

```python
# Python
from openai import OpenAI
client = OpenAI(api_key="YOUR_API_KEY", base_url="https://api.compux.ai/v1")
```

```typescript
// TypeScript
import OpenAI from 'openai';
const client = new OpenAI({ apiKey: 'YOUR_API_KEY', baseURL: 'https://api.compux.ai/v1' });
```

## How It Works

```
AI Startup                    CompuX                      Compute Provider
    |                           |                               |
    |-- Needs compute --------->|                               |
    |                           |-- Financing ($1M) ----------->|
    |                           |<-- Credits ($1.25-1.5M) ------|
    |<-- Blockable credits -----|                               |
    |                           |                               |
    |-- API call (OpenAI fmt)-->|-- Routes to best provider --->|
    |<-- Response --------------|<-- Response ------------------|
```

**Layer 5: Token Operator** -- CompuX operates at Layer 5 of the AI value chain, between infrastructure (GPUs) and applications (AI products). We optimize the flow of compute credits like a financial operator.

## Key Concepts

| Concept | Description |
|---------|-------------|
| **Compute Credits** | Standardized units of compute across providers |
| **Credit Transfusion** | Converting financing into amplified compute credits |
| **Blockable Credits** | Credits that can be frozen/unfrozen as collateral |
| **Token Operator** | Layer 5 entity managing compute credit flow |
| **Multi-Provider Routing** | Automatic selection of optimal provider per request |

Read more in our [Concepts](concepts/) section.

## Community & Support

- [Website](https://compux.ai) -- Learn about CompuX
- [Knowledge Base](https://compux.net) -- In-depth articles and guides
- [API Docs](https://docs.compux.ai) -- API reference
- [Twitter](https://twitter.com/compux_ai) -- Updates and announcements
- [LinkedIn](https://www.linkedin.com/company/compux) -- Company news
- [GitHub](https://github.com/CompuX-ai) -- Open source projects
- [Contact](https://compux.ai/get-in-touch) -- Talk to us

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

This project is licensed under the MIT License -- see [LICENSE](LICENSE) for details.
