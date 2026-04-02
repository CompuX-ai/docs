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

<h3 align="center">AIコンピュートクレジットマーケットプレイス</h3>

<p align="center">
  100万ドルの資金調達を125〜150万ドルのコンピュートクレジットに変換。<br>
  OpenAI互換API。マルチプロバイダー。ロックインなし。
</p>

<p align="center">
  <a href="https://github.com/CompuX-ai/docs/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License"></a>
  <a href="https://compux.ai"><img src="https://img.shields.io/badge/website-compux.ai-brightgreen" alt="Website"></a>
  <a href="https://docs.compux.ai"><img src="https://img.shields.io/badge/API_Docs-docs.compux.ai-blue" alt="API Docs"></a>
  <a href="https://learn-compux.kossanstin.workers.dev"><img src="https://img.shields.io/badge/Learn-Knowledge_Base-orange" alt="Learn"></a>
  <a href="https://twitter.com/compux_ai"><img src="https://img.shields.io/twitter/follow/compux_ai" alt="Twitter"></a>
</p>

---

## CompuXとは？

CompuXは、AIスタートアップ、コンピュートプロバイダー、資本パートナーを結ぶ**三者間マーケットプレイス**です。資金調達をコンピュートクレジットに変換し、25〜50%の乗数効果を実現します — 100万ドルが125〜150万ドルの利用可能なコンピュートになります。

**OpenAIの直接代替。** コード1行を変更するだけ：

```python
# 変更前 (OpenAI)
from openai import OpenAI
client = OpenAI(api_key="sk-...")

# 変更後 (CompuX) — 同じSDK、同じAPI、25〜50%安い
from openai import OpenAI
client = OpenAI(
    api_key="your-compux-key",
    base_url="https://api.compux.ai/v1"
)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "CompuXからこんにちは！"}]
)
```

## なぜCompuX？

- **25〜50%のコスト削減** コンピュートクレジットファイナンスによる（割引ではなく、実際の金融乗数）
- **OpenAI互換API** — ドロップイン代替、コード変更ゼロ
- **マルチプロバイダー** — OpenAI、Anthropic、Google、Mistral、オープンソースモデル
- **ブロック可能クレジット** — 貸し手が凍結/解凍できる担保付きコンピュート
- **ロックインなし** — いつでもプロバイダーを切り替え、クレジットを保持

## ドキュメント

### ナレッジベース (Learn)

AIコンピュート経済学、ファイナンス、インフラに関する詳細記事。

| セクション | ページ数 | 学べること |
|-----------|---------|-----------|
| [コンセプト](concepts/) | 34 | コンピュートクレジット、トークンオペレーター、GPU経済学、LLMルーティング |
| [比較](compare/) | 9 | CompuX vs OpenRouter、Together AI、Lambda Labs、ベンチャーデット |
| [ユースケース](use-cases/) | 7 | スタートアップ、貸し手、GPUプロバイダー、開発ツール |
| [FAQ](faq/) | 10 | 価格、統合、担保に関する490のQ&A |

### APIリファレンス

完全なAPIドキュメントは **[docs.compux.ai](https://docs.compux.ai)** をご覧ください。

- [Chat Completions](https://docs.compux.ai/docs/api-reference/chat-completions) — OpenAI互換エンドポイント
- [認証](https://docs.compux.ai/docs/authentication/api-keys) — APIキーとJWT認証
- [モデル](https://docs.compux.ai/docs/api-reference/models) — 利用可能なモデルとプロバイダー
- [クイックスタート](https://docs.compux.ai/docs/getting-started/quickstart) — 5分で開始

## クイックスタート

### 1. APIキーを取得

[app.compux.ai](https://app.compux.ai/register) でサインアップし、APIキーを作成します。

### 2. 最初のリクエストを送信

```bash
curl https://api.compux.ai/v1/chat/completions \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4o",
    "messages": [{"role": "user", "content": "こんにちは！"}]
  }'
```

### 3. OpenAI互換SDKで使用

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

## 仕組み

```
AIスタートアップ              CompuX                      コンピュートプロバイダー
    |                           |                               |
    |-- コンピュートが必要 ----->|                               |
    |                           |-- 資金調達 ($1M) ------------>|
    |                           |<-- クレジット ($1.25-1.5M) ---|
    |<-- ブロック可能クレジット -|                               |
    |                           |                               |
    |-- APIリクエスト (OpenAI)->|-- 最適プロバイダーへルート --->|
    |<-- レスポンス ------------|<-- レスポンス ----------------|
```

**レイヤー5：トークンオペレーター** — CompuXはAIバリューチェーンのレイヤー5で運営し、インフラ（GPU）とアプリケーション（AI製品）の間に位置します。金融オペレーターのようにコンピュートクレジットの流れを最適化します。

## 主要コンセプト

| コンセプト | 説明 |
|-----------|------|
| **コンピュートクレジット** | プロバイダー間で標準化されたコンピュート単位 |
| **クレジットトランスフュージョン** | 資金調達を増幅されたコンピュートクレジットに変換 |
| **ブロック可能クレジット** | 担保として凍結/解凍可能なクレジット |
| **トークンオペレーター** | コンピュートクレジットの流れを管理するレイヤー5エンティティ |
| **マルチプロバイダールーティング** | リクエストごとに最適なプロバイダーを自動選択 |

[コンセプト](concepts/) セクションで詳しく読む。

## コミュニティとサポート

- [ウェブサイト](https://compux.ai) — CompuXについて
- [ナレッジベース](https://learn-compux.kossanstin.workers.dev) — 詳細記事とガイド
- [API Docs](https://docs.compux.ai) — APIリファレンス
- [Twitter](https://twitter.com/compux_ai) — アップデートとお知らせ
- [LinkedIn](https://www.linkedin.com/company/compux) — 企業ニュース
- [GitHub](https://github.com/CompuX-ai) — オープンソースプロジェクト
- [お問い合わせ](https://compux.ai/get-in-touch) — ご連絡ください

## コントリビュート

コントリビュートを歓迎します！ガイドラインは [CONTRIBUTING.md](CONTRIBUTING.md) をご覧ください。

## ライセンス

このプロジェクトはMITライセンスの下でライセンスされています — 詳細は [LICENSE](LICENSE) をご覧ください。