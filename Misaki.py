import discord
import json
import os
from discord.ext import commands

with open (r"C:\Users\George Rupp\Desktop\Files\Programming\Github\Suspend-bot\json\setting.json", 'r', encoding='utf8') as jsonSetting:
    jdata = json.load(jsonSetting)

Misaki = commands.Bot(command_prefix=commands.when_mentioned, description="大家的事務員-青羽美咲")
Misaki.remove_command('help')

@Misaki.event
async def on_ready():
    await Misaki.change_presence(status = discord.Status.online, activity = discord.Game('アイドルマスター ミリオンライブ!'))
    print("Misaki is online!\n大家的事務員，青羽美咲上線啦！")

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
    await ctx.send(f'function **{extension}** loadeded.')

@Misaki.command()
async def unload(ctx, extension):
    Misaki.unload_extension(f'cogs.{extension}')
    await ctx.send(f'function **{extension}** unloaded.')

@Misaki.command()
async def reload(ctx, extension):
    Misaki.reload_extension(f'cogs.{extension}')
    await ctx.send(f'function **{extension}** reloaded.')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        Misaki.load_extension(f'cogs.{filename[:-3]}')

Misaki.run(jdata['BotToken'])