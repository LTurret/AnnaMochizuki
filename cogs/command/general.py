from discord.ext import commands


class general(commands.Cog):
    def __init__(self, Anna):
        self.Anna = Anna


    @commands.command()
    async def botsaid(self, ctx, *,message):
        await ctx.message.delete()
        await ctx.send(message)

    @commands.command()
    async def reply(self, ctx, reply_id, *,message):
        await ctx.message.delete()
        reply_message = await ctx.channel.fetch_message(reply_id)
        await reply_message.reply(message)
    
    @commands.has_permissions(manage_messages=True)
    @commands.command()
    async def cls(self, ctx, amount: int):
        await ctx.message.delete()
        if amount > 10:
            await ctx.send("訊息數量`>10`請分批執行")
        else:
            await ctx.channel.purge(limit=amount)

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"延遲時間為： {(self.Anna.latency)*1000:.1f} ms")


def setup(Anna):
    Anna.add_cog(general(Anna))