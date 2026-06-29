import os
import lancedb
import pyarrow as pa

from vectorstore.embedding import get_embedding_model
from langchain_text_splitters import RecursiveCharacterTextSplitter

from config import DEVICE

def create_schema(vector_dim: int) -> pa.schema:
    return pa.schema([
        pa.field("vector", pa.list_(pa.float32(), vector_dim)),
        pa.field("text", pa.string()),
        pa.field("source_file", pa.string()),
        pa.field("chunk_index", pa.int16())
    ])

class LanceDBManager:
    def __init__(
        self,
        db_path: str = "data/vector_db/lancedb",
        table_name: str = "research_papers"
    ):
        self.db_path = db_path
        self.table_name = table_name
        self.embed_model = get_embedding_model()

        vector = self.embed_model.embed_query("test")
        self.vector_dim = len(vector)

        schema = create_schema(self.vector_dim)

        os.makedirs(self.db_path, exist_ok=True)

        self.db = lancedb.connect(self.db_path)

        if self.table_name not in self.db.table_names():
            self.table = self.db.create_table(
                self.table_name,
                schema=schema
            )
        else:
            self.table = self.db.open_table(
                self.table_name
            )

    def add_document(
        self,
        text_content: str,
        source_name: str,
        chunk_size: int = 1000,
        chunk_overlap: int = 200
    ):
        separators = [
            "\n\n",
            "\n",
            ".",
            " "
        ]

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=separators
        )

        chunks = splitter.split_text(text_content)
        if not chunks:
            return
        print(f"Chunk length: {len(chunks)} from {source_name}")

        embeddings = self.embed_model.embed_documents(chunks)

        data_to_insert = [
            {
                "vector": emb,
                "text": chunk,
                "source_file": source_name,
                "chunk_index": idx
            }
            for idx, (chunk, emb) in enumerate(zip(chunks, embeddings))
        ]

        self.table.add(data_to_insert)
        """self.table.create_index(
            num_partitions=self.vector_dim // 4,
            num_sub_vectors=self.vector_dim // 8,
            accelerator=DEVICE
        )"""
        print(f"Store data from {source_name} to LanceDB")

    def similarity_search(self, query: str, top_k: int = 5) -> str:
        query_vector = self.embed_model.embed_query(query)

        results = (
            self.table.search(query_vector)
            .limit(top_k)
            .to_list()
        )

        if not results:
            return "No related documents."
        
        context_parts = []
        for res in results:
            context = f"""[Source {res['source_file']}] - Chunk {res['chunk_index']}
            {res['text']}
            """
            context_parts.append(context)

        return "\n\n---\n\n".join(context_parts)