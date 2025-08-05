
import feedparser

def search_arxiv(topic):
    url = f"http://export.arxiv.org/api/query?search_query=all:{topic}&start=0&max_results=5"
    feed = feedparser.parse(url)
    results = []
    for entry in feed.entries:
        results.append({
            'title': entry.title,
            'summary': entry.summary,
            'url': entry.link
        })
    return results
