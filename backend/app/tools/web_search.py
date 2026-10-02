from tavily import TavilyClient
from app.config import settings
tavily_client = TavilyClient(
    api_key=settings.tavily_api_key
)
def web_search(query:str):
    return tavily_client.search(
        query=query,
        max_result=6
    )