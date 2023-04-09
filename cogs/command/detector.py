from discord.ext import commands

class detector(commands.Cog):
    def __init__(self, Anna):
        self.Anna = Anna

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.count("https://www.dcard.tw/"):
            await message.channel.send("低能卡注意")

        if message.content.count("https://www.tiktok.com/"):
            await message.channel.send("沒爸媽注意")

async def setup(Anna):
    await Anna.add_cog(detector(Anna))
