import discord
import json
import datetime
from discord.ext import commands

with open ('setting.json', 'r', encoding='utf8') as jsonSetting:
    jdata = json.load(jsonSetting)

class MLTD(commands.Cog):
    def __init__(self, Misaki):
        self.Misaki = Misaki

    #add embedded sheets here
    @commands.command()
    async def helplist(self, ctx):
        embed=discord.Embed(title = "MLTD指令選單", description = "大家的事務員，青羽美咲！", colo = 0x00ffff
        , timestamp = datetime.datetime.now)
        embed.set_author(name = "青羽美咲", url = jdata['MLTD_Misaki_about'], icon_url = jdata['MLTD_765_icon'])
        embed.set_thumbnail(url = "https://i.imgur.com/eEKg1Vn.jpg")
        embed.add_field(name = "直播推廣通知", value = "@青羽美咲 Stream", inline = True)
        embed.add_field(name = "日服活動確認", value = "@青羽美咲 JPevent", inline = True)
        embed.add_field(name = "台服活動確認", value = "@青羽美咲 TWevent", inline = True)
        embed.set_footer(text = "2020/**/** timedatestamp")
        await self.Misaki.say(embed=embed)

    #probably code an asyncio function to here.
    #it will be standard asyncio or be discord std function.
    @commands.command()
    async def Stream(self, ctx):
        await ctx.send(jdata['MLTD_StreamPic'])
        await ctx.send(jdata['MLTD_StreamLink'])

def setup(Misaki):
    Misaki.add_cog(MLTD(Misaki))