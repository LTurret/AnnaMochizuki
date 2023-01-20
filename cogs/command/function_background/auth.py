import json

def secrets() -> list:
    with open("./cogs/command/function_background/secret.json", "r") as secret:
        secret = json.load(secret)
        CONSUMER_KEY = secret["CONSUMER_KEY"]
        CONSUMER_KEY_SECRET = secret["CONSUMER_KEY_SECRET"]
        ACCESS_TOKEN = secret["ACCESS_TOKEN"]
        ACCESS_TOKEN_SECRET = secret["ACCESS_TOKEN_SECRET"]
        WEBHOOK_URL = secret["WEBHOOK_URL"]
    secrets = [CONSUMER_KEY, CONSUMER_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, WEBHOOK_URL]
    return secrets