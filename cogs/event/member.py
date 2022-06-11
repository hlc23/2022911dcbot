from core.cog_classes import Cog_base
import discord

class Member(Cog_base):

    @discord.Cog.listener()
    async def on_member_join(self, member:discord.Member):
        embed = discord.Embed(colour=discord.Colour.random(), title=f"{member.name} 加入了!")
        embed.set_thumbnail(url=member.display_avatar.url)
        await self.bot.get_channel(self.config["boundary_channel"]).send(embed=embed)
    
    @discord.Cog.listener()
    async def on_member_remove(self, member:discord.Member):
        embed = discord.Embed(colour=discord.Colour.random(), title=f"喔不, {member.name} 離開了!")
        embed.set_thumbnail(url=member.display_avatar.url)
        await self.bot.get_channel(self.config["boundary_channel"]).send(embed=embed)

def setup(bot:discord.Bot):
    bot.add_cog(Member(bot))
