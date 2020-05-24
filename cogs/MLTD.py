import discord
import json
import datetime
from discord.ext import commands

with open (r"C:\Users\George Rupp\Desktop\Files\Programming\Github\Suspend-bot\json\MLTD.json", 'r', encoding='utf8') as jsonSetting:
    jdata = json.load(jsonSetting)

class MLTD(commands.Cog):
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

    @commands.command()
    async def MLTDhelp(self, ctx):
        embed = discord.Embed(title = "MLTD指令選單", description = "大家的事務員，青羽美咲！", colour = 0x93e2df
        , timestamp = datetime.datetime.utcnow())
        embed.set_author(name = "青羽美咲", url = jdata['MLTD_Misaki_about'], icon_url = jdata['MLTD_765_icon'])
        embed.set_thumbnail(url = "https://i.imgur.com/eEKg1Vn.jpg")
        embed.add_field(name = "大和美少女", value = "**@青羽美咲 大和美少女**", inline = False)
        embed.add_field(name = "南斗", value = "**@青羽美咲 南斗**", inline = False)
        embed.add_field(name = "歌單", value = "**@青羽美咲 歌單**", inline = False)
        embed.add_field(name = "直播推廣通知", value = "**@青羽美咲 Stream**", inline = False)
        embed.add_field(name = "日服活動確認", value = "**@青羽美咲 JPevent**", inline = False)
        embed.add_field(name = "台服活動確認", value = "**@青羽美咲 TWevent**", inline = False)
        embed.set_footer(text = "なんとぉー！")
        await ctx.send(embed=embed)

    @commands.command()
    async def TWevent(self, ctx):
        embed = discord.Embed(title = "台服活動貼文", colour = 0x93e2df
        , timestamp = datetime.datetime.utcnow())
        embed.set_author(name = "偶像大師 百萬人演唱會！劇場時光", url = "https://www.facebook.com/idolmastermlTD.ch/?epa=SEARCH_BOX", icon_url = jdata['MLTD_TWevent_avatar'])
        embed.set_image(url = jdata['MLTD_TWevent_cover'])
        embed.add_field(name = "內文", value = jdata['MLTD_TWevent_ann'], inline = False)
        await ctx.send(embed=embed)

    #probably code an asyncio function to here.
    #it will be standard asyncio or be discord std function.
    @commands.command()
    async def Stream(self, ctx):
        await ctx.send(jdata['MLTD_StreamPic'])
        await ctx.send(jdata['MLTD_StreamLink'])

def setup(Misaki):
    Misaki.add_cog(MLTD(Misaki))