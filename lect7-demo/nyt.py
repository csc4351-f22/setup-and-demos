import requests

API_KEY = "Nice try! I deleted this, you'll have to get your own."

def get_headlines(query):
    response = requests.get(
        "https://api.nytimes.com/svc/search/v2/articlesearch.json",
        params={"q": query, "api-key": API_KEY},
    )

    response_json = response.json()
    headlines = []
    for doc in response_json["response"]["docs"]:
        headlines.append(doc["headline"]["main"])
    return headlines