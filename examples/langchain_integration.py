"""CompuX + LangChain — Use CompuX as the LLM backend for LangChain applications."""

import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

# CompuX works as a drop-in for any LangChain OpenAI integration
llm = ChatOpenAI(
    model="gpt-4o",
    api_key=os.environ["COMPUX_API_KEY"],
    base_url="https://api.compux.ai/v1",
    temperature=0.7,
)

# Basic invocation
response = llm.invoke([
    SystemMessage(content="You are an AI compute cost advisor."),
    HumanMessage(content="I spend $5,000/month on OpenAI. How can CompuX help?"),
])
print(response.content)

# Streaming
print("\n--- Streaming ---")
for chunk in llm.stream([HumanMessage(content="What are blockable credits?")]):
    print(chunk.content, end="", flush=True)
print()

# Batch processing
print("\n--- Batch ---")
questions = [
    [HumanMessage(content="What is a token operator?")],
    [HumanMessage(content="How does compute credit financing work?")],
    [HumanMessage(content="What is LLM routing?")],
]
results = llm.batch(questions)
for q, r in zip(questions, results):
    print(f"Q: {q[0].content}")
    print(f"A: {r.content[:100]}...\n")