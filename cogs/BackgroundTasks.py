import discord
import asyncio
from discord.ext import commands, tasks

class BackgroundTasks(commands.Cog):
    def __init__(self, Misaki, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.Misaki = Misaki
        self.bg_task = self.Misaki.loop.create_task(self.report_data())

    async def report_data(self):
        await self.Misaki.wait_until_ready()
        channel = self.Misaki.get_channel(695508789327298570)
        while not self.Misaki.is_closed():
            # await channel.send("ㄐㄐ")
            await asyncio.sleep(60)

def setup(Misaki):
    Misaki.add_cog(BackgroundTasks(Misaki))