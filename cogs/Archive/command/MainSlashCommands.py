import json
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option

with open ("./json/config.json", 'r', encoding="utf8") as config:
    config = json.load(config)

class MainSlashCommands(commands.Cog):
    def __init__(self, Anna):
        self.Anna = Anna
    @cog_ext.cog_slash(name = "cls",
                       description = "指定欲刪除訊息的數量",
                       guild_ids = config['guild_ids'],
                       options = [
                           create_option(
                               name = "amount",
                               description = "訊息數量",
                               option_type = 4,
                               required = True
                           )
                       ])
    async def cls(self, ctx:SlashContext, amount:int):
        server = self.Anna.get_guild(ctx.guild_id)
        member = server.get_member(ctx.author_id)
        if (member.guild_permissions.manage_channels == True):
            await ctx.channel.purge(limit = amount)
            await ctx.send(content = f"成功刪除 **{amount}** 則訊息", hidden = True)
        else:
            await ctx.send(content = "權限不足", hidden = True)

    @cog_ext.cog_slash(name = "ping",
                       description = "回傳機器人的延遲時間",
                       guild_ids = config['guild_ids'])
    async def ping(self, ctx):
        if (round(self.Anna.latency*1000) >= 100):
            await ctx.send(f'你與我的距離為 {round(self.Anna.latency*1000)} 毫秒\n有夠遠的')
        else:
            await ctx.send(f'你與我的距離為 {round(self.Anna.latency*1000)} 毫秒')

def setup(Anna):
    Anna.add_cog(MainSlashCommands(Anna))