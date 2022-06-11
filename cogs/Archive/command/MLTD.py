import aiohttp
import discord
import json
import os
import datetime
import asyncio
import urllib.request as request
from random import randint
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice

# functional image path:
fpath = "./images/functional"
# mltdevent image path:
mepath = "./images/mltdevent"

def typematch(typeid):
    match typeid:
        case 3:
            return True
        case 4:
            return True
        case 11:
            return True
        case 13:
            return True
        case 16:
            return True
        case _:
            return False

with open ("./json/mltd.json", mode="r", encoding='utf8') as MLTDjson:
    Mjson = json.load(MLTDjson)
with open ("./json/config.json", mode="r", encoding="utf8") as config:
    config = json.load(config)

# aiohttp for event boarding
async def GetNewestEvent(session):
    print(f"fetching event id at: {str(datetime.datetime.now()):0.22}")
    async with session.get("https://api.matsurihi.me/mltd/v1/events") as response:
        try:
            data = await response.json()
            return data[-1]
        except Exception as e:
            print(f"exception occur: {e}")

async def SearchEvent(evtid, session):
    async with session.get(f"https://api.matsurihi.me/mltd/v1/events/{evtid}") as response:
        print(f"fetching event information at: {str(datetime.datetime.now()):0.22}")
        try:
            data = await response.json()
            return data
        except Exception as e:
            print(f"exception occur: {e}")
    
async def FetchBorder(evtid, session):
    async with session.get(f"https://api.matsurihi.me/mltd/v1/events/{evtid}/rankings/borderPoints") as response:
        print(f"fetching event border at: {str(datetime.datetime.now()):0.22}")
        try:
            data = await response.json()
            return data
        except Exception as e:
            print(f"exception occur: {e}")

