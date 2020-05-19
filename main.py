import discord
import json
from discord.ext import commands

with open ('setting.json', 'r', encoding='utf8') as jsonSetting:
    jdata = json.load(jsonSetting)

Misaki = commands.Bot(command_prefix='|')

@Misaki.event
async def on_ready():
    print("Misaki is working!\n大家的事務員，美咲上班啦！")

@Misaki.event
async def on_member_join(member):
    channel = Misaki.get_channel(int(jdata['MainChannelID']))
    await channel.send(f'{member.mention} 加入了漢堡群！')

@Misaki.event
async def on_member_remove(member):
    channel = Misaki.get_channel(int(jdata['MainChannelID']))
    await channel.send(f'{member.mention} 退出了漢堡群，SAD！')

@Misaki.listen()
async def on_message(message):
     if "help" == message.content:
        channel = Misaki.get_channel(int(jdata['MainChannelID']))
        await channel.send('okay here\'s list...')
     elif "水塔" == message.content:
        channel = Misaki.get_channel(int(jdata['MainChannelID']))
        await channel.send('鄭順謙')

@Misaki.command()
async def ping(ctx):
    if (round(Misaki.latency*1000) >= 100):
        await ctx.send(f'你與我的距離為 {round(Misaki.latency*1000)} 毫秒')
        await ctx.send('有夠遠的 :ok_this_is_epic:')
    else:
        await ctx.send(f'你與我的距離為 {round(Misaki.latency*1000)} 毫秒')

Misaki.run(jdata['BotToken'])