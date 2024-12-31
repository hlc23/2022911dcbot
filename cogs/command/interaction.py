from random import choice, randint
import discord
from core.cog_classes import Cog_base

class Interaction(Cog_base):
    
    @Cog_base.command(name="family_mart", aliases=["fm"])
    async def family_mart(self, ctx: discord.ApplicationContext):
        await ctx.respond(f"{choice(["上", "下"])}{randint(1, 5)}{choice(["左", "右"])}{randint(1, 8)}")

    @Cog_base.command(name="dice", aliases=["roll"])
    async def dice(self, ctx: discord.ApplicationContext, sides: int = 6):
        await ctx.respond(f"{randint(1, sides)}")
