# Pricing

CompuX charges for API usage in compute credits. Credits are the universal currency across all providers and models. The key advantage: through [compute credit financing](../concepts/compute-credits.md), your dollars convert into 25-50% more credits than buying directly from providers.

**Key Takeaways:**

* **Credit-Based Pricing** — All usage is measured in compute credits, not dollars per token.
* **25-50% Multiplier** — $1M in financing becomes $1.25-1.5M in usable credits.
* **Transparent** — Check your balance, usage, and costs in real-time via API or dashboard.
* **No Markup on Tokens** — CompuX passes through provider pricing. Savings come from financing, not discounts.
* **Pay-as-You-Go or Financed** — Start with pay-as-you-go, upgrade to financing for the multiplier.

## How Credits Work

1 compute credit = $1 USD worth of API usage at provider list prices.

When you use a model, credits are deducted based on the provider's token pricing:

```
Credits used = (input_tokens × input_price + output_tokens × output_price) / 1,000,000
```

**Example:** A GPT-4o request with 1,000 input tokens and 500 output tokens:

```
Credits = (1,000 × $2.50 + 500 × $10.00) / 1,000,000
Credits = ($2,500 + $5,000) / 1,000,000
Credits = $0.0075
```

That request costs 0.0075 credits ($0.0075 at list price). With a 1.35x financing multiplier, your effective cost is $0.0056 — a 25% saving.

## Plans

| Plan | Monthly Credits | Price | Financing Multiplier | Best For |
|------|----------------|-------|---------------------|----------|
| **Free** | 5 credits | $0 | 1.0x | Testing and evaluation |
| **Starter** | 100 credits | $100/mo | 1.0x (no financing) | Small projects, prototyping |
| **Growth** | 1,000 credits | $800/mo | 1.25x | Startups with product-market fit |
| **Scale** | 10,000 credits | $7,000/mo | 1.35x | Series A/B companies |
| **Enterprise** | Custom | Custom | Up to 1.50x | High-volume, custom terms |

### Financing Multiplier Explained

The multiplier is CompuX's core value. Through bulk purchasing agreements with providers and [non-dilutive financing](../concepts/non-dilutive-ai-compute-funding.md):

- **Growth (1.25x):** Pay $800 → get $1,000 in credits. Save 20%.
- **Scale (1.35x):** Pay $7,000 → get $9,450 in credits. Save 26%.
- **Enterprise (1.50x):** Pay $100,000 → get $150,000 in credits. Save 33%.

The multiplier increases with commitment. Annual contracts get higher multipliers than monthly.

## Token Pricing by Model

Credits map directly to provider token prices. Here are the effective costs (before financing multiplier):

### Chat Models — Cost per 1M Tokens in Credits

| Model | Input Credits | Output Credits |
|-------|--------------|----------------|
| `gpt-4o` | 2.50 | 10.00 |
| `gpt-4o-mini` | 0.15 | 0.60 |
| `gpt-4.1` | 2.00 | 8.00 |
| `gpt-4.1-mini` | 0.40 | 1.60 |
| `gpt-4.1-nano` | 0.10 | 0.40 |
| `claude-sonnet-4-20250514` | 3.00 | 15.00 |
| `claude-haiku-3-5-20241022` | 0.80 | 4.00 |
| `gemini-2.5-pro` | 1.25 | 10.00 |
| `gemini-2.5-flash` | 0.15 | 0.60 |
| `mistral-large-latest` | 2.00 | 6.00 |
| `llama-4-maverick` | 0.20 | 0.60 |
| `llama-3.1-8b` | 0.05 | 0.10 |

**With Scale plan (1.35x multiplier):** Divide credit costs by 1.35 to get your actual USD cost. GPT-4o output becomes $7.41/M tokens instead of $10.00.

### Embedding Models

| Model | Credits per 1M Tokens |
|-------|-----------------------|
| `text-embedding-3-large` | 0.13 |
| `text-embedding-3-small` | 0.02 |

