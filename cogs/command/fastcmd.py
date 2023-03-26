import json

from discord.ext import commands

class fastcmd(commands.Cog):
    def __init__(self, Anna):
        self.Anna = Anna


    @commands.Cog.listener()
    async def on_message(self, message):
        content = message.content
        threads = {
            "imas": 672685805525008414,
            "nsfw": 983712854156935229,
            "meme": 1081248335710654524,
            "art": 1023609569529823273,
            "cs": 712240674337980486,
            "ip": 1075816300514902138
        }

        def not_bot() -> bool:
            return message.author != self.Anna.user

        def slashing() -> bool:
            return content[:1] == "j" and content[1:2] == "/"

        if not_bot() and slashing():
            target = content[2:]
            target_role = message.guild.get_role(threads[target])
            if any(list(map(lambda role: role==target_role, message.author.roles))):
                await message.author.remove_roles(target_role)
            else:
                await message.author.add_roles(target_role)
            
            await message.delete()

async def setup(Anna):
    await Anna.add_cog(fastcmd(Anna))