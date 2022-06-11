import discord
import json

class Cog_base(discord.Cog):
    
    def __init__(self, bot:discord.Bot):
        self.bot = bot
        with open("./data/config.json", mode="r", encoding="utf-8") as config_file:
            self.config = json.load(config_file)

