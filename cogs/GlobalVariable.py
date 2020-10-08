import discord
from discord.ext import commands

class GlobalVariable(commands.Cog):
    def __init__(self, reason):
        self.reason = reason
    
    def BotSaidFilter(self, Status, message_id):
        self.Status = Status
        self.message_id = message_id

def setup(Misaki):
    Misaki.add_cog(GlobalVariable(Misaki))