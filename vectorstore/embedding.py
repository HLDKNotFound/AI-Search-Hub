from langchain_huggingface import HuggingFaceEmbeddings
from functools import lru_cache

from config import DEVICE, EMBEDDING_MODEL

@lru_cache(maxsize=1)
def get_embedding_model(model_name: str = EMBEDDING_MODEL) -> HuggingFaceEmbeddings:
    model_kwargs = {
        "device": DEVICE
    }
    encode_kwargs = {
        "normalize_embeddings": True
    }

    embed_model = HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs
    )
    
    return embed_model