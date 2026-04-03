/**
 * CompuX TypeScript Quickstart — Drop-in OpenAI replacement.
 *
 * Install: npm install openai
 * Run:     COMPUX_API_KEY=cpx_live_... npx tsx quickstart.ts
 */

import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.COMPUX_API_KEY,
  baseURL: "https://api.compux.ai/v1",
});

// Basic chat completion
async function chat(message: string): Promise<string> {
  const response = await client.chat.completions.create({
    model: "gpt-4o",
    messages: [{ role: "user", content: message }],
  });
  return response.choices[0].message.content ?? "";
}

// Streaming
async function streamChat(message: string): Promise<void> {
  const stream = await client.chat.completions.create({
    model: "gpt-4o",
    messages: [{ role: "user", content: message }],
    stream: true,
  });

  for await (const chunk of stream) {
    const content = chunk.choices[0]?.delta?.content;
    if (content) process.stdout.write(content);
  }
  console.log();
}

// Multi-model comparison
async function compareModels(prompt: string): Promise<void> {
  const models = ["gpt-4o-mini", "claude-sonnet-4-20250514", "gemini-2.5-flash"];

  const results = await Promise.all(
    models.map(async (model) => {
      const start = Date.now();
      const response = await client.chat.completions.create({
        model,
        messages: [{ role: "user", content: prompt }],
        max_tokens: 100,
      });
      return {
        model,
        latency: Date.now() - start,
        tokens: response.usage?.total_tokens ?? 0,
        preview: response.choices[0].message.content?.slice(0, 80) ?? "",
      };
    })
  );

  console.log("\nModel Comparison:");
  for (const r of results) {
    console.log(`  ${r.model}: ${r.latency}ms, ${r.tokens} tokens — "${r.preview}..."`);
  }
}

async function main() {
  // Basic request
  const answer = await chat("What is a compute credit marketplace?");
  console.log("Answer:", answer);

  // Streaming
  console.log("\nStreaming:");
  await streamChat("Explain AI compute financing in 2 sentences.");

  // Compare models
  await compareModels("What is CompuX?");
}

main().catch(console.error);