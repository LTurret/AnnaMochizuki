import discord, json, os
from discord.ext import commands
from discord_slash import SlashCommand

with open ("./json\config.json", mode="r", encoding="utf-8") as config:
    config = json.load(config)

Misaki = commands.Bot(command_prefix = commands.when_mentioned, intents = discord.Intents.all())
slash = SlashCommand(Misaki, sync_commands = True, sync_on_cog_reload = True, override_type = True)
Misaki.remove_command('help')

@Misaki.event
async def on_ready():
    await Misaki.change_presence(status = discord.Status.online, activity = discord.Game('偶像大師 百萬人演唱會！ 劇場時光'))
    print("ㄤ奈可愛")

@Misaki.command()
async def load(ctx, extension):
    await ctx.message.delete()
    Misaki.load_extension(f'cogs.{extension}')
    await ctx.send(f'function **{extension}** loadeded.', delete_after = 5)

@Misaki.command()
async def unload(ctx, extension):
    await ctx.message.delete()
    Misaki.unload_extension(f'cogs.{extension}')
    await ctx.send(f'function **{extension}** unloaded.', delete_after = 5)

@Misaki.command()
async def reload(ctx, extension):
    await ctx.message.delete()
    Misaki.reload_extension(f'cogs.{extension}')
    await ctx.send(f'function **{extension}** reloaded.', delete_after = 5)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        Misaki.load_extension(f'cogs.{filename[:-3]}')

Misaki.run(config['BotToken'])