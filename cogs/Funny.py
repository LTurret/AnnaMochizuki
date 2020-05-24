import discord
import json
from discord.ext import commands

with open (r"C:\Users\George Rupp\Desktop\Files\Programming\Github\Suspend-bot\json\setting.json", 'r', encoding='utf8') as jsonSetting:
    jdata = json.load(jsonSetting)

class Funny(commands.Cog):
    def __init__(self, Misaki):
        self.Misaki = Misaki

    @commands.Cog.listener()
    async def on_message(self, message):
        #if message.content == '一根手指':
            #await message.channel.send('5000塊')
        #elif message.content in jdata['keywordOfZhen']:
            #await message.channel.send('鄭順謙')
        if message.content in jdata['keywordOfSu']:
            await message.channel.send('<@493622381554827274>')

def setup(Misaki):
    Misaki.add_cog(Funny(Misaki))