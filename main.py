import discord
import json
from discord.ext import commands

with open ('setting.json', 'r', encoding='utf8') as jsonSetting:
    jdata = json.load(jsonSetting)

Misaki = commands.Bot(command_prefix='.')

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
        await ctx.send(f'你與我的距離為 {round(Misaki.latency*1000)} 毫秒\n有夠遠的')
    else:
        await ctx.send(f'你與我的距離為 {round(Misaki.latency*1000)} 毫秒')

@Misaki.command()
async def purge(ctx, amount=1):
	await ctx.channel.purge(limit=amount+1)

@Misaki.command()
async def 大和美少女(ctx):
    pic = discord.File('C:\\Users\\George Rupp\\Desktop\\Files\\Programming\\Github\\Suspend-bot\\local-picture\\水手大和.jpg')
    await ctx.send(file=pic)

@Misaki.command()
async def 南斗(ctx):
    pic = discord.File('C:\\Users\\George Rupp\\Desktop\\Files\\Programming\\Github\\Suspend-bot\\local-picture\\Misakiaoba.gif')
    await ctx.send(file=pic)

@Misaki.command()
async def 歌單(ctx):
    await ctx.send('https://www.youtube.com/playlist?list=PL7N_IWFrvzwsOLqvzI9D5lyKEuiV6dXkT')



Misaki.run(jdata['BotToken'])