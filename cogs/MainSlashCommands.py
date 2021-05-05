import discord
import json
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option

with open (r"C:\Users\a0919\Desktop\Files\Programming\Github\Suspend-bot\json\setting.json", 'r', encoding="utf8") as GlobalSetting:
    GlobalSetting = json.load(GlobalSetting)

class MainSlashCommands(commands.Cog):
    def __init__(self, Misaki):
        self.Misaki = Misaki

    # @cog_ext.cog_slash(name = "ouen",
    #             description = '使用指令後打上"応援するよ！"來為杏奈應援！！',
    #             guild_ids = GlobalSetting['guild_ids'])
    # async def ouen(self, ctx):
    #     await ctx.send(content = f"(＊>△<)＜応援ください！")

    @cog_ext.cog_slash(name = "cls",
                       description = "指定欲刪除訊息的數量",
                       guild_ids = GlobalSetting['guild_ids'],
                       options = [
                           create_option(
                               name = "amount",
                               description = "訊息數量",
                               option_type = 4,
                               required = True
                           )
                       ])
    async def cls(self, ctx, amount:int):
        await ctx.channel.purge(limit = amount)
        await ctx.send(content = f"您已成功刪除 **{amount}** 則訊息", hidden = True)

def setup(Misaki):
    Misaki.add_cog(MainSlashCommands(Misaki))