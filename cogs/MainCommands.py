import json, random
from discord.ext import commands

with open("./json/maincommands.json", mode="r", encoding="utf8") as MainCommandsJson:
    MainCommandsJson = json.load(MainCommandsJson)
with open("./json/other.json", mode="r", encoding="utf8") as ConfigOther:
    ConfigOther = json.load(ConfigOther)

# Set Anna keyword detect function for shorter programming
def Anna_keyword(message):
    for keyword in MainCommandsJson["杏奈關鍵字"]:
        result = message.upper().count(keyword)
        if (result == 1):
            break
    return result

# Set Serika keyword detect function for shorter programming
def Serika_keyword(message):
    for keyword in MainCommandsJson["星梨花關鍵字"]:
        result = message.upper().count(keyword)
        if (result == 1):
            break
    return result

# Set HOLD-UP keyword detect funcion for shorter programming
def Holdup_keyword(message):
    for keyword in MainCommandsJson["修但幾勒"]:
        result = message.upper().count(keyword)
        if (result == 1):
            break
    return result

class MainCommands(commands.Cog):
    def __init__(self, Anna):
        self.Anna = Anna
        self.OuenResponseHolder = False

    @commands.command()
    async def botsaid(self, ctx, *,message):
        await ctx.message.delete()
        await ctx.send(message)

    @commands.command()
    async def reply(self, ctx, reply_id, *,message):
        await ctx.message.delete()
        reply_message = await ctx.channel.fetch_message(reply_id)
        await reply_message.reply(message)

    @commands.Cog.listener()
    async def on_message(self, message):

        # Global initialization function

        # Shorter condition
        content = message.content
        author = message.author

        # Packaging bot detection
        def not_bot():
            return author != self.Anna.user

        # [Other] Twitter Mode
        if (content.upper().count("TWITTER MODE") and len(content) != 12 and not_bot()):
            await message.add_reaction("🗨️")
            await message.add_reaction("🔁")
            await message.add_reaction("❤️")


        # [MLTD] Webhook translator
        TriggerPassword = content.count('TriggerWebhookConverter')
        if (TriggerPassword == True and author.display_name == "音無小鳥"):
            await message.delete()
            await message.channel.send(content[24:])

        # [MLTD] 応援 - 訊息發送器
        if (content == "(＊>△<)＜応援ください！" and not(not_bot())):
            self.OuenResponseHolder = True

        # [MLTD] 応援 - 回應表情符號
        if (content.count("応援するよ") and self.OuenResponseHolder == True):
            self.OuenResponseHolder = False
            random_emojis = [
                "<:Su00:882135513539182642>",
                "<:Su01:882135525648117780>",
                "<:Su02:882135536964358184>",
                "<:Su03:882135547395571722>",
                "<:Su04:882135559043170315>",
                "<:Su05:882135571974213682>",
                "<:Su15:882142299528761374>"
            ]
            emoji = random_emojis[random.randint(0, 6)]
            await message.channel.send(emoji)




        # [Other] 打上池
        if (content.count("打上池") and not_bot()):
            channel = message.guild.get_channel(474858135853596675)
            reply_message = await channel.fetch_message(885778763932139530)
            if (str(author) == "LTurret#0834"):
                await reply_message.reply("https://imgur.com/aMTsmeY")
            else:
                await message.channel.send("不要抽打上池\n<@!278453052850176000> 快點去打165")

        # [Other] 你很腦殘嗎
        if (content.count("你很腦殘嗎") and not_bot()):
            await message.channel.send(ConfigOther['AreYouBrainless'])

        # [Other] 星梨花要來抓人囉
        if (Serika_keyword(content) and content.count("抓人") and not_bot()):
          url = [
            "https://cdn.discordapp.com/attachments/474858135853596675/898778507482644530/unknown.png",
            "https://media.discordapp.net/attachments/474858135853596675/898607444685627462/unknown.png"
          ]
          await message.channel.send(random.choice(url))




        # [ㄤ奈] >:)
        if (content.count(">:)") and not_bot()):
            await message.channel.send(ConfigOther['>:)'])

        # [ㄤ奈] >:(
        if (content.count(">:(") and not_bot()):
            await message.channel.send(ConfigOther['>:('])

        # [ㄤ奈] ㄤ奈可愛
        if (Anna_keyword(content) and content.count("可愛") and not_bot()):
            MemberRoles = author.roles
            if str(MemberRoles).count("THE IDOLM@STER"):
                if (str(author) == "LTurret#0834"):
                    await message.channel.send("你很噁心... <:AnnaShock:882135258865229894>")
                else:
                    await message.channel.send("謝謝... 製作人 <:Su04:882135559043170315>💜")
            else:
                pass
        
        # [ㄤ奈] 修但幾勒
        if (not_bot() and Holdup_keyword(content)):
            await message.channel.send("https://imgur.com/plUSSmA")
        
        # [ㄤ奈] 我把ㄤ奈救出來了
        if (not_bot() and content == "我把ㄤ奈救出來了"):
            await message.channel.send("：ㄤ奈得救了")

        # [ㄤ奈] ㄤ奈得救了
        if (not_bot() and content == "ㄤ奈得救了"):
            await message.channel.send("：我把ㄤ奈救出來了")

        # [ㄤ奈] 窩不知道
        if (content.count("知道嗎")):
            response = [
              "https://imgur.com/dsZqxeT",
              "https://imgur.com/X03kht3",
              "https://imgur.com/ENUfHlE"
            ]
            response = random.choice(response)
            await message.channel.send(response)

        # [ㄤ奈] 窩不知道
        if (content.count("我是") and Anna_keyword(content)):
            await message.channel.send("你才不是")




        # [Orginization] bad gif delete
        if (content.count("https://tenor.com/view/shut-up-gif-21170155")):
            await message.delete()




        # [Dev tool] try if on_message is still working
        if (content.count("get") and not_bot()):
            try:
                await message.delete()
            except Exception as e:
                print(e)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        # Member verification system
        if (payload.channel_id == 463321768212299778 and payload.message_id == 464825427844792320 and str(payload.emoji) == "<:Serika:677696191772753940>"):
            guild = self.Anna.get_guild(payload.guild_id)
            role = guild.get_role(711454063962882051)
            await payload.member.add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        # Member verification system
        if (payload.channel_id == 463321768212299778 and payload.message_id == 464825427844792320 and str(payload.emoji) == "<:Serika:677696191772753940>"):
            guild = self.Anna.get_guild(payload.guild_id)
            member = guild.get_member(payload.user_id)
            role = guild.get_role(711454063962882051)
            await member.remove_roles(role)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, exception):
        await ctx.channel.send(exception)

def setup(Anna):
    Anna.add_cog(MainCommands(Anna))