import discord
import json
from discord.ext import commands

with open ('setting.json', 'r', encoding='utf8') as jsonSetting:
    jdata = json.load(jsonSetting)

class MLTD(commands.Cog):
    def __init__(self, Misaki):
        self.Misaki = Misaki

    #add embedded sheets here
    @commands.command()
    async def helplist(self, ctx):
        await ctx.send('soon')

    #probably code an asyncio function to here.
    #it will be standard asyncio or be discord std function.
    @commands.command()
    async def Stream(self, ctx):
        await ctx.send(jdata['MLTD_StreamPic'])
        await ctx.send(jdata['MLTD_StreamLink'])

def setup(Misaki):
    Misaki.add_cog(MLTD(Misaki))