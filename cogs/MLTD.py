import discord
import json
import datetime
import urllib.request as request
from random import randint
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice

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

    @cog_ext.cog_slash(name = "轉蛋",
                       description = "MLTD轉蛋模擬器",
                       guild_ids = GlobalSetting["guild_ids"],
                       options = [
                           create_option(
                               name = "amount",
                               description = "轉蛋數量",
                               option_type = 4,
                               required = True
                           )
                       ])
    async def 轉蛋(self, ctx:SlashContext, amount:int):
        server = self.Misaki.get_guild(ctx.guild_id)
        author = server.get_member(ctx.author)
        if (amount > 10):
            await ctx.send(content = "單次抽獎上限為10次喲", hidden = True)
        else:
            result = " "
            for draw in range(amount):
                if (draw == 9):
                    reward = Mjson['Draw_SR']
                    result = result + ' ' + reward
                else:
                    percentage = randint(1, 100)
                    if (percentage <= 15 and percentage > 3):
                        reward = Mjson['Draw_SR']
                    elif (percentage <= 3):
                        reward = Mjson['Draw_SSR']
                    else:
                        reward = Mjson['Draw_R']
                    result = result + ' ' + reward
            if (amount == 1):
                embed = discord.Embed(title = f'{str(author)[:-5]} 的轉蛋結果', description = "拍到大家的笑容了！", colour = 0x93e2df, timestamp = datetime.datetime.utcnow())
                embed.set_author(name = "早坂そら", url = Mjson['早坂空_about'], icon_url = Mjson['早坂空_avatar'])
                embed.add_field(name = f'> 轉出機率為',value = f'**{percentage}%**', inline = False)
                embed.add_field(name = "> 抽獎結果", value = f'{result}', inline = False)
                await ctx.send(embed = embed)
            elif (amount > 1 and amount != 10):
                embed = discord.Embed(title = f'{str(author)[:-5]} 的轉蛋結果', description = "拍到大家的笑容了！", colour = 0x93e2df, timestamp = datetime.datetime.utcnow())
                embed.set_author(name = "早坂そら", url = Mjson['早坂空_about'], icon_url = Mjson['早坂空_avatar'])
                embed.add_field(name = "> 抽獎結果", value = f'{result}', inline = False)
                await ctx.send(embed = embed)
            elif (amount == 10):
                embed = discord.Embed(title = f'{str(author)[:-5]} 的轉蛋結果', description = "拍到大家的笑容了！", colour = 0x93e2df, timestamp = datetime.datetime.utcnow())
                embed.set_author(name = "早坂そら", url = Mjson['早坂空_about'], icon_url = Mjson['早坂空_avatar'])
                embed.add_field(name = "> 抽獎結果，抽了10次有SR保底", value = f'{result}', inline = False)
                await ctx.send(embed = embed)

    @cog_ext.cog_slash(name = "event",
                       description = "查MLTW pt或高分榜",
                       guild_ids = GlobalSetting["guild_ids"],
                       options = [
                           create_option(
                               name = "id",
                               description = "活動id",
                               option_type = 4,
                               required = True
                           ),
                           create_option(
                               name = "type",
                               description = "榜單類型",
                               option_type = 3,
                               required = True,
                               choices = [
                                   create_choice(
                                       name = "pt榜",
                                       value = "eventPoint"
                                   ),
                                   create_choice(
                                       name = "高分榜",
                                       value = "highScore"
                                   )
                               ]
                           )
                       ])
    async def event(self, ctx:SlashContext, id, type):
        src = "https://mltd-zh.azurewebsites.net/api/events/" + str(id) + "/rankings/borderPoints"
        result = ""
        with request.urlopen(src) as response:
            data = json.load(response)
            date_type = [data["date"]["evtBegin"][:-14], data["date"]["evtEnd"][:-14]]
            time_code = [" 15:00 ~ ", " 20:59"] 
            evtRng = "活動期間："
            evtBoost = "加倍日期：" + data["date"]["boostBegin"][:-14].replace("-", "/")
            n = 0
            for date in date_type:
                evtRng += date + time_code[n]
                n = n + 1
            evtRng = evtRng.replace("-", "/")
            result = data["evtName"] + f'\n\n{evtRng}\n{evtBoost}\n'
            information = data[type]["scores"]
            for datum in information:
                result += '\n排名：{:>5}'.format(datum["rank"]) + '   '  + '分數：{:>10,}'.format(datum["score"]) + '  ' +  '名稱： {:^0}'.format(datum["name"])
            result = "```\n" + result + "```"
        await ctx.send(content = result, hidden = False)
            
def setup(Misaki):
    Misaki.add_cog(MLTD(Misaki))