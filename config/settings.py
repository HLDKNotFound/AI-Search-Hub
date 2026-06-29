import torch

chart_path = "data/output"

EMBEDDING_MODEL = "BAAI/bge-m3"
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"