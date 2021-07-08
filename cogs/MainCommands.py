import discord
import json
import datetime
import random
from discord.ext import commands
from discord.ext.commands import command, Cog #button
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice
from discord_components import DiscordComponents, Button, ButtonStyle, InteractionType

with open (r"C:\Users\a0919\Desktop\Files\Programming\Github\Suspend-bot\json\MainCommands.json", 'r', encoding="utf8") as MainCommandsJson:
    MainCommandsJson = json.load(MainCommandsJson)

class MainCommands(commands.Cog):
    def __init__(self, Misaki):
        self.Misaki = Misaki
        self.RaidMessage = []
        self.RaidCategory = []
        self.RaidVoiceChannel = []
        self.RaidAuthorId = ""
        self.RaidAuthorName = ""
        self.RaidChamberName = ""
        self.RaidEndedSystemCaller = "Idle"
        self.RaidStatus = False
        self.BotSaidFilter = True
        self.OuenResponseHolder = False

    @commands.command()
    async def reply(self, ctx):
        print(ctx)

    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def purge(self, ctx, amount:int):
        await ctx.channel.purge(limit = amount+1)
        await ctx.channel.send(f'{amount} 個訊息已被刪除')

    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def cls(self, ctx, amount:int):
        await ctx.channel.purge(limit = amount+1)

    @commands.command()
    async def botsaid(self, ctx, *,message):
        await ctx.message.delete()
        await ctx.send(message)

    @commands.command()
    async def rgs(self, ctx):
        await ctx.channel.send("RGS is up!")

    @commands.command()
    async def rds(self, ctx, keyword:str, population:int, groups:int):
        HavetheNick = []
        for member in ctx.guild.members:
            if (member.nick != None and member.nick.count(keyword)):
                HavetheNick.append(member.name)
        if (population == 0):
            await ctx.channel.send("人數不可為0！")
        else:
            if (len(HavetheNick) < population * groups):
                    await ctx.channel.send(f'不足以分組。\n請確定人數是否足夠、關鍵字 "{keyword}" 是否更改為暱稱之內。')
            else:
                for iteration in range(groups):
                    ChosenMember = random.sample(HavetheNick, k=population)
                    for RemoveMember in ChosenMember:
                        HavetheNick.remove(RemoveMember)
                    embed = discord.Embed(title = f'第 {iteration+1} 小隊', description = None, colour = 0x93e2df, timestamp = datetime.datetime.utcnow())
                    embed.set_thumbnail(url = MainCommandsJson['Flag_icon'])
                    embed.add_field(name = "隊員", value=f'{ChosenMember}', inline=False)
                    await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self, message):
        #引以為戒
        if (message.content == "星辰" and message.author != self.Misaki.user):
            await message.channel.send("<@!278453052850176000> 你必須引以為戒")


        #明年一定第二
        if (message.content == "明年一定二位" and message.author != self.Misaki.user):
            await message.channel.send("<@!278453052850176000> 不可以食言耶")


        #general - Twitter Mode
        if (message.content.upper().count("TWITTER MODE") and len(message.content) != 12 and message.author != self.Misaki.user):
            await message.add_reaction("❤️")
            await message.add_reaction("🗨️")
            await message.add_reaction("🔁")


        #iM@S
        TriggerPassword = message.content.count('TriggerWebhookConverter')
        if (TriggerPassword == True and message.author.display_name == "音無小鳥"):
            await message.delete()
            await message.channel.send(message.content[24:])


        #Random Group-up System (RGS)
        TriggerRGS = message.content.count("RGS is up!")
        if (TriggerRGS == True and message.author == self.Misaki.user):
            await message.channel.send("Random Group-up System voting is here!")
            await message.add_reaction("🚩")


        #RAS Detector
        RaidDetector = message.content.count("Raid is start soon...")
        if (RaidDetector == True and message.author == self.Misaki.user and self.BotSaidFilter == False):
            self.RaidMessage = message
            await message.edit(content = f"A Raid (:flag_tw:) afk will be starting in 10 seconds by <@{self.RaidAuthorId}>. Prepare to join raiding `{self.RaidAuthorName}'s {self.RaidChamberName}` *Now located above lounge.* **You do not need to react to anything**")
            self.BotSaidFilter = True
            self.RaidEndedSystemCaller = "Stady"
            await message.add_reaction("🔚")

        
        #応援發送器
        if (message.content == "(＊>△<)＜応援ください！" and message.author == self.Misaki.user):
            self.OuenResponseHolder = True
        #応援回應
        if (message.content.count("応援するよ") and self.OuenResponseHolder == True):
            self.OuenResponseHolder = False
            random_emojis = [
                "<:Su01:823936033246806056>",
                "<:Su02:823936042729734195>",
                "<:Su00:823936024865931314>",
                "<:Su03:823936052120911933>",
                "<:Su04:823936062975377448>",
                "<:Su05:823936075847565312>",
                "<:Su15:823936198115590144>"
            ]
            emoji = random_emojis[random.randint(0, 6)]
            await message.channel.send(emoji)
            

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        #ReactionRole
        if (payload.channel_id == 463321768212299778 and payload.message_id == 464825427844792320 and str(payload.emoji) == "<:Serika:677696191772753940>"):
            guild = self.Misaki.get_guild(payload.guild_id)
            role = guild.get_role(711454063962882051)
            await payload.member.add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        #ReactionRole
        if (payload.channel_id == 463321768212299778 and payload.message_id == 464825427844792320 and str(payload.emoji) == "<:Serika:677696191772753940>"):
            guild = self.Misaki.get_guild(payload.guild_id)
            member = guild.get_member(payload.user_id)
            role = guild.get_role(711454063962882051)
            await member.remove_roles(role)

    @commands.command()
    async def button(self, ctx):
        await ctx.send(
            content = "按鈕功能還在開發，目前沒有功能",
            components = [
                Button(
                    label = "按這個會交互失敗",
                    style = 4
                ),
                Button(
                    label = "相關API",
                    style = 5,
                    url = "https://devkiki7000.gitbook.io/discord-components/"
                )
            ]
        )

    @commands.Cog.listener()
    async def on_command_error(self, ctx, exception):
        await ctx.channel.send(exception)      

def setup(Misaki):
    DiscordComponents(Misaki) # button
    Misaki.add_cog(MainCommands(Misaki))