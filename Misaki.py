import discord
import json
import os
from discord.ext import commands

with open ('setting.json', 'r', encoding='utf8') as jsonSetting:
    jdata = json.load(jsonSetting)

Misaki = commands.Bot(command_prefix=commands.when_mentioned, description='Hello world')

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

@Misaki.command()
async def load(ctx, extension):
    Misaki.load_extension(f'cogs.{extension}')

@Misaki.command()
async def unload(ctx, extension):
    Misaki.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        Misaki.load_extension(f'cogs.{filename[:-3]}')

Misaki.run(jdata['BotToken'])