from discord.ext import commands

class voice(commands.Cog):
    def __init__(self, Anna):
        self.Anna = Anna

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if before.channel is None and after.channel is not None:
            if after.channel.id == 340094920524038146:
                print(member)

def setup(Anna):
    Anna.add_cog(voice(Anna))
