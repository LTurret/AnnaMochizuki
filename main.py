import discord
from discord.ext import commands

Misaki = commands.Bot(command_prefix='|')

@Misaki.event
async def on_ready():
    print("Misaki is working!")

@Misaki.event
async def on_member_join(member):
    print(f'{member} 加入了漢堡群！')

@Misaki.event
async def on_member_leave(member):
    print(f'{member} 退出了漢堡群，SAD')

Misaki.run('NzEyMjQzMDQwNzYwMTAyOTky.XsOu7A.6UD4xvWSbWH0LSIy_A8mgFNOEmA')