import discord
import json
import os
from discord.ext import commands
# from discord_slash import SlashCommand, SlashCommandOptionType, SlashContext

with open (r"C:\Users\a0919\Desktop\Files\Programming\Github\Suspend-bot\json\setting.json", 'r', encoding='utf8') as jsonSetting:
    jdata = json.load(jsonSetting)

Misaki = commands.Bot(command_prefix=commands.when_mentioned, description="大家的事務員-青羽美咲")
Misaki.remove_command('help')
# slash = SlashCommand(Misaki, auto_register = True)


@Misaki.event
async def on_ready():
    await Misaki.change_presence(status = discord.Status.online, activity = discord.Game('偶像大師 百萬人演唱會！ 劇場時光'))
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

Misaki.run(jdata['BotToken'])