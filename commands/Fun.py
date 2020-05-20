import discord
import json
from discord.ext import commands

with open ('setting.json', 'r', encoding='utf8') as jsonSetting:
    jdata = json.load(jsonSetting)

Misaki = commands.Bot(command_prefix='.')

class Fun(commands.Cog):
    def __init__(self, Misaki):
        self.bot = Misaki

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

    #Testing out
    @Misaki.listen()
    async def on_message(self, message):
        if "help" == message.content:
            channel = self.bot.get_channel(int(jdata['MainChannelID']))
            await channel.send('okay here\'s list...')
        elif "水塔" == message.content:
            channel = self.bot.get_channel(int(jdata['MainChannelID']))
            await channel.send('鄭順謙')

def setup(Misaki):
    Misaki.add_cog(Fun(Misaki))