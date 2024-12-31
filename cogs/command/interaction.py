from random import choice, randint
import discord
from core.cog_classes import Cog_base

class Interaction(Cog_base):
    
    @discord.slash_command(name="family_mart")
    async def family_mart(self, ctx: discord.ApplicationContext):
        await ctx.respond(f"{choice(['上', '下'])}{randint(1, 5)}{choice(['左', '右'])}{randint(1, 8)}")

    @discord.slash_command(name="dice", description="Roll a dice")
    async def dice(self, ctx: discord.ApplicationContext):
        await ctx.respond(f"{randint(1, 6)}")

def setup(bot: discord.Bot):
    bot.add_cog(Interaction(bot))
