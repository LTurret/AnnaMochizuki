import discord
import datetime
from discord.ext import commands

class helplist(commands.Cog):
    def __init__(self, Misaki):
        self.Misaki = Misaki

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title = "MLTD指令清單", description = None, colour = 0x93e2df, timestamp = datetime.datetime.utcnow())
        embed.add_field(name = "> 主要指令清單", value = "**@青羽美咲 help_main**", inline = False)
        embed.add_field(name = "> MLTD指令清單", value = "**@青羽美咲 help_mltd**", inline = False)
        await ctx.send(embed=embed)

    @commands.command()
    async def help_mltd(self, ctx):
        embed = discord.Embed(title = "MLTD指令清單", description = None, colour = 0x93e2df, timestamp = datetime.datetime.utcnow())
        embed.add_field(name = "> 歌單", value = "**@青羽美咲 歌單**", inline = False)
        embed.add_field(name = "> 轉蛋模擬器", value = "**/轉蛋 [轉出次數]**", inline = False)
        embed.add_field(name = "> 轉蛋機率", value = "**@青羽美咲 轉蛋機率**", inline = False)
        await ctx.send(embed=embed)

    @commands.command()
    async def help_main(self, ctx):
        embed = discord.Embed(title = "主要指令清單", description = None, colour = 0x93e2df, timestamp = datetime.datetime.utcnow())
        embed.add_field(name = "> 與我的延遲", value = "**/ping**", inline = False)
        embed.add_field(name = "> 刪除數量訊息", value = "**/cls [數量]** *權限限制*", inline = False)
        embed.add_field(name = "> 匿名訊息", value = "**@青羽美咲 botsaid [訊息]**", inline = False)
        embed.add_field(name = "> 隨機組隊", value = "**@青羽美咲 rds [關鍵字] [每組幾人] [隊伍數]**", inline = False)
        await ctx.send(embed=embed)

    @commands.command()
    async def help_other(self, ctx):
        embed = discord.Embed(title = "主要指令清單", description = None, colour = 0x93e2df, timestamp = datetime.datetime.utcnow())
        embed.add_field(name = "> 乘法公式", value = "**@青羽美咲 乘法公式**", inline = False)
        await ctx.send(embed=embed)

def setup(Misaki):
    Misaki.add_cog(helplist(Misaki))