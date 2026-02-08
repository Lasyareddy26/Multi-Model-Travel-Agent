import os
from langchain_community.tools.tavily_search import TavilySearchResults

def search_travel(query: str):
    """Searches for flights, hotels, and attractions."""
    search = TavilySearchResults(api_key=os.getenv("TAVILY_API_KEY"), max_results=5)
    return search.invoke({"query": query})