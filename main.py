import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from lib import load_config, get_cogs


load_dotenv()
TOKEN = os.getenv("TOKEN")
config = load_config()
cogs = get_cogs()
bot = discord.Bot(debug_guilds=[985045688377282581], intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("="*15)
    print(f"{bot.user} is ready and online!")
    print("="*15)
    return

@bot.slash_command(name = "reload", description = "Reload cog")
@commands.has_any_role(config["admin"])
async def reload(ctx:discord.ApplicationContext):
    try:
        load_config()
        get_cogs()
        for cog in cogs:
            try:
                bot.reload_extension(f"cogs.{cog}")
            except:
                bot.load_extension(f"cogs.{cog}")
    except:
        await ctx.respond("Error")
    else:
        await ctx.respond("Reload complete")
    return

@bot.slash_command(name = "unload", description = "Unload cog")
@commands.has_any_role(config["admin"])
async def unload(ctx:discord.ApplicationContext, cog: discord.Option(str, description="Cog name")):
    try:
        bot.unload_extension(f"cogs.{cog}")
    except:
        await ctx.respond("Error", ephemeral=True)
    else:
        await ctx.respond("Unload complete", ephemeral=True)
    return

for cog in cogs:
    bot.load_extension(f"cogs.{cog}")

try:
    bot.run(TOKEN)
except:
    os.system("kill 1")
