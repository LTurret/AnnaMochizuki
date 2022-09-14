import datetime
import discord

from discord.ext import commands
from random import randint

configurations = {
    "MLTD_Misaki_about": "https://zh.moegirl.org/zh-tw/%E9%9D%92%E7%BE%BD%E7%BE%8E%E5%92%B2",
    "早坂空_about": "https://zh.wikipedia.org/wiki/%E5%81%B6%E5%83%8F%E5%A4%A7%E5%B8%AB_%E7%99%BE%E8%90%AC%E4%BA%BA%E6%BC%94%E5%94%B1%E6%9C%83%EF%BC%81%E8%A7%92%E8%89%B2%E5%88%97%E8%A1%A8",
    "早坂空_avatar": "https://i.imgur.com/EPXQqym.png",
    "Draw_R": "<:GachaR:993767364392927302>",
    "Draw_SR": "<:GachaSR:993767365919645727>",
    "Draw_SSR": "<:GachaSSR:993767368264273960>"
}

class general(commands.Cog):
    def __init__(self, Anna):
        self.Anna = Anna

    @commands.command()
    async def gacha(self, ctx, amount:int):
        author = ctx.author
        if amount > 10:
            await ctx.send(content = "單次抽獎上限為10次喲", hidden = True)
        else:
            result = str()
            for draw in range(amount):
                if draw == 9:
                    reward = configurations['Draw_SR']
                    result = result + ' ' + reward
                else:
                    percentage = randint(1, 100)
                    if percentage <= 15 and percentage > 3:
                        reward = configurations['Draw_SR']
                    elif (percentage <= 3):
                        reward = configurations['Draw_SSR']
                    else:
                        reward = configurations['Draw_R']
                    result = result + ' ' + reward
            if amount == 1:
                embed = discord.Embed(title = f'{str(author)[:-5]} 的轉蛋結果', description = "拍到大家的笑容了！", colour = 0x93e2df, timestamp = datetime.datetime.utcnow())
                embed.set_author(name = "早坂そら", url = configurations['早坂空_about'], icon_url = configurations['早坂空_avatar'])
                embed.add_field(name = f'> 轉出機率為',value = f'**{percentage}%**', inline = False)
                embed.add_field(name = "> 抽獎結果", value = f'{result}', inline = False)
                await ctx.send(embed = embed)
            elif amount > 1 and amount != 10:
                embed = discord.Embed(title = f'{str(author)[:-5]} 的轉蛋結果', description = "拍到大家的笑容了！", colour = 0x93e2df, timestamp = datetime.datetime.utcnow())
                embed.set_author(name = "早坂そら", url = configurations['早坂空_about'], icon_url = configurations['早坂空_avatar'])
                embed.add_field(name = "> 抽獎結果", value = f'{result}', inline = False)
                await ctx.send(embed = embed)
            elif amount == 10:
                embed = discord.Embed(title = f'{str(author)[:-5]} 的轉蛋結果', description = "拍到大家的笑容了！", colour = 0x93e2df, timestamp = datetime.datetime.utcnow())
                embed.set_author(name = "早坂そら", url = configurations['早坂空_about'], icon_url = configurations['早坂空_avatar'])
                embed.add_field(name = "> 抽獎結果，抽了10次有SR保底", value = f'{result}', inline = False)
                await ctx.send(embed = embed)
    
def setup(Anna):
    Anna.add_cog(general(Anna))