## Cost Calculator

### Monthly Estimate Formula

```
Monthly cost = (daily_requests × avg_input_tokens × input_price
              + daily_requests × avg_output_tokens × output_price)
              × 30 / 1,000,000 / financing_multiplier
```

### Example Scenarios

**Chatbot (10K requests/day, GPT-4o-mini):**
```
Input:  10,000 × 500 tokens × $0.15/M = $0.75/day
Output: 10,000 × 200 tokens × $0.60/M = $1.20/day
Monthly: ($0.75 + $1.20) × 30 = $58.50 in credits
With Growth (1.25x): $46.80/month actual cost
```

**RAG Pipeline (5K requests/day, GPT-4o):**
```
Input:  5,000 × 3,000 tokens × $2.50/M = $37.50/day
Output: 5,000 × 1,000 tokens × $10.00/M = $50.00/day
Monthly: ($37.50 + $50.00) × 30 = $2,625 in credits
With Scale (1.35x): $1,944/month actual cost (saves $681)
```

**High-Volume Inference (100K requests/day, Llama-3.1-8b):**
```
Input:  100,000 × 200 tokens × $0.05/M = $1.00/day
Output: 100,000 × 100 tokens × $0.10/M = $1.00/day
Monthly: ($1.00 + $1.00) × 30 = $60 in credits
Starter plan: $60/month
```

## Checking Your Balance

### Via API

```bash
curl https://api.compux.ai/v1/account/credits \
  -H "Authorization: Bearer $COMPUX_API_KEY"
```

Response:
```json
{
  "total_credits": 10000.00,
  "used_credits": 3247.58,
  "remaining_credits": 6752.42,
  "blocked_credits": 0.00,
  "plan": "scale",
  "financing_multiplier": 1.35
}
```

### Via Dashboard

[app.compux.ai/billing](https://app.compux.ai/billing) — Real-time balance, usage graphs, and invoices.

### In API Responses

Every response includes credit usage in the `x_compux` extension:

```json
{
  "x_compux": {
    "provider": "openai",
    "credits_used": 0.0075,
    "credits_remaining": 6752.42
  }
}
```

## Usage Tracking

### Detailed Usage Report

```bash
curl "https://api.compux.ai/v1/account/usage?start_date=2026-04-01&end_date=2026-04-03" \
  -H "Authorization: Bearer $COMPUX_API_KEY"
```

### Budget Alerts

Set alerts in the dashboard or per API key:
- **Warning** — Notify at 80% of monthly budget
- **Critical** — Notify at 95% of monthly budget
- **Hard limit** — Stop requests at 100% (optional, per-key)

## Billing

- **Monthly billing** — Credits reset each billing cycle. Unused credits roll over for 90 days.
- **Annual contracts** — Pay upfront for higher multipliers. Credits valid for 12 months.
- **Top-ups** — Buy additional credits at any time at your plan's multiplier rate.
- **Invoicing** — Available for Scale and Enterprise plans.

## No Hidden Fees

| Fee Type | CompuX |
|----------|--------|
| API requests | Included in token pricing |
| Streaming | No surcharge |
| Function calling | No surcharge |
| Provider routing | No surcharge |
| Data egress | Free |
| Support | Free (Starter+) |

## Related Resources

- [API Reference](api-reference.md) — Endpoint documentation
- [Available Models](models.md) — Full model list with per-model pricing
- [Compute Credits](../concepts/compute-credits.md) — How the credit system works
- [Compute Credit Transfusion](../concepts/compute-credit-transfusion-guide.md) — How financing multipliers work
- [CompuX vs Cloud Credits](../compare/compux-vs-cloud-credits.md) — Comparison with AWS/GCP startup credits
- [GPU Pricing Comparison](../compare/gpu-pricing-comparison-2026.md) — Market rate benchmarks