import discord
from discord.ext import commands
from typing import Optional
import random

class MainCommands(commands.Cog):
    def __init__(self, Misaki):
        self.Misaki = Misaki

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
    async def rds(self, ctx, keyword:str, sampling:int, rng:int):
        hasNick = []
        for member in ctx.guild.members:
            if member.nick != None and member.nick.count(keyword):
                hasNick.append(member)
        for hasSamp in random.sample(hasNick, k=sampling):
            print(hasSamp)

def setup(Misaki):
    Misaki.add_cog(MainCommands(Misaki))