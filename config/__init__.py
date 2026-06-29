from .prompts import(
    manager_prompt,
    paper_prompt,
    web_prompt,
    visual_prompt,
    writer_prompt,
    critic_prompt
)

from .settings import (
    DEVICE,
    EMBEDDING_MODEL
)

__all__ = [
    "manager_prompt",
    "paper_prompt",
    "web_prompt",
    "visual_prompt",
    "writer_prompt",
    "critic_prompt",

    "DEVICE",
    "EMBEDDING_MODEL"
]