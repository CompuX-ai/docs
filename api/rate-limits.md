# Rate Limits

CompuX enforces rate limits to ensure fair usage and platform stability. Limits apply per API key and are measured in requests per minute (RPM) and tokens per minute (TPM). Higher plans get higher limits.

**Key Takeaways:**

* **Per-Key Limits** — Each API key has its own rate limit counters.
* **Two Dimensions** — Requests per minute (RPM) and tokens per minute (TPM).
* **Plan-Based** — Higher financing tiers get higher limits.
* **Transparent Headers** — Every response includes remaining quota in headers.
* **Graceful Handling** — 429 responses include `Retry-After` header for backoff.

## Rate Limits by Plan

### Chat Completions

| Plan | RPM (requests/min) | TPM (tokens/min) | Daily Request Cap |
|------|---------------------|-------------------|-------------------|
| **Free Tier** | 20 | 40,000 | 1,000 |
| **Sandbox** (`cpx_test_`) | 100 | 100,000 | 10,000 |
| **Starter** | 500 | 500,000 | Unlimited |
| **Growth** | 2,000 | 2,000,000 | Unlimited |
| **Scale** | 10,000 | 10,000,000 | Unlimited |
| **Enterprise** | Custom | Custom | Unlimited |

### Embeddings

| Plan | RPM | TPM |
|------|-----|-----|
| **Free Tier** | 50 | 100,000 |
| **Sandbox** | 200 | 500,000 |
| **Starter** | 1,000 | 2,000,000 |
| **Growth** | 5,000 | 10,000,000 |
| **Scale** | 20,000 | 50,000,000 |
| **Enterprise** | Custom | Custom |

### Other Endpoints

| Endpoint | All Plans |
|----------|-----------|
| `GET /v1/models` | 60 RPM |
| `GET /v1/account/credits` | 60 RPM |
| `GET /v1/account/usage` | 30 RPM |

## How Limits Work

### Sliding Window

Rate limits use a 60-second sliding window. Each request is counted for 60 seconds from when it was made. There is no "reset at the top of the minute" — the window moves continuously.

### Token Counting

For TPM limits, tokens are counted at request time:

- **Input tokens** — counted when the request is received
- **Output tokens** — counted when the response is generated
- **Streaming** — output tokens are counted as they are generated

A request that sends 1,000 input tokens and receives 500 output tokens counts as 1,500 tokens toward the TPM limit.

### Concurrent Requests

There is no hard concurrency limit. However, rate limits effectively cap throughput. A Starter plan at 500 RPM can sustain ~8 concurrent requests per second.

## Rate Limit Headers

Every API response includes these headers:

```
X-RateLimit-Limit-Requests: 500
X-RateLimit-Limit-Tokens: 500000
X-RateLimit-Remaining-Requests: 487
X-RateLimit-Remaining-Tokens: 492350
X-RateLimit-Reset-Requests: 2026-04-03T12:01:00Z
X-RateLimit-Reset-Tokens: 2026-04-03T12:01:00Z
```

### Reading Headers in Code

```python
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Hello"}],
)

# Access rate limit info from raw response
print(f"Remaining requests: {response.headers['X-RateLimit-Remaining-Requests']}")
print(f"Remaining tokens: {response.headers['X-RateLimit-Remaining-Tokens']}")
```

## When Limits Are Exceeded

A `429 Too Many Requests` response is returned:

```json
{
  "error": {
    "message": "Rate limit exceeded. Limit: 500 RPM. Current: 512 RPM. Retry after 3 seconds.",
    "type": "rate_limit_error",
    "code": "rate_limit_exceeded"
  }
}
```

The `Retry-After` header tells you exactly how long to wait:

```
HTTP/1.1 429 Too Many Requests
Retry-After: 3
```

## Handling Rate Limits

### Basic Strategy

1. Check `Retry-After` header on 429 responses
2. Wait the specified number of seconds
3. Retry the request

### Proactive Throttling

Monitor `X-RateLimit-Remaining-Requests` and slow down before hitting the limit:

```python
import time
from openai import OpenAI

client = OpenAI(api_key="YOUR_KEY", base_url="https://api.compux.ai/v1")

def throttled_request(messages, min_remaining=50):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
    )

    remaining = int(response.headers.get("X-RateLimit-Remaining-Requests", 100))
    if remaining < min_remaining:
        time.sleep(1)  # Slow down when approaching limit

    return response
```

### Batch Processing

For high-volume workloads, spread requests evenly across the rate limit window:

```python
import asyncio
from openai import AsyncOpenAI

client = AsyncOpenAI(api_key="YOUR_KEY", base_url="https://api.compux.ai/v1")

async def process_batch(items, rpm_limit=400):
    """Process items while staying under RPM limit."""
    delay = 60.0 / rpm_limit  # Seconds between requests
    results = []

    for item in items:
        response = await client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": item}],
        )
        results.append(response.choices[0].message.content)
        await asyncio.sleep(delay)

    return results
```

## Requesting Higher Limits

If your workload requires higher limits:

1. **Upgrade your plan** in the [dashboard](https://app.compux.ai/billing)
2. **Contact sales** at [compux.ai/get-in-touch](https://compux.ai/get-in-touch) for Enterprise custom limits
3. **Optimize requests** — use `gpt-4o-mini` for simple tasks to reduce token usage

Enterprise customers can request:
- Custom RPM/TPM limits
- Dedicated capacity (reserved GPU allocation)
- Priority routing (lower latency)
- Burst allowances (temporary limit increases)

## Related Resources

- [API Reference](api-reference.md) — Endpoint documentation
- [Error Handling](errors.md) — Error codes including 429 handling
- [Pricing](pricing.md) — Plan tiers and credit costs
- [Available Models](models.md) — Per-model limits and capabilities