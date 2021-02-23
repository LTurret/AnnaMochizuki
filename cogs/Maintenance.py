import discord
import datetime
import os
from discord.ext import commands

def showcogs(filetype:str):
    for filename in os.listdir("./cogs"):
        if filename.endswith(filetype):
            print(filename)

class Maintenance(commands.Cog):
    def __init__(self, Misaki):
        self.Misaki = Misaki

    @commands.command()
    async def show(self, ctx, filetype:str):
        showcogs(filetype)

def setup(Misaki):
    Misaki.add_cog(Maintenance(Misaki))