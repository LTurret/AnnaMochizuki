import discord, datetime
from discord.ext import commands
from discord.ext.commands.converter import EmojiConverter

class Other(commands.Cog):
    def __init__(self, Misaki):
        self.Misaki = Misaki

    @commands.command()
    async def 乘法公式(self, ctx):
        embed = discord.Embed(title = "乘法公式", description = None, colour = 0x93e2df
        , timestamp = datetime.datetime.utcnow())
        embed.add_field(name = "a²-b²", value = "(a+b)(a-b)", inline = False)
        embed.add_field(name = "a³±b³", value = "(a±b)(a²±ab+b²)", inline = False)
        embed.add_field(name = "(a±b)²", value = "a²±2ab+b²", inline = False)
        embed.add_field(name = "(a+b)³", value = "a³-3a²b+3ab²+b³ \n= a³+b³+3ab(a+b)", inline = False)
        embed.add_field(name = "(a-b)³", value = "a³-3a²b+3ab²-b³ \n= a³-b³-3ab(a-b)", inline = False)
        await ctx.send(embed=embed)

def setup(Misaki):
    Misaki.add_cog(Other(Misaki))