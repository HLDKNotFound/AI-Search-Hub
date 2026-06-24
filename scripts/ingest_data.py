import os
from vectorstore import LanceDBManager

def ingest_paper(
    pdf_file_path: str,
    source_name: str
):
    db_manager = LanceDBManager()

    if not os.path.exists(pdf_file_path):
        raise FileNotFoundError(f"Not found: {pdf_file_path}")

    db_manager.add_document(
        text_content=pdf_file_path,
        source_name=source_name,
        chunk_size=1000,
        chunk_overlap=200
    )