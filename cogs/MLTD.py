import discord
import json
import datetime
from discord.ext import commands

with open (r"C:\Users\George Rupp\Desktop\Files\Programming\Github\Suspend-bot\json\MLTD.json", 'r', encoding='utf8') as MLTDjson:
    Mjson = json.load(MLTDjson)
with open (r"C:\Users\George Rupp\Desktop\Files\Programming\Github\Suspend-bot\json\announce.json", 'r', encoding='utf8') as EventDescription:
    Eann = json.load(EventDescription)

class MLTD(commands.Cog):
    def __init__(self, Misaki):
        self.Misaki = Misaki

    @commands.command()
    async def 大和美少女(self, ctx):
        pic = discord.File(Mjson['大和美少女'])
        await ctx.send(file=pic)

    @commands.command()
    async def 南斗(self, ctx):
        pic = discord.File(Mjson['南斗'])
        await ctx.send(file=pic)

    @commands.command()
    async def 歌單(self, ctx):
        await ctx.send(Mjson['歌單'])

    @commands.command()
    async def TWevent(self, ctx):
        embed = discord.Embed(title = "台服活動貼文", colour = 0x93e2df
        , timestamp = datetime.datetime.utcnow())
        embed.set_author(name = "偶像大師 百萬人演唱會！劇場時光", url = "https://www.facebook.com/idolmastermlTD.ch/?epa=SEARCH_BOX", icon_url = Mjson['MLTD_TWevent_avatar'])
        embed.set_image(url = Mjson['MLTD_TWevent_cover'])
        embed.add_field(name = "內文", value = Eann['MLTD_TWevent_ann'], inline = False)
        await ctx.send(embed=embed)

    @commands.command()
    async def Stream(self, ctx):
        await ctx.send(Mjson['MLTD_StreamPic'])
        await ctx.send(Mjson['MLTD_StreamLink'])

def setup(Misaki):
    Misaki.add_cog(MLTD(Misaki))