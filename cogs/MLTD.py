import discord
import json
import datetime
import random
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
        embed.set_author(name = "偶像大師 百萬人演唱會！劇場時光"
        , url = Mjson['MLTD_TW_about'], icon_url = Mjson['MLTD_TWevent_avatar'])
        embed.set_image(url = Mjson['MLTD_TWevent_cover'])
        embed.add_field(name = "內文", value = Eann['MLTD_TWevent_ann'], inline = False)
        await ctx.send(embed=embed)

    @commands.command()
    async def Stream(self, ctx):
        await ctx.send(Mjson['MLTD_StreamPic'])
        await ctx.send(Mjson['MLTD_StreamLink'])

    @commands.command()
    async def 轉蛋機率(self, ctx):
        embed = discord.Embed(title = "轉蛋機率"
        , description = None, colour = 0x93e2df, timestamp = datetime.datetime.utcnow())
        embed.add_field(name = "> <:SSR:723921126560104539>", value = '**"提供機率" 3%，也就是 "轉出機率" <= "3%"**', inline = False)
        embed.add_field(name = "> <:SR:723921117013606460>", value = '**"提供機率" 12%，也就是 "轉出機率" <= "15"**', inline = False)
        embed.add_field(name = "> <:R_:723921106909659227>", value = '**"提供機率" 85%，也就是 "轉出機率" >= "15"**', inline = False)
        await ctx.send(embed=embed)

    @commands.command()
    async def 轉蛋(self, ctx, amount:int):
        await ctx.message.delete()
        if (amount > 10):
            await ctx.channel.send("單次抽獎上限為10次喲", delete_after = 3)
        else:
            result = " "
            for draw in range(amount):
                if (draw == 9):
                    reward = Mjson['Draw_SR']
                    result = result + ' ' + reward
                else:
                    percentage = random.randint(1, 100)
                    if (percentage <= 15 and percentage > 3):
                        reward = Mjson['Draw_SR']
                    elif (percentage <= 3):
                        reward = Mjson['Draw_SSR']
                    else:
                        reward = Mjson['Draw_R']
                    result = result + ' ' + reward
            if (amount >= 1 and amount != 10):
                #await ctx.channel.send(f'<@{ctx.message.author.id}> 的轉出機率為{percentage}%，抽了{draw+1}次的{result}')
                embed = discord.Embed(title = f'{str(ctx.message.author)[:-5]} 的轉蛋結果'
                , description = "拍到大家的笑容了！", colour = 0x93e2df, timestamp = datetime.datetime.utcnow())
                embed.set_author(name = "早坂そら", url = Mjson['早坂空_about'], icon_url = Mjson['早坂空_avatar'])
                embed.add_field(name = f'> 轉出機率為',value = f'**{percentage}%**', inline = False)
                embed.add_field(name = "> 抽獎結果", value = f'{result}', inline = False)
                await ctx.send(embed=embed)
            elif (amount == 10):
                #await ctx.channel.send(f'抽了{draw+1}次的{result}')
                embed = discord.Embed(title = f'{str(ctx.message.author)[:-5]} 的轉蛋結果'
                , description = "拍到大家的笑容了！", colour = 0x93e2df, timestamp = datetime.datetime.utcnow())
                embed.set_author(name = "早坂そら", url = Mjson['早坂空_about'], icon_url = Mjson['早坂空_avatar'])
                embed.add_field(name = "> 抽獎結果，抽了10次有SR保底", value = f'{result}', inline = False)
                await ctx.send(embed=embed)

def setup(Misaki):
    Misaki.add_cog(MLTD(Misaki))