import discord
import json
import random
import datetime
from discord import Webhook, RequestsWebhookAdapter
from discord.ext import commands

with open (r"C:\Users\George Rupp\Desktop\Files\Programming\Github\Suspend-bot\json\MainCommands.json", 'r', encoding="utf8") as MainCommandsJson:
    MainCommandsJson = json.load(MainCommandsJson)

class MainCommands(commands.Cog):
    def __init__(self, Misaki):
        self.Misaki = Misaki

    @commands.command()
    async def ping(self, ctx):
        if (round(self.Misaki.latency*1000) >= 100):
            await ctx.send(f'你與我的距離為 {round(self.Misaki.latency*1000)} 毫秒\n有夠遠的')
        else:
            await ctx.send(f'你與我的距離為 {round(self.Misaki.latency*1000)} 毫秒')

    @commands.command()
    async def purge(self, ctx, amount=1):
        doCommand = False
        for MemberRoles in ctx.message.author.roles:
            if (str(MemberRoles) == "Verified Member" and doCommand != True):
                doCommand = True
        if (doCommand == True):
            await ctx.channel.purge(limit=amount+1)
            await ctx.channel.send(f'{amount} 個訊息已被刪除')
        else:
            await ctx.channel.purge(limit=1)
            await ctx.channel.send("您的權限不足使用此指令。")

    @commands.command()
    async def cls(self, ctx, amount=1):
        doCommand = False
        for MemberRoles in ctx.message.author.roles:
            if (str(MemberRoles) == "Verified Member" and doCommand != True):
                doCommand = True
        if (doCommand == True):
            await ctx.channel.purge(limit=amount+1)
        else:
            await ctx.channel.purge(limit=1)

    @commands.command()
    async def botsaid(self, ctx, *,message):
        await ctx.message.delete()
        await ctx.send(message)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        print(payload.emoji)
        if (payload.channel_id == MainCommandsJson['ImformationChannel'] and payload.message_id == MainCommandsJson['Rules'] and str(payload.emoji) == MainCommandsJson['ReactionRole_Emoji']):
            guild = self.Misaki.get_guild(payload.guild_id)
            role = guild.get_role(MainCommandsJson['Verified-Member'])
            await payload.member.add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        if (payload.channel_id == MainCommandsJson['ImformationChannel'] and payload.message_id == MainCommandsJson['Rules'] and str(payload.emoji) == MainCommandsJson['ReactionRole_Emoji']):
            guild = self.Misaki.get_guild(payload.guild_id)
            member = guild.get_member(payload.user_id)
            role = guild.get_role(MainCommandsJson['Verified-Member'])
            await member.remove_roles(role)

    @commands.command()
    async def rds(self, ctx, keyword:str, population:int, groups:int):
        hasNick = []
        for member in ctx.guild.members:
            if member.nick != None and member.nick.count(keyword):
                hasNick.append(member.name)
        if (len(hasNick) <= population * groups):
            await ctx.channel.send(f'不足以分組。\n請確定人數是否足夠、關鍵字 "{keyword}" 是否更改為暱稱之內。')
            pass
        else:
            for iteration in range(groups):
                enum = random.sample(hasNick, k=population)
                for removal in enum:
                    hasNick.remove(removal)
                embed = discord.Embed(title = f'第 {iteration+1} 小隊', description = None, colour = 0x93e2df
                , timestamp = datetime.datetime.utcnow())
                embed.set_thumbnail(url = MainCommandsJson['Flag_icon'])
                embed.add_field(name = "隊員", value=f'{enum}', inline=False)
                await ctx.send(embed=embed)
    
    @commands.command()
    async def JoinInvisibleVC(self, ctx):
        await ctx.message.delete()
        member = ctx.guild.get_member(ctx.message.author.id)
        await member.move_to(ctx.guild.get_channel(MainCommandsJson['InvisibleChannel-Id']))

    @commands.Cog.listener()
    async def on_message(self, message):
        TriggerPassword = message.content.count('TriggerWebhookConverter')
        if (TriggerPassword == True and message.author != self.Misaki.user):
            await message.delete()
            await message.channel.send(message.content[24:])

def setup(Misaki):
    Misaki.add_cog(MainCommands(Misaki))