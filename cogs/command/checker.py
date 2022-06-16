import discord
from core.cog_classes import Cog_base
from lib.server_check import server_check

class Checker(Cog_base):


    @discord.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.content.startswith("!check"):
            message_content = message.content
            ip = message_content.replace("!check ", "")
            check = server_check(ip)
            print(check)
            if check is None:
                embed = discord.Embed(title="伺服器檢查", description=ip, colour=discord.Colour.red())
                embed.add_field(name="狀態", value="未找到")
                embed.set_footer(text=message.author.display_name, icon_url=message.author.display_avatar.url)
                await message.channel.send(embed=embed)
                return
            if check == "Server is offline":
                embed = discord.Embed(title="伺服器檢查", description=ip, colour=discord.Colour.dark_blue())
                embed.add_field(name="狀態", value="離線")
                embed.set_footer(text=message.author.display_name, icon_url=message.author.display_avatar.url)
                await message.channel.send(embed=embed)
                return
            
            embed = discord.Embed(title="伺服器檢查", description=ip, colour=discord.Colour.green())
            embed.add_field(name="狀態", value="上線中")
            embed.set_footer(text=message.author.display_name, icon_url=message.author.display_avatar.url)
            embed.add_field(name="版本", value=check.get("Version"), inline=True)
            embed.add_field(name="當前玩家數", value=check.get("NoP"))
            if check.get("Players") != []:
                text = ""
                for p in check.get("Players"):
                    text += f"{p}\n"
                embed.add_field(name="玩家", value=text)
            await message.channel.send(embed=embed)
            return

def setup(bot:discord.Bot):
    bot.add_cog(Checker(bot))
