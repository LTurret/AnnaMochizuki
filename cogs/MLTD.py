import discord
import json
import datetime
import random
import bs4
import urllib.request as req
from discord.ext import commands

with open (r"C:\Users\a0919\Desktop\Files\Programming\Github\Suspend-bot\json\mltd.json", 'r', encoding='utf8') as MLTDjson:
    Mjson = json.load(MLTDjson)

class MLTD(commands.Cog):
    def __init__(self, Misaki):
        self.Misaki = Misaki

    @commands.command()
    async def 轉蛋機率(self, ctx):
        embed = discord.Embed(title = "轉蛋機率"
        , description = None, colour = 0x93e2df, timestamp = datetime.datetime.utcnow())
        embed.add_field(name = "> <:SSR:723921126560104539>", value = '**"提供機率" 3%，也就是 "轉出機率" <= 3%**', inline = False)
        embed.add_field(name = "> <:SR:723921117013606460>", value = '**"提供機率" 12%，也就是 "轉出機率" <= 15%**', inline = False)
        embed.add_field(name = "> <:R_:723921106909659227>", value = '**"提供機率" 85%，也就是 "轉出機率" > 15%**', inline = False)
        await ctx.send(embed=embed)

    @commands.command()
    async def ouen(self, ctx):
        await ctx.message.delete()
        await ctx.channel.send("(＊>△<)＜応援ください！")
        self.OuenActivation = True

    @commands.command()
    async def 轉蛋(self, ctx, amount:int):
        if (amount > 10):
            await ctx.channel.send("單次抽獎上限為10次喲")
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
            if (amount == 1):
                embed = discord.Embed(title = f'{str(ctx.message.author)[:-5]} 的轉蛋結果', description = "拍到大家的笑容了！", colour = 0x93e2df, timestamp = datetime.datetime.utcnow())
                embed.set_author(name = "早坂そら", url = Mjson['早坂空_about'], icon_url = Mjson['早坂空_avatar'])
                embed.add_field(name = f'> 轉出機率為',value = f'**{percentage}%**', inline = False)
                embed.add_field(name = "> 抽獎結果", value = f'{result}', inline = False)
                await ctx.send(embed=embed)
            elif (amount > 1 and amount != 10):
                embed = discord.Embed(title = f'{str(ctx.message.author)[:-5]} 的轉蛋結果', description = "拍到大家的笑容了！", colour = 0x93e2df, timestamp = datetime.datetime.utcnow())
                embed.set_author(name = "早坂そら", url = Mjson['早坂空_about'], icon_url = Mjson['早坂空_avatar'])
                embed.add_field(name = "> 抽獎結果", value = f'{result}', inline = False)
                await ctx.send(embed=embed)
            elif (amount == 10):
                embed = discord.Embed(title = f'{str(ctx.message.author)[:-5]} 的轉蛋結果', description = "拍到大家的笑容了！", colour = 0x93e2df, timestamp = datetime.datetime.utcnow())
                embed.set_author(name = "早坂そら", url = Mjson['早坂空_about'], icon_url = Mjson['早坂空_avatar'])
                embed.add_field(name = "> 抽獎結果，抽了10次有SR保底", value = f'{result}', inline = False)
                await ctx.send(embed=embed)

    @commands.command()
    async def getData(self, character_name:str):
        #put a character name list here
        #serction 1.
        #   put every character name to embed message to show off all option
        url = "https://imas.gamedbs.jp/mlth/"
        request = req.Request(url, headers= {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
        })
        with req.urlopen(request) as response:
            data = response.read().decode("utf-8")
        root = bs4.BeautifulSoup(data, "html.parser")
        source = root.find_all("li", class_="hvr-grow")
        Idol = []
        for source_information in source:
            character_name = source_information.a.get("title")[0:len(source_information)-6]
            Idol.append(character_name)
            for IdolName in Idol:
                if str(IdolName) == character_name:
                    print(IdolName)

def setup(Misaki):
    Misaki.add_cog(MLTD(Misaki))