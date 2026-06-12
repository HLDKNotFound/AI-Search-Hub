import os
from langchain_google_genai import ChatGoogleGenerativeAI

def get_llm(model_name: str = "gemini-2.5-flash", temperature: float = 0):
    return ChatGoogleGenerativeAI(
        model=model_name,
        temperature=temperature
    )