from langchain_huggingface import HuggingFaceEmbeddings

def get_embedding_model() -> HuggingFaceEmbeddings:
    model_name = "BAAI/bg-small-en-v1.5"
    model_kwargs = {
        "device": "cuda"
    }
    encode_kwargs = {
        "normalize_embeddings": True
    }

    return HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs
    )