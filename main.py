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
    if (round(Misaki.latency*1000) >= 100):
        await ctx.send(f'你與我的距離為 {round(Misaki.latency*1000)} 毫秒')
        await ctx.send('有夠遠的 :ok_this_is_epic:')
    else:
        await ctx.send(f'你與我的距離為 {round(Misaki.latency*1000)} 毫秒')

@Misaki.command()
async def 鄭順謙(ctx):
    await ctx.send('還錢')

@Misaki.command()
async def 水塔(ctx):
    await ctx.send('鄭順謙')
    await ctx.send('還錢')


Misaki.run('NzEyMjQzMDQwNzYwMTAyOTky.XsOu7A.6UD4xvWSbWH0LSIy_A8mgFNOEmA')