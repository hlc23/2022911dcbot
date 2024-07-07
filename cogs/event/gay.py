import discord
from core.cog_classes import Cog_base

class GayCog(Cog_base):

    @discord.Cog.listener()
    async def on_member_update(self, before: discord.Member, after: discord.Member):
        if after.id == 417215201423917078 and after.nick != "南同":
            await after.edit(nick="南同")
        return

    @discord.Cog.listener()
    async def on_ready(self):
        if gay := self.bot.get_guild(417215201423917078).get_member(417215201423917078):
            if gay.nick != "南同":
                await gay.edit(nick="南同")


def setup(bot):
    bot.add_cog(GayCog(bot))
