from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()
tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def web_search(query: str) -> str:
    results = tavily.search(
        query=query,
        max_results=6,
        search_depth="advanced"
    )
    output = []
    for r in results["results"]:
        output.append(
            f"Başlık: {r['title']}\n"
            f"URL: {r['url']}\n"
            f"İçerik: {r['content']}\n"
        )
    return "\n---\n".join(output)

def fetch_page(url: str) -> str:
    try:
        result = tavily.extract(urls=[url])
        content = result["results"][0]["raw_content"]
        return content[:4000]
    except Exception as e:
        return f"Sayfa okunamadı: {str(e)}"