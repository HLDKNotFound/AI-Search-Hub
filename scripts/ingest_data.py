import os
from tools.document_tools import DocumentExtractor
from vectorstore import LanceDBManager

def ingest_paper(
    pdf_file_path: str,
    source_name: str
):
    db_manager = LanceDBManager()

    if not os.path.exists(pdf_file_path):
        raise FileNotFoundError(f"Not found: {pdf_file_path}")
    
    extractor = DocumentExtractor(file_path=pdf_file_path)
    document_content = extractor.process_document()

    db_manager.add_document(
        text_content=document_content,
        source_name=source_name,
        chunk_size=1000,
        chunk_overlap=200
    )

if __name__ == "__main__":
    sample_pdf = "data/input/Summary.pdf"
    ingest_paper(sample_pdf, "Pdf_file")