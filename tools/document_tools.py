from langchain_core.tools import tool

@tool
def lance_search(query: str) -> str:
    """
    Search relevant documents from LanceDB.

    Args:
        query (str): The search query.
    """
    return ""