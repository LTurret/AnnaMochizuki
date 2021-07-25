import discord, json, datetime, random
from discord.ext import commands

with open(r"C:\Users\a0919\Desktop\Files\Programming\Github\Suspend-bot\json\MainCommands.json", 'r', encoding="utf8") as MainCommandsJson:
    MainCommandsJson = json.load(MainCommandsJson)
with open(r"C:\Users\a0919\Desktop\Files\Programming\Github\Suspend-bot\json\Other.json", mode="r", encoding="utf8") as config_other:
    config_other = json.load(config_other)

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
    async def botsaid(self, ctx, *,message):
        await ctx.message.delete()
        await ctx.send(message)

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
        # [Other] Twitter Mode
        if (message.content.upper().count("TWITTER MODE") and len(message.content) != 12 and message.author != self.Misaki):
            await message.add_reaction("🗨️")
            await message.add_reaction("🔁")
            await message.add_reaction("❤️")


        # [MLTD] Webhook translator
        TriggerPassword = message.content.count('TriggerWebhookConverter')
        if (TriggerPassword == True and message.author.display_name == "音無小鳥"):
            await message.delete()
            await message.channel.send(message.content[24:])


        # [MLTD] 応援 - 訊息發送器
        if (message.content == "(＊>△<)＜応援ください！" and message.author == self.Misaki.user):
            self.OuenResponseHolder = True


        # [MLTD] 応援 - 回應表情符號
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


        # [Other] 你很腦殘嗎
        if (message.content.count("你很腦殘嗎") and message.author != self.Misaki.user):
            await message.channel.send(config_other['AreYouBrainless'])
            
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        # Member verification system
        if (payload.channel_id == 463321768212299778 and payload.message_id == 464825427844792320 and str(payload.emoji) == "<:Serika:677696191772753940>"):
            guild = self.Misaki.get_guild(payload.guild_id)
            role = guild.get_role(711454063962882051)
            await payload.member.add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        # Member verification system
        if (payload.channel_id == 463321768212299778 and payload.message_id == 464825427844792320 and str(payload.emoji) == "<:Serika:677696191772753940>"):
            guild = self.Misaki.get_guild(payload.guild_id)
            member = guild.get_member(payload.user_id)
            role = guild.get_role(711454063962882051)
            await member.remove_roles(role)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, exception):
        await ctx.channel.send(exception)

def setup(Misaki):
    Misaki.add_cog(MainCommands(Misaki))