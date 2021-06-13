import discord
import json
import datetime
import random
import urllib.request as request
from discord.ext import commands
from discord_slash import cog_ext

with open (r"C:\Users\a0919\Desktop\Files\Programming\Github\Suspend-bot\json\mltd.json", 'r', encoding='utf8') as MLTDjson:
    Mjson = json.load(MLTDjson)
with open (r"C:\Users\a0919\Desktop\Files\Programming\Github\Suspend-bot\json\setting.json", 'r', encoding="utf8") as GlobalSetting:
    GlobalSetting = json.load(GlobalSetting)

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

    @cog_ext.cog_slash(name = "ouen",
                       description = '使用指令後打上"応援するよ！"來為杏奈應援！！',
                       guild_ids = GlobalSetting['guild_ids'])
    async def ouen(self, ctx):
        await ctx.send(content = f"(＊>△<)＜応援ください！")

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
    async def MLTDtest(self, ctx):
        await ctx.message.delete()
        src = "https://mltd-zh.azurewebsites.net/api/events/72/rankings/borderPoints"
        result = ""
        with request.urlopen(src) as response:
            data = json.load(response)
            information = data["eventPoint"]["scores"]
            for datum in information:
                result += '\n排名：{:>5}'.format(datum["rank"]) + '   '  + '分數：{:>10,}'.format(datum["score"]) + '  ' +  '名稱： {:^0}'.format(datum["name"])
        await ctx.channel.send(result)
    # @commands.command()
    # async def MLTDevent(self, ctx, id:int, mode):
    #     eventid = str(id)
    #     src = "https://mltd-zh.azurewebsites.net/api/events/"+eventid+"/rankings/borderPoints"
    #     result = ""
    #     with request.urlopen(src) as response:
    #         data = json.load(response)
    #         if mode.upper() == "PT":
    #             mode = "eventPoint"
    #         elif mode.upper() == "SCORE":
    #             mode = "highScore"
    #         data = response[mode]["scores"]
    #         for datum in data:
    #             result += '\n排名：{:>5}'.format(datum["rank"]) + '   '  + '分數：{:>10,}'.format(datum["score"]) + '  ' +  '名稱： {:^0}'.format(datum["name"])
    #     print(result)
    #     #await ctx.channel.send(data)
            
def setup(Misaki):
    Misaki.add_cog(MLTD(Misaki))