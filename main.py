import discord
from discord.ext import commands

Misaki = commands.Bot(command_prefix='|')

@Misaki.event
async def on_ready():
    print("Misaki is working!")

@Misaki.event
async def on_member_join(member):
    channel = Misaki.get_channel(474858135853596675)
    await channel.send(f'{member.mention} 加入了漢堡群')

@Misaki.event
async def on_member_remove(member):
    channel = Misaki.get_channel(474858135853596675)
    await channel.send(f'{member.mention} 退出了漢堡群，SAD！')

@Misaki.command()
async def ping(ctx):
    await ctx.send(f'你與我的距離為 {round(Misaki.latency*1000)} 毫秒')

Misaki.run('NzEyMjQzMDQwNzYwMTAyOTky.XsOu7A.6UD4xvWSbWH0LSIy_A8mgFNOEmA')