import json, os

import discord
from discord.ext import commands

with open("./config/token.json", mode="r") as token:
    token = json.load(token)

Anna = commands.Bot(command_prefix=commands.when_mentioned)
Anna.remove_command("help")

@Anna.event
async def on_ready():
    await Anna.change_presence(status = discord.Status.online, activity = discord.Game("偶像大師 百萬人演唱會！ 劇場時光"))
    try:
        os.system("cls")
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

for filename in os.listdir("./cogs/command"):
    if filename.endswith(".py"):
        print(f"Loading commands extension: {filename}")
        Anna.load_extension(f"cogs.command.{filename[:-3]}")

Anna.run(token["token"])
