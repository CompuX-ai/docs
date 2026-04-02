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

<h3 align="center">AI 算力信用额度市场</h3>

<p align="center">
  将100万美元融资转化为125-150万美元的算力额度。<br>
  兼容 OpenAI 的 API。多供应商。无锁定。
</p>

<p align="center">
  <a href="https://github.com/CompuX-ai/docs/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License"></a>
  <a href="https://compux.ai"><img src="https://img.shields.io/badge/website-compux.ai-brightgreen" alt="Website"></a>
  <a href="https://docs.compux.ai"><img src="https://img.shields.io/badge/API_Docs-docs.compux.ai-blue" alt="API Docs"></a>
  <a href="https://learn-compux.kossanstin.workers.dev"><img src="https://img.shields.io/badge/Learn-Knowledge_Base-orange" alt="Learn"></a>
  <a href="https://twitter.com/compux_ai"><img src="https://img.shields.io/twitter/follow/compux_ai" alt="Twitter"></a>
</p>

---

## 什么是 CompuX？

CompuX 是一个**三方市场**，连接 AI 初创企业、算力供应商和资本合作伙伴。我们将融资转化为算力额度，提供 25-50% 的乘数效应 — 100万美元变成125-150万美元的可用算力。

**直接替换 OpenAI。** 只需更改一行代码：

```python
# 之前 (OpenAI)
from openai import OpenAI
client = OpenAI(api_key="sk-...")

# 之后 (CompuX) — 相同的 SDK，相同的 API，便宜 25-50%
from openai import OpenAI
client = OpenAI(
    api_key="your-compux-key",
    base_url="https://api.compux.ai/v1"
)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "你好，来自 CompuX！"}]
)
```

## 为什么选择 CompuX？

- **节省 25-50%** 通过算力信用融资（不是折扣 — 真实的金融乘数）
- **兼容 OpenAI 的 API** — 直接替换，零代码更改
- **多供应商** — OpenAI、Anthropic、Google、Mistral、开源模型
- **可冻结额度** — 可作为抵押品冻结/解冻的算力
- **无锁定** — 随时切换供应商，保留您的额度

## 文档

### 知识库 (Learn)

关于 AI 算力经济学、融资和基础设施的深度文章。

| 板块 | 页数 | 您将了解 |
|------|------|----------|
| [概念](concepts/) | 34 | 算力额度、Token 运营商、GPU 经济学、LLM 路由 |
| [对比](compare/) | 9 | CompuX vs OpenRouter、Together AI、Lambda Labs、风险债务 |
| [应用场景](use-cases/) | 7 | 初创企业、贷方、GPU 供应商、开发工具 |
| [常见问题](faq/) | 10 | 490 个关于定价、集成、抵押的问答 |

### API 参考

完整 API 文档请访问 **[docs.compux.ai](https://docs.compux.ai)**。

- [Chat Completions](https://docs.compux.ai/docs/api-reference/chat-completions) — 兼容 OpenAI 的端点
- [身份验证](https://docs.compux.ai/docs/authentication/api-keys) — API 密钥和 JWT 认证
- [模型](https://docs.compux.ai/docs/api-reference/models) — 可用模型和供应商
- [快速开始](https://docs.compux.ai/docs/getting-started/quickstart) — 5分钟内启动

## 快速开始

### 1. 获取 API 密钥

在 [app.compux.ai](https://app.compux.ai/register) 注册并创建 API 密钥。

### 2. 发送第一个请求

```bash
curl https://api.compux.ai/v1/chat/completions \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4o",
    "messages": [{"role": "user", "content": "你好！"}]
  }'
```

### 3. 使用任何兼容 OpenAI 的 SDK

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

## 工作原理

```
AI 初创企业                   CompuX                      算力供应商
    |                           |                               |
    |-- 需要算力 -------------->|                               |
    |                           |-- 融资 ($1M) ---------------->|
    |                           |<-- 额度 ($1.25-1.5M) ---------|
    |<-- 可冻结额度 ------------|                               |
    |                           |                               |
    |-- API 请求 (OpenAI 格式)->|-- 路由到最佳供应商 ----------->|
    |<-- 响应 ------------------|<-- 响应 ----------------------|
```

**第5层：Token 运营商** — CompuX 运营在 AI 价值链的第5层，位于基础设施（GPU）和应用（AI 产品）之间。我们像金融运营商一样优化算力额度的流动。

## 关键概念

| 概念 | 描述 |
|------|------|
| **算力额度** | 跨供应商的标准化算力单位 |
| **信用转化** | 将融资转化为放大的算力额度 |
| **可冻结额度** | 可作为抵押品冻结/解冻的额度 |
| **Token 运营商** | 管理算力额度流动的第5层实体 |
| **多供应商路由** | 自动为每个请求选择最优供应商 |

在 [概念](concepts/) 板块了解更多。

## 社区与支持

- [官网](https://compux.ai) — 了解 CompuX
- [知识库](https://learn-compux.kossanstin.workers.dev) — 深度文章和指南
- [API 文档](https://docs.compux.ai) — API 参考
- [Twitter](https://twitter.com/compux_ai) — 更新和公告
- [LinkedIn](https://www.linkedin.com/company/compux) — 公司新闻
- [GitHub](https://github.com/CompuX-ai) — 开源项目
- [联系我们](https://compux.ai/get-in-touch) — 与我们沟通

## 贡献

欢迎贡献！请参阅 [CONTRIBUTING.md](CONTRIBUTING.md) 了解指南。

## 许可证

本项目基于 MIT 许可证 — 详见 [LICENSE](LICENSE)。