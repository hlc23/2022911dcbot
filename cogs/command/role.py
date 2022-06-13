import discord
from discord.commands.core import slash_command
from discord.ext import commands
from core.cog_classes import Cog_base, RoleButton
import json

class ButtonRoleCog(Cog_base):
    """A cog with a slash command for posting the message with buttons
    and to initialize the view again when the bot is restarted.
    """

    with open("./data/config.json", mode="r", encoding="utf-8") as config_file:
        config = json.load(config_file)

    @slash_command(description="Post the button role message")
    @commands.has_any_role(config["admin"])
    async def update(self, ctx: commands.Context):
        """Slash command to post a new view with a button for each role."""

        # timeout is None because we want this view to be persistent.
        view = discord.ui.View(timeout=None)

        # # Loop through the list of roles and add a new button to the view for each role.
        # for role_id in self.game["all_game_role_id"]:
        #     # Get the role from the guild by ID.
        #     role = ctx.guild.get_role(role_id)
        #     view.add_item(RoleButton(role))

        embed = discord.Embed()
        embed.title = "點選按鈕獲得身分組"
        description = ""
        for game in self.game.keys():
            emoji = self.bot.get_emoji(self.game[game]["emoji"])
            description += f"{game}{emoji}\n"
            role = ctx.guild.get_role(self.game[game]["role"])
            view.add_item(RoleButton(role, emoji))
        embed.description = description
        embed.set_footer(text=f'請忽略"此交互失敗"')
        channel = self.bot.get_channel(self.config["get_role_channel"])
        new_message = await channel.fetch_message(self.config["get_role_message"])
        await new_message.edit(content=None,embed=embed, view=view)


def setup(bot):
    bot.add_cog(ButtonRoleCog(bot))
