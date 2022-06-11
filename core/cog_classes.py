import discord
import json

class Cog_base(discord.Cog):
    
    def __init__(self, bot:discord.Bot):
        self.bot = bot
        with open("./data/config.json", mode="r", encoding="utf-8") as config_file:
            self.config:dict
            self.config = json.load(config_file)
        with open("./data/game.json", mode="r", encoding="utf-8") as game_file:
            self.game:dict
            self.game = json.load(game_file)
        self.guild_id = self.config["guild_id"]

class RoleButton(discord.ui.Button):
    def __init__(self, role: discord.Role, emoji= discord.Emoji):
        """
        A button for one role. `custom_id` is needed for persistent views.
        """
        super().__init__(
            label=role.name,
            style=discord.enums.ButtonStyle.primary,
            custom_id=str(role.id),
            emoji=emoji
        )

    async def callback(self, interaction: discord.Interaction):
        """This function will be called any time a user clicks on this button.

        Parameters
        ----------
        interaction : discord.Interaction
            The interaction object that was created when a user clicks on a button.
        """
        # Figure out who clicked the button.
        user = interaction.user
        # Get the role this button is for (stored in the custom ID).
        role = interaction.guild.get_role(int(self.custom_id))

        if role is None:
            # If the specified role does not exist, return nothing.
            # Error handling could be done here.
            return

        # Add the role and send a response to the user ephemerally (hidden to other users).
        if role not in user.roles:
            # Give the user the role if they don't already have it.
            await user.add_roles(role)
        else:
            await user.remove_roles(role)