async def FetchCover(session, evtid):
    async with session.get(f"https://storage.matsurihi.me/mltd/event_bg/{evtid:0>4,d}.png") as response:
        print(f"fetching event cover image at: {str(datetime.datetime.now()):0.22}")
        try:
            with open(f"{evtid:0>4,d}.png", "wb") as file:
                file.write(await response.read())
        except Exception as e:
            print(f"exception occur: {e}")

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
                                       name = "圖片模式",
                                       value = "image"
                                   ),
                                   create_choice(
                                       name = "文字模式",
                                       value = "text"
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
    async def event(self, ctx, display_mode="image", score_type="eventPoint"):
        async with aiohttp.ClientSession() as session:
            # 協程擷取json
            eventData = await GetNewestEvent(session)
            if not(os.listdir(mepath).count(f'{eventData["id"]:0>4,d}.png')):
                await FetchBorder(eventData["id"], session)
            if (typematch(eventData["type"])):
                tasks = [
                    asyncio.create_task(FetchBorder(eventData["id"], session))
                ]
                await asyncio.gather(*tasks)
                BorderData = tasks[0].result()

                # 指定資料
                eventName = eventData["name"]
                beginDate = eventData["schedule"]["beginDate"]
                endDate = eventData["schedule"]["endDate"]
                boostDate = eventData["schedule"]["boostBeginDate"]
                timeSummaries = BorderData[score_type]["summaryTime"]

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

                # 台灣時間以及當前時間，方便觀察
                current_time = datetime.datetime.now()
                end_time = datetime.datetime(int(endDate[0:4]), int(endDate[5:7]), int(endDate[8:10]), 19, 59, 59, 0)
                different_time = end_time - current_time
                different_hours = different_time.total_seconds() / 3600
                different_days = different_hours / 24
                total_hours = dayLength*24
                progress = (total_hours-different_hours) / total_hours
                taipei_time = int(timeSummaries[11:13]) - 1
                taipei_time = f"{int(taipei_time)}{timeSummaries[13:16]}"

                # 榜線數據標頭
                result = f'https://mltd.matsurihi.me/events/{eventData["id"]}\n'
                result += "```"

                # 字型設定
                font_path = f"{mepath}/component/jf-openhuninn-1.1.ttf"
                boarding = ImageFont.truetype(font_path, 30)
                title = ImageFont.truetype(font_path, 30)
                fetchtime = ImageFont.truetype(font_path, 23)
                body = ImageFont.truetype(font_path, 20)

                # Pillow 畫布設定
                bgpath = f"{mepath}/component/AnnaFrame.png"
                AnnaFrame = Image.open(bgpath)
                AnnaFrame = AnnaFrame.convert('RGBA')
                draw = ImageDraw.Draw(AnnaFrame)

                # Pillow 設定
                y_globe = 290
                y_accumulate = 40
                x_globe = 40
                length_adjust = 1
                adjust_x = 150

                # 圖片資訊產生
                draw.text((x_globe,35), f"{eventName}", (2, 62, 125), font=title)
                draw.text((x_globe,80), f"資料時間：{time_date} ({progress:.1%})\n", (51, 65, 92), font=fetchtime)
                draw.text((x_globe,120), f"活動期間：{beginDate} ~ {endDate} ({dayLength*24}小時)\n", (92, 103, 125), font=body)
                draw.text((x_globe,145), f"後半期間：{boostDate} ~ {endDate}\n", (92, 103, 125), font=body)
                draw.text((x_globe,170), f"剩下時間：{different_days:.2}天 ({int(different_hours)}小時)\n", (92, 103, 125), font=body)

                # 圖片排名產生
                for data in BorderData['eventPoint']["scores"]:
                    rank = data["rank"]
                    score = data["score"]
                    if score is not None:
                        if (length_adjust <= 3):
                            argx = 73
                        elif (length_adjust == 4):
                            argx = 36
                        elif (length_adjust > 4 and length_adjust < 7):
                            argx = 18
                        else:
                            argx = 0
                        draw.text(xy=(x_globe + argx, y_globe),
                                text=f"{rank}",
                                fill=(3, 83, 164),
                                font=boarding
                                )
                        draw.text(xy=(x_globe + 95, y_globe), text="位", fill=(3, 83, 164), font=boarding)
                        if (len(str(score)) == 8):
                            adjust_x = 176.8
                        elif (len(str(score)) == 7):
                            adjust_x = 194
                        draw.text((x_globe + adjust_x + 30, y_globe),f"{score:,.0f}", (4, 102, 200), font=boarding)
                        y_globe += y_accumulate
                        length_adjust += 1

                AnnaFrame.save(f"{mepath}/boarding.png")

                # 文字模式
                result += f"{eventName}\n"
                result += f"活動期間：{beginDate} ~ {endDate} ({dayLength*24}小時)\n"
                result += f"後半期間：{boostDate} ~ {endDate}\n"
                result += f"更新時間：{time_date} ({progress:.1%})\n"
                result += f"剩下時間：{different_days:.2}天 ({different_hours:.3}小時)\n"

                # 榜線資料
                result += f"\n"
                for data in BorderData[score_type]["scores"]:
                    rank = data["rank"]
                    score = data["score"]
                    if score is not None:
                        result += f"排名：{rank:<10,d}分數：{score:>10,.0f}\n"
                result = f"{result}```"

                if display_mode == "text":
                    await ctx.send(content=result, hidden=False)
                else:
                    image = discord.File(f"{mepath}/boarding.png")
                    await ctx.send(file=image, hidden=False)
                # image = discord.File(f'{mepath}/{eventData["id"]:0>4,d}.png')
            else:
                await ctx.send(content="目前沒有活動", hidden=False)




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




    @cog_ext.cog_slash(name="randompics",
                        description="隨機發一張圖片出來",
                        guild_ids=config['guild_ids'])
    async def randompics(self, ctx):
        path = f"{fpath}/random"
        file = [filename for filename in os.listdir(f"{path}")]
        print(file)
        await ctx.channel.send(discord.File())

def setup(Anna):
    Anna.add_cog(MLTD(Anna))