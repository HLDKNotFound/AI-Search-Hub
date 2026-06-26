import os
from langchain_openai import ChatOpenAI

def get_llm(
    model_name: str = "google/gemini-2.5-flash", 
    temperature: float = 0,
    max_tokens: int = 3000
):
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        return "ERROR: OPENROUTER_API_KEY environment variable is not configured."

    return ChatOpenAI(
        model=model_name,
        api_key=api_key,
        base_url="https://openrouter.ai/api/v1",
        temperature=temperature,
        max_tokens=max_tokens
    )

from .manager_agent import manager_agent_node
from .paper_agent import paper_agent_node
from .web_agent import web_agent_node
from .visual_agent import visual_agent_node
from .writer_agent import writer_agent_node
from .critic_agent import critic_agent_node

__all__ = [
    "manager_agent_node",
    "paper_agent_node",
    "web_agent_node",
    "visual_agent_node",
    "writer_agent_node",
    "critic_agent_node"
]