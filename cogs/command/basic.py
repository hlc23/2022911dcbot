import discord
from core.cog_classes import Cog_base

class Basic(Cog_base):

    @discord.slash_command(name = "hello", description = "Say hello to the bot")
    async def hello(self, ctx:discord.ApplicationContext):
        await ctx.respond(f"Hi {ctx.author.mention}")
        return

    @discord.slash_command(name="ping", description = "Ping the bot.")
    async def ping(self, ctx:discord.ApplicationContext):
        await ctx.respond(f"{round(self.bot.latency*1000)} ms")
        return


def setup(bot:discord.Bot):
    bot.add_cog(Basic(bot))
