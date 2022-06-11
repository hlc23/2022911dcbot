import discord
import os # default module
from dotenv import load_dotenv

load_dotenv() # load all the variables from the env file
bot = discord.Bot(debug_guilds=[985045688377282581])

@bot.event
async def on_ready():
    print("="*15)
    print(f"{bot.user} is ready and online!")
    print("="*15)

@bot.slash_command(name = "hello", description = "Say hello to the bot")
async def hello(ctx:discord.ApplicationContext):
    await ctx.respond(f"Hi {ctx.author.mention}")

bot.run(os.getenv('TOKEN')) # run the bot with the token