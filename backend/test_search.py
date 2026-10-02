from app.tools.web_search import web_search


results = web_search(
    "latest developments in RAG systems"
)

for result in results["results"]:
    print(result["title"])
    print(result["url"])
    print()