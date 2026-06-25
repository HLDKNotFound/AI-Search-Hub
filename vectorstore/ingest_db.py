import os
from vectorstore import LanceDBManager
from langchain_community.document_loaders import PyPDFLoader

def ingest_db(
    pdf_file_path: str,
):
    db_manager = LanceDBManager()

    if not os.path.exists(pdf_file_path):
        raise FileNotFoundError(f"Not found: {pdf_file_path}")

    loader = PyPDFLoader(pdf_file_path)
    pages = loader.load()

    extracted_text = "\n".join([page.page_content for page in pages])

    db_manager.add_document(
        text_content=extracted_text,
        source_name=pdf_file_path,
        chunk_size=1000,
        chunk_overlap=200
    )