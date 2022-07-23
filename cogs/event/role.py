import discord
from core.cog_classes import Cog_base, RoleButton

class Role(Cog_base):

    @discord.Cog.listener()
    async def on_ready(self):
        """This method is called every time the bot restarts.
        If a view was already created before (with the same custom IDs for buttons)
        it will be loaded and the bot will start watching for button clicks again.
        """
        # We recreate the view as we did in the /post command.
        view = discord.ui.View(timeout=None)
        # Make sure to set the guild ID here to whatever server you want the buttons in!
        guild = self.bot.get_guild(self.guild_id)
        for game in self.game.keys():
            role_id = self.game[game]["role"]
            role = guild.get_role(role_id)
            emoji = self.bot.get_emoji(self.game[game].get("emoji"))
            view.add_item(RoleButton(role, emoji))
            del emoji

        # Add the view to the bot so it will watch for button interactions.
        self.bot.add_view(view)


def setup(bot:discord.Bot):
    bot.add_cog(Role(bot))
