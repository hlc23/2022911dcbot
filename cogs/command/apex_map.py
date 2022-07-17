import discord
from core.cog_classes import Cog_base
from lib.map_checker import mapCheck

class apexMap(Cog_base):

    @discord.slash_command(name="apexmap", description ="show the apex map information")
    async def show_map(
        self,
        ctx:discord.ApplicationContext,
        mode:discord.Option(description="選擇模式", choices=[discord.OptionChoice(name="大逃殺", value="battle_royale"), discord.OptionChoice(name="大逃殺(積分)", value="ranked"), discord.OptionChoice(name="競技場", value="arenas"), discord.OptionChoice(name="競技場(積分)", value="arenasRanked"), discord.OptionChoice(name="控制", value="control")])
    ):
        r = mapCheck(mode)
        if r is None:
            embed = discord.Embed(colour=discord.Colour.red(), title="未知錯誤", description=f"請通知{self.bot.get_guild(self.guild_id).get_role(self.config['admin']).mention}")
            await ctx.respond(embed=embed)
            return
        
        embed = discord.Embed(colour=discord.Colour.green(), title=r["mode"])
        embed.add_field(name="當前地圖", value=r["currentMap"], inline=False)
        embed.add_field(name="時間", value=f"{r['startTime']} ~ {r['endTime']}", inline=False)
        embed.add_field(name="下一張地圖", value=r["nextMap"], inline=False)

        await ctx.respond(embed=embed)
        return



def setup(bot:discord.Bot):
    bot.add_cog(apexMap(bot))
