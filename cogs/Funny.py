import discord
import json
from discord.ext import commands

with open ('setting.json', 'r', encoding='utf8') as jsonSetting:
    jdata = json.load(jsonSetting)

class Funny(commands.Cog):
    def __init__(self, Misaki):
        self.Misaki = Misaki

    @commands.command()
    async def 大和美少女(self, ctx):
        pic = discord.File(jdata['大和美少女'])
        await ctx.send(file=pic)

    @commands.command()
    async def 南斗(self, ctx):
        pic = discord.File(jdata['南斗'])
        await ctx.send(file=pic)

    @commands.command()
    async def 歌單(self, ctx):
        await ctx.send(jdata['歌單'])

    @commands.Cog.listener()
    async def on_message(self, message):
        #(if "help" == message.content:
            #channel = self.Misaki.get_channel(int(jdata['MainChannelID']))
            #await channel.send('okay here\'s list...'))
        if "<@712243040760102992>" == message.content:
            channel = self.Misaki.get_channel(int(jdata['MainChannelID']))
            await channel.send('是在ping啥小')

def setup(Misaki):
    Misaki.add_cog(Funny(Misaki))