import discord
from discord.ext import commands
from core.cog_classes import Cog_base, RoleButton
import json

class ButtonRoleCog(Cog_base):
    """A cog with a slash command for posting the message with buttons
    and to initialize the view again when the bot is restarted.
    """

    with open("./data/config.json", mode="r", encoding="utf-8") as config_file:
        config = json.load(config_file)

    @discord.slash_command(description = "Only for admin.")
    @commands.has_any_role(config["admin"])
    async def update(self, ctx: discord.ApplicationContext):
        try:
            view = discord.ui.View(timeout=None)
            embed = discord.Embed()
            embed.title = "點選按鈕獲得身分組"
            description = ""
            for game in self.game.keys():
                self.game[game]:dict
                if self.game[game].get("emoji") is not None:
                    try:
                        emoji = self.bot.get_emoji(self.game[game]["emoji"])
                        description += f"{game}{emoji}\n"
                    except:
                        description += f"{game}\n"
                else:
                    description += f"{game}\n"
                role = ctx.guild.get_role(self.game[game]["role"])
                view.add_item(RoleButton(role, emoji))
            embed.description = description
            embed.set_footer(text='出現"此交互失敗"請直接忽略')
            channel = self.bot.get_channel(self.config["get_role_channel"])
            new_message = await channel.fetch_message(self.config["get_role_message"])
            await new_message.edit(content=None,embed=embed, view=view)
        except commands.MissingAnyRole:
            await ctx.respond("你沒有權限使用此指令")


def setup(bot):
    bot.add_cog(ButtonRoleCog(bot))
