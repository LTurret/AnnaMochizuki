import discord
import json
import random
import datetime
from discord.ext import commands

with open (r"C:\Users\George Rupp\Desktop\Files\Programming\Github\Suspend-bot\json\MLTD.json", 'r', encoding='utf8') as MLTDjson:
    Mjson = json.load(MLTDjson)

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
    async def rds(self, ctx, keyword:str, sampling1:int, sampling2:int):
        hasNick = []
        for member in ctx.guild.members:
            if member.nick != None and member.nick.count(keyword):
                hasNick.append(member.name)
        for iteration in range(sampling2):
            enum = random.sample(hasNick, k=sampling1)
            for removal in enum:
                hasNick.remove(removal)
            embed = discord.Embed(title = f'第 {iteration+1} 小隊', description = None, colour = 0x93e2df
            , timestamp = datetime.datetime.utcnow())
            embed.set_thumbnail(url = 'https://icons.iconarchive.com/icons/paomedia/small-n-flat/1024/flag-icon.png') #TO JSON TO JSON TO JSON
            embed.add_field(name = "隊員", value=f'{enum}', inline=False)
            await ctx.send(embed=embed)

def setup(Misaki):
    Misaki.add_cog(MainCommands(Misaki))