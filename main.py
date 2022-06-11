from discord.ext import commands
import discord
import os
from dotenv import load_dotenv
import json

load_dotenv()
bot = discord.Bot(debug_guilds=[985045688377282581])

@bot.event
async def on_ready():
    print("="*15)
    print(f"{bot.user} is ready and online!")
    print("="*15)



with open("./data/cogs.json", mode="r", encoding="utf-8") as cogs_file:
    cogs = json.load(cogs_file)["cogs"]

for cog in cogs:
    bot.load_extension(f"cogs.{cog}")
    print(f"load {cog}")


bot.run(os.getenv('TOKEN'))