import discord
from core.cog_class import Cog_base

class Basic(Cog_base):

    @discord.slash_command(name = "Hello", description = "Say hello to the bot")
    async def hello(self, ctx:discord.ApplicationContext):
        await ctx.respond(f"Hi {ctx.author.mention}")

    @discord.slash_command(name="Ping", description = "Ping the bot.")
    async def ping(self, ctx:discord.ApplicationContext):
        await ctx.respond(f"{round(self.bot.latency*1000)} ms")

def setup(bot:discord.Bot):
    bot.add_cog(Basic(bot))
