import discord
import json
import random
import datetime
from discord.ext import commands

with open (r"C:\Users\George Rupp\Desktop\Files\Programming\Github\Suspend-bot\json\MainCommands.json", 'r', encoding="utf8") as MainCommandsJson:
    MainCommandsJson = json.load(MainCommandsJson)

class MainCommands(commands.Cog):
    def __init__(self, Misaki):
        self.Misaki = Misaki

    @commands.command()
    async def help_main(self, ctx):
        embed = discord.Embed(title = "主要指令清單", description = None, colour = 0x93e2df
        , timestamp = datetime.datetime.utcnow())
        embed.add_field(name = "> 與我的延遲", value = "**@青羽美咲 ping**", inline = False)
        embed.add_field(name = "> 刪除數量訊息", value = "**@青羽美咲 purge [數量]**", inline = False)
        embed.add_field(name = "> 匿名訊息", value = "**@青羽美咲 botsaid [訊息]**", inline = False)
        embed.add_field(name = "> 隨機組隊", value = "**@青羽美咲 rds [關鍵字] [每組幾人] [隊伍數]**", inline = False)
        await ctx.send(embed=embed)

    @commands.command()
    async def ping(self, ctx):
        if (round(self.Misaki.latency*1000) >= 100):
            await ctx.send(f'你與我的距離為 {round(self.Misaki.latency*1000)} 毫秒\n有夠遠的')
        else:
            await ctx.send(f'你與我的距離為 {round(self.Misaki.latency*1000)} 毫秒')

    @commands.command()
    async def purge(self, ctx, amount=1):
        await ctx.channel.purge(limit=amount+1)

    @commands.command()
    async def cls(self, ctx, amount=1):
        await ctx.channel.purge(limit=amount+1)

    @commands.command()
    async def botsaid(self, ctx, *,message):
        await ctx.message.delete()
        await ctx.send(message)
    
    @commands.command()
    async def rds(self, ctx, keyword:str, population:int, groups:int):
        hasNick = []
        for member in ctx.guild.members:
            if member.nick != None and member.nick.count(keyword):
                hasNick.append(member.name)
        if (len(hasNick) <= population * groups):
            await ctx.channel.send(f'不足以分組。\n請確定人數是否足夠、關鍵字 "{keyword}" 是否更改為暱稱之內。')
            pass
        else:
            for iteration in range(groups):
                enum = random.sample(hasNick, k=population)
                for removal in enum:
                    hasNick.remove(removal)
                embed = discord.Embed(title = f'第 {iteration+1} 小隊', description = None, colour = 0x93e2df
                , timestamp = datetime.datetime.utcnow())
                embed.set_thumbnail(url = MainCommandsJson['Flag_icon'])
                embed.add_field(name = "隊員", value=f'{enum}', inline=False)
                await ctx.send(embed=embed)

def setup(Misaki):
    Misaki.add_cog(MainCommands(Misaki))