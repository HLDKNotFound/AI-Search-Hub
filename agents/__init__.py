import os
from langchain_openai import ChatOpenAI

def get_llm(model_name: str = "google/gemini-2.5-flash", temperature: float = 0):
    api_key = os.getenv("OPENROUTER_API_KEY")

    return ChatOpenAI(
        model=model_name,
        api_key=api_key,
        base_url="https://openrouter.ai/api/v1",
        temperature=temperature
    )