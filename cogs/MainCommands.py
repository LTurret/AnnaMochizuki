import json, random
from discord.ext import commands

with open("./json/maincommands.json", mode="r", encoding="utf8") as MainCommandsJson:
    MainCommandsJson = json.load(MainCommandsJson)
with open("./json/other.json", mode="r", encoding="utf8") as config_other:
    config_other = json.load(config_other)

class MainCommands(commands.Cog):
    def __init__(self, Misaki):
        self.Misaki = Misaki
        self.OuenResponseHolder = False

    @commands.command()
    async def botsaid(self, ctx, *,message):
        await ctx.message.delete()
        await ctx.send(message)

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
                "<:Su00:882135513539182642>",
                "<:Su01:882135525648117780>",
                "<:Su02:882135536964358184>",
                "<:Su03:882135547395571722>",
                "<:Su04:882135559043170315>",
                "<:Su05:882135571974213682>"
                "<:Su15:882142299528761374>"
            ]
            emoji = random_emojis[random.randint(0, 6)]
            await message.channel.send(emoji)


        # [Other] 你很腦殘嗎
        if (message.content.count("你很腦殘嗎") and message.author != self.Misaki.user):
            await message.channel.send(config_other['AreYouBrainless'])


        # [Other] >:)
        if (message.content.count(">:)") and message.author != self.Misaki.user):
            await message.channel.send(config_other['>:)'])


        # [Other] ㄤ奈可愛
        if (MainCommandsJson["杏奈可愛keywords"].count(message.content) and message.author != self.Misaki.user):
            MemberRoles = message.author.roles
            try:
                if str(MemberRoles).count("THE IDOLM@STER"):
                    print("access")
                    if (str(message.author) == "LTurret#0834"):
                        await message.channel.send("你很噁心... <:AnnaShock:882135258865229894>")
                    else:
                        await message.channel.send("謝謝... 製作人 <:Su04:882135559043170315>💜")
                else:
                    pass
            except Exception as e:
                await message.channel.send(e)


        # [Other] 打上池
        if (message.content.count("打上池") and message.author != self.Misaki.user):
            channel = message.guild.get_channel(474858135853596675)
            reply_message = await channel.fetch_message(885778763932139530)
            if (str(message.author) == "LTurret#0834"):
                await reply_message.reply("https://imgur.com/aMTsmeY")
            else:
                await message.channel.send("不要抽打上池\n<@!278453052850176000> 快點去打165")

        # get information
        # if (message.content.count("get") and message.author != self.Misaki.user):
        #     try:
        #         await message.delete()
        #     except Exception as e:
        #         print(e)
            
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