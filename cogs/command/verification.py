import json

from os import getenv

from discord.ext import commands

class constants():
    def __init__(self):
        self.__GUILD:int = getenv("Production")
        self.__CHANNEL_INFORMATION:int = getenv("CHANNEL_INFORMATION")
        self.__MESSAGE:int = getenv("MESSAGE")
        self.__ROLE_MEMBER:int = getenv("ROLE_MEMBER")

    def id(self, selector:str=""):
        manifest = {
            "info_channel": self.__CHANNEL_INFORMATION,
            "guild": self.__GUILD,
            "msg": self.__MESSAGE,
            "role_member": self.__ROLE_MEMBER
        }
        return manifest[selector]

class verification(commands.Cog):
    def __init__(self, Anna):
        self.constants = constants()
        self.Anna = Anna

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):

        guild = self.Anna.get_guild(self.constants.id("guild"))
        channel = payload.channel_id
        emoji = payload.emoji.name
        msg = payload.message_id

        if channel == self.constants.id("info_channel") and msg == self.constants.id("msg"):
            
            if emoji == "✅":
                role = guild.get_role(self.constants.id("role_member"))
                await payload.member.add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):

        guild = self.Anna.get_guild(self.constants.id("guild"))
        channel = payload.channel_id
        emoji = payload.emoji.name
        msg = payload.message_id

        if channel == self.constants.id("info_channel") and msg == self.constants.id("msg"):

            if emoji == "✅":
                member = guild.get_member(payload.user_id)
                role = guild.get_role(711454063962882051)
                await member.remove_roles(role)

async def setup(Anna):
    await Anna.add_cog(verification(Anna))