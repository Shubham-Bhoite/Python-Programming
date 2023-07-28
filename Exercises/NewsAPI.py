#Use the NewsAPI and the requests module to fetch the daily news related to different topics

import requests
import json

while True:
    query = input("What type of news you want to hear(enter 0 to exit) : ")
    if query == "0":
        break
    url = f"https://newsapi.org/v2/everything?q={query}&from=2023-04-02&sortBy=publishedAt&apiKey=1bfa2c3570f74297a6e3c58a5bf92d65"
    r = requests.get(url)
    news = json.loads(r.text)
    
    if 'articles' in news:
        for article in news["articles"]:
            print("------------------")
            print(article["title"])
            print(article["description"])
            print("-------------------")
            
    else:
        print("No articles found for your query. Please try again.!")