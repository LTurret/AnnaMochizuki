import discord
from discord.ext import commands

Misaki = commands.Bot(command_prefix='|')

@Misaki.event
async def on_ready():
    print("Misaki is working!")

Misaki.run('NzEyMjQzMDQwNzYwMTAyOTky.XsOu7A.6UD4xvWSbWH0LSIy_A8mgFNOEmA')