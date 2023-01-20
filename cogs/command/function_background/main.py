import json
import os
import time

from fetch import fetch
from push import notify_push
from auth import secrets


secrets = secrets()

def template(url: str, keywords: list=[], hashtags: list=[]) -> str:

    current_time = f"<t:{int(time.time())}>"
    content = f"━《　✨ 美咲發推啦 ✨　》━\n\n> {current_time}\n> {url}"
    content += "\n"

    if len(keywords) > 0:
        additional = f"\n關鍵字："
        for keyword in keywords:
            additional += f"{keyword}、"
        content += additional
        content = content[:-1]

    if len(hashtags) > 0:
        additional = f"\n"
        for hashtag in hashtags:
            additional += f"{hashtag} "
        content += additional
        content = content[:-1]

    content += f"\n￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣"

    return content


def get_keywords(webhook_data: list) -> list:
    keywords = []
    if "annotations" in webhook_data["entities"]:
        for annotation in webhook_data["entities"]["annotations"]:
            keywords.append(f'`{annotation["normalized_text"]}`')
    return keywords


def get_hashtags(webhook_data: list) -> list:
    hashtags = []
    if "hashtags" in webhook_data["entities"]:
        for hashtag in webhook_data["entities"]["hashtags"]:
            hashtags.append(f'`#{hashtag["tag"]}`')
    return hashtags


def main() -> str:
    
    fetch(secrets)

    with open("data.json", "r", encoding="utf-8") as webhook_data:
        webhook_data = json.load(webhook_data)
        if "errors" in webhook_data:
            return "API Errors, process could not resolve"

    if "last_id.json" not in os.listdir():
        with open("last_id.json", mode="w") as last_id:
            json.dump({"id": webhook_data["meta"]["newest_id"]}, last_id)
    else:
        with open("./last_id.json", mode="r") as last_id:
            last_id = json.load(last_id)["id"]

    cluster = [0, []]
    for data in webhook_data["data"]:
        if data["id"] != last_id:
            cluster[0] += 1
            cluster[1].append(data)
        else:
            break
    print(f"{cluster[0]} tweets in queue")

    prefix = "https://twitter.com/imasml_theater/status/"

    for _ in range(cluster[0]):
        data = cluster[1].pop()
        suffix = data["id"]
        url = prefix + suffix
        keywords = get_keywords(data)
        hashtags = get_hashtags(data)
        notify_push(template(url, keywords, hashtags))
    return "completed"


result = main()
print(result)