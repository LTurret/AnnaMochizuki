from discord.ext import commands

class misc(commands.Cog):
    def __init__(self, Anna):
        self.Anna = Anna


    @commands.command()
    async def isthissammoo(self, ctx, user_identification: int):
        await ctx.message.delete()

        sammoo_hashmap = {
            "a": 1,
            "s": 1,
            "m": 2,
            "o": 2
        }
        hashmap = {
            "a": 0,
            "s": 0,
            "m": 0,
            "o": 0
        }

        guild = ctx.guild
        member = await guild.fetch_member(user_identification)

        await ctx.send(f"> 正在檢查 `{member.display_name}` 是不是 `sammoo`")

        for char in member.display_name:
            if (char.lower() in hashmap):
                hashmap[char] += 1

        def so_is_it():
            for letter in ["a", "s", "m", "o"]:
                if hashmap[letter] < sammoo_hashmap[letter]:
                    return "不是"
            return "**是**"

        result = so_is_it()
        await ctx.send(result)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, exception):
        await ctx.send("看起來你指令打錯惹")
        if isinstance(exception, commands.BadArgument):
            await ctx.send("請使用 `使用者ID` 來檢查：`~isthissammoo [使用者ID]`")


def setup(Anna):
    Anna.add_cog(misc(Anna))