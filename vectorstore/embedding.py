from langchain_huggingface import HuggingFaceEmbeddings

def get_embedding_model(
        model_name: str = "BAAI/bge-m3"
) -> HuggingFaceEmbeddings:
    model_kwargs = {
        "device": "cuda"
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