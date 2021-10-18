import discord
import json
import datetime
import asyncio
import urllib.request as request
from random import randint
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice

with open ("./json/mltd.json", mode="r", encoding='utf8') as MLTDjson:
    Mjson = json.load(MLTDjson)
with open ("./json/config.json", mode="r", encoding="utf8") as config:
    config = json.load(config)

async def getEvent():
    url = "https://api.matsurihi.me/mltd/v1/events"
    with request.urlopen(url) as response:
        data = json.load(response)
    print("Feteched Event Information.")
    return data[-1]

async def getBoarding(evtid):
    url = f"https://api.matsurihi.me/mltd/v1/events/{str(evtid)}/rankings/borderPoints"
    with request.urlopen(url) as response:
        data = json.load(response)
    print("Feteched RankBoarding.")
    return data

async def create_BoardingCache(fetched_data):
    with open("BoardingCache.json", mode="w", encoding="utf-8") as cache:
        json.dump(fetched_data, cache, indent=4, ensure_ascii=False)
    print("Dumped BoardingCache")

async def create_EvtInfoCache(fetched_data):
    with open("EvtInfoCache.json", mode="w", encoding="utf-8") as cache:
        json.dump(fetched_data, cache, indent=4, ensure_ascii=False)
    print("Dumped EvtInfoCache")

class MLTD(commands.Cog):
    def __init__(self, Anna):
        self.Anna = Anna

    @commands.command()
    async def roll_chance(self, ctx):
        embed = discord.Embed(title = "轉蛋機率"
        , description = None, colour = 0x93e2df, timestamp = datetime.datetime.utcnow())
        embed.add_field(name = "> <:SSR:723921126560104539>", value = '**"提供機率" 3%，也就是 "轉出機率" <= 3%**', inline = False)
        embed.add_field(name = "> <:SR:723921117013606460>", value = '**"提供機率" 12%，也就是 "轉出機率" <= 15%**', inline = False)
        embed.add_field(name = "> <:R_:723921106909659227>", value = '**"提供機率" 85%，也就是 "轉出機率" > 15%**', inline = False)
        await ctx.send(embed=embed)

    @cog_ext.cog_slash(name = "ouen",
                       description = '使用指令後打上"応援するよ！"來為杏奈應援！！',
                       guild_ids = config['guild_ids'])
    async def ouen(self, ctx):
        await ctx.send(content = f"(＊>△<)＜応援ください！")

    @cog_ext.cog_slash(name = "event",
                       description = "查MLTD日服pt榜",
                       guild_ids = config["guild_ids"],
                       options = [
                           create_option(
                               name = "display_mode",
                               description = "顯示模式",
                               option_type = 3,
                               required = False,
                               choices = [
                                   create_choice(
                                       name = "詳細模式",
                                       value = "detail"
                                   ),
                                   create_choice(
                                       name = "簡易模式",
                                       value = "lite"
                                   )
                               ]
                           ),
                           create_option(
                               name = "score_type",
                               description = "轉蛋數量",
                               option_type = 3,
                               required = False,
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
    async def event(self, ctx, display_mode="detail", score_type="eventPoint"):
        # 協程擷取json
        eventData = await getEvent()
        tasks = [
            asyncio.create_task(getBoarding(eventData["id"]))
        ]
        await asyncio.gather(*tasks)
        boardingDataset = tasks[0].result()

        # 指定資料
        eventName = eventData["name"]
        beginDate = eventData["schedule"]["beginDate"]
        endDate = eventData["schedule"]["endDate"]
        boostDate = eventData["schedule"]["boostBeginDate"]
        timeSummaries = boardingDataset[score_type]["summaryTime"]

        # 格式化日期
        beginDate = beginDate.replace("-", "/")[0:10]
        endDate = endDate.replace("-", "/")[0:10]
        boostDate = boostDate.replace("-", "/")[0:10]
        time_date = timeSummaries.replace("-","/")[0:10]
        time_date += f" {timeSummaries[11:16]}"

        # 活動天數
        formatedBD = datetime.date(int(beginDate[0:4]), int(beginDate[5:7]), int(beginDate[8:10]))
        formatedED = datetime.date(int(endDate[0:4]), int(endDate[5:7]), int(endDate[8:10]))
        dayLength = (formatedED - formatedBD).days

        # 新增台灣時間，方便觀察
        taipei_time = int(timeSummaries[11:13]) - 1
        taipei_time = f"{int(taipei_time)}{timeSummaries[13:16]}"

        # 榜線數據標頭
        result = str()

        # 顯示模式
        if display_mode == "detail":
            result += f"活動名稱：{eventName}\n"
            result += f"活動期間：{beginDate} ~ {endDate}\n"
            # result += f"活動天數：f"{dayLength}，已經過了：{percentage}"
            result += f"活動天數：{dayLength}天\n"
            result += f"加倍時間：{boostDate}\n"
        result += f"資料時間：{time_date}\n"

        # 榜線資料
        result += f"\n"
        for data in boardingDataset[score_type]["scores"]:
            rank = data["rank"]
            score = data["score"]
            if score is not None:
                result += f"排名：{rank:<10,d}分數：{score:>10,.0f}\n"
        result = f"```{result}```"
        await ctx.send(content=result, hidden=False)

    @cog_ext.cog_slash(name = "roll",
                       description = "MLTD轉蛋模擬器",
                       guild_ids = config["guild_ids"],
                       options = [
                           create_option(
                               name = "amount",
                               description = "轉蛋數量",
                               option_type = 4,
                               required = True
                           )
                       ])
    async def roll(self, ctx:SlashContext, amount:int):
        server = self.Anna.get_guild(ctx.guild_id)
        author = server.get_member(ctx.author)
        if (amount > 10):
            await ctx.send(content = "單次抽獎上限為10次喲", hidden = True)
        else:
            result = str()
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

def setup(Anna):
    Anna.add_cog(MLTD(Anna))
