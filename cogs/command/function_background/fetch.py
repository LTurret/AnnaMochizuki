import json

from requests_oauthlib import OAuth1Session


def fetch(secrets: list) -> None:
    
    api = "https://api.twitter.com/2/tweets/search/recent"
    
    payload = {
        "query": "from:imasml_theater",
        "tweet.fields": ["entities"],
        "max_results": 11
    }

    oauth = OAuth1Session(
        secrets[0],
        client_secret = secrets[1],
        resource_owner_key = secrets[2],
        resource_owner_secret = secrets[3]
    )

    response = oauth.get(api, params=payload)
    print(f"OAuth response: {response.status_code}")

    tweets = json.loads(response.text)

    with open("./cogs/command/function_background/data.json", mode="w", encoding="utf-8") as data:
        json.dump(tweets, data, ensure_ascii=False, indent=4)