import json

def load_config():
    with open("./data/config.json", mode="r", encoding="utf-8") as config_file:
        config = json.load(config_file)
    return config

def get_cogs():
    with open("./data/cogs.json", mode="r", encoding="utf-8") as cogs_file:
        cogs = json.load(cogs_file)["cogs"]
    return cogs