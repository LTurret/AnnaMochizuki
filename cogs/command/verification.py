import json

from discord.ext import commands

# Unique ids for verification.
with open("./config/unique.json") as unique_ids:
    unique_ids = json.load(unique_ids)

# Server scopes(ids), used for quick switching between production and testing server.
with open("./config/scope.json") as server_scopes:
    server_scopes = json.load(server_scopes)

class constants():
    def __init__(self):
        self.__GUILD:int = server_scopes["Production"]
        self.__CHANNEL_INFORMATION:int = unique_ids["CHANNEL_INFORMATION"]
        self.__MESSAGE:int = unique_ids["MESSAGE"]
        self.__ROLE_MEMBER:int = unique_ids["ROLE_MEMBER"]
        self.__ROLE_NSFW:int = unique_ids["ROLE_NSFW"]

    def id(self, selector:str=""):
        manifest = {
            "info_channel": self.__CHANNEL_INFORMATION,
            "guild": self.__GUILD,
            "msg": self.__MESSAGE,
            "role_member": self.__ROLE_MEMBER,
            "role_nsfw": self.__ROLE_NSFW
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
            
            if emoji == "Serika":
                role = guild.get_role(self.constants.id("role_member"))
                await payload.member.add_roles(role)
            
            if emoji == "YeahBoi":
                role = guild.get_role(self.constants.id("role_nsfw"))
                await payload.member.add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):

        guild = self.Anna.get_guild(self.constants.id("guild"))
        channel = payload.channel_id
        emoji = payload.emoji.name
        msg = payload.message_id

        if channel == self.constants.id("info_channel") and msg == self.constants.id("msg"):

            if emoji == "Serika":
                member = guild.get_member(payload.user_id)
                role = guild.get_role(711454063962882051)
                await member.remove_roles(role)
                
            if emoji == "YeahBoi":
                member = guild.get_member(payload.user_id)
                role = guild.get_role(983712854156935229)
                await member.remove_roles(role)
 

def setup(Anna):
    Anna.add_cog(verification(Anna))