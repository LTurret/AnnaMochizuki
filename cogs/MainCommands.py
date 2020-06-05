import discord
from discord.ext import commands
from re import search

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
    async def botsaid(self, ctx, *,message):
        await ctx.message.delete()
        await ctx.send(message)
    
    @commands.command()
    async def rand_squad(self, ctx):
        for member in ctx.guild.members:
            thestring = "LT"
            #if str(member).find("LT"):
            if search(str(member), thestring):
                print(f"{member} has 'LT' in its name!")
            else:
                print(f"{member} hasn't 'LT' in its name!")
                    

def setup(Misaki):
    Misaki.add_cog(MainCommands(Misaki))