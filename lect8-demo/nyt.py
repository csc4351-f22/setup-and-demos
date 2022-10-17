import requests
from dotenv import find_dotenv, load_dotenv
# pip3 install python-dotenv
import os

load_dotenv(find_dotenv())
API_KEY = os.getenv("API_KEY")

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