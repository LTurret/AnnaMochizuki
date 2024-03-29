import asyncio
import json

from dotenv import load_dotenv
from os import getenv
from os import listdir
from os import system

import discord

from discord.ext import commands

load_dotenv()

intents = discord.Intents.all()
intents.members = True
intents.messages = True
intents.message_content = True

Anna = commands.Bot(command_prefix=commands.when_mentioned, intents=discord.Intents.all())
Anna.remove_command("help")

@Anna.event
async def on_ready():
    await Anna.change_presence(status = discord.Status.online, activity = discord.Game("偶像大師 百萬人演唱會！ 劇場時光"))
    try:
        system("clear")
    except Exception as _:
        pass
    print(f"Enter pleasure!!")

@Anna.command()
async def load(ctx, extension):
    await ctx.message.delete()
    Anna.load_extension(f"cogs.command.{extension}")
    await ctx.send(f"function **{extension}** loadeded.", delete_after = 5)

@Anna.command()
async def unload(ctx, extension):
    await ctx.message.delete()
    Anna.unload_extension(f"cogs.command.{extension}")
    await ctx.send(f"function **{extension}** unloaded.", delete_after = 5)

@Anna.command()
async def reload(ctx, extension):
    await ctx.message.delete()
    Anna.reload_extension(f"cogs.command.{extension}")
    await ctx.send(f"function **{extension}** reloaded.", delete_after = 5)

async def main():
    async with Anna:
        for filename in listdir("./cogs/command"):
            if filename.endswith(".py"):
                print(f"Loading commands extension: {filename}")
                await Anna.load_extension(f"cogs.command.{filename[:-3]}")
        await Anna.start(getenv("BOT_TOKEN"))

asyncio.run(main())