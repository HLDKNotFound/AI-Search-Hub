from langchain_core.tools import tool
from vectorstore import LanceDBManager

db_manager = LanceDBManager()

@tool
def lance_search(query: str) -> str:
    """
    Search relevant documents from LanceDB.

    Args:
        query (str): The search query.
    """
    
    try:
        results = db_manager.similarity_search(
            query=query,
            top_k=5
        )

        return results
    
    except Exception as e:
        return f"LANCEDB SEARCH ERROR: {str(e)}"