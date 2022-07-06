import discord
from discord.ext import commands
from core.cog_classes import Cog_base
import json

class Game(Cog_base):

    with open("./data/config.json", mode="r", encoding="utf-8") as config_file:
        config = json.load(config_file)

    @discord.slash_command(name="game", description = "Create new game.")
    @commands.has_any_role(config["admin"])
    async def new_game(
        self,
        ctx: discord.ApplicationContext,
        game_name: discord.Option(str, description="New game's name."),
        role_color: discord.Option(str, description="Role color code", default=discord.Colour.random()),
        emoji: discord.Option(discord.Emoji, description="Emoji for game icon", default=None)
    ):
        with open("data/game.json", mode="r", encoding="utf-8") as game_file:
            game_config = json.load(game_file)
            game_config:dict
        if game_name in game_config.keys():
            await ctx.respond("This game has already exists.", )
            return
        guild =  self.bot.get_guild(self.guild_id)
        game_role = await guild.create_role(name=game_name, colour=role_color)
        bot_role = guild.get_role(self.config["bot_role"])
        overwrite = {
            guild.default_role:discord.PermissionOverwrite(
                view_channel=False,
                connect=False),
            game_role:discord.PermissionOverwrite(
                view_channel=True,
                connect=True),
            bot_role:discord.PermissionOverwrite(
                view_channel=False,
                connect=False)
        }
        game_category = await guild.create_category(name=game_name, overwrites=overwrite, position=len(guild.categories)-2)
        game_chat = await game_category.create_text_channel(name="聊天區")
        game_voice = await game_category.create_voice_channel(name="動態語音")
        if emoji is not None:
            self.game[game_name] = {
                "role":game_role.id,
                "emoji":emoji.id,
                "chat":game_chat.id,
                "voice":game_voice.id
            }
        else:
            self.game[game_name] = {
                "role":game_role.id,
                "chat":game_chat.id,
                "voice":game_voice.id
            }
        with open("./data/game.json", mode="w", encoding="utf-8") as wjson:
            json.dump(self.game, wjson, indent=4, ensure_ascii=True)
        await ctx.respond("創建成功")

def setup(bot:discord.Bot):
    bot.add_cog(Game(bot))
