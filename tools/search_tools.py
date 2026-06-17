import os
from langchain_core.tools import tool
from tavily import TavilyClient

@tool
def tavily_search(
    query: str, 
    max_results: int = 3, 
    search_depth: str = "advanced"
):
    """
    Use this tool to search the internet ffro the latest information, benchmark metrics, news,
    or API updates.

    Args:
        query (str): The search query.
        max_results (int): The maximum number of search results to return (default: 3).
        search_depth (str): The depth of the search ("basic" or "advanced").
    """

    api_key = os.getenv("TAVILY_API_KEY")
    if not api_key:
        return "ERROR: TAVILY_API_KEY environment variable is not configured."
    
    tavily_client = TavilyClient(api_key = api_key)

    try:
        # Call the Tavily Search API
        response = tavily_client(
            query=query,
            search_depth=search_depth,
            max_results=max_results,
            include_answer=True,            # Tavily generates an AI summary answer
            include_raw_content=False       # Keep False to avoid exceeding the LLM's context window limit
        )

        # Extract the AI-generated answer directly from Tavily
        tavily_answer = response.get("answer", "")

        # Extract and format the detailed search results
        results = response.get("results", [])
        formatted_results = []

        for idx, r in enumerate(results, 1):
            formatted_results.append(
                f"Source [{idx}]: {r.get('title')}\n"
                f"URL: {r.get('url')}\n"
                f"Content: {r.get('content')}"
            )

        # Aggregate into a single string to return to the State
        final_output = f"[TAVILy At SUMMARY]:\n{tavily_answer}\n\n"
        final_output += "[DETAILED SEARCH RESULTS]:\n" + "\n---\n".join(formatted_results)

        return final_output
    
    except Exception as e:
        return f"TAVILY SEARCH ERROR: {str(e)}"