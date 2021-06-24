from discord.ext import commands

class Testing(commands.Cog):
    """This cog listens for updates and then does stuff.
    It mostly prints it to my logging channel but thats really it."""

    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def globaltest1(self, ctx):
        global testingvar
        testingvar = "globaltest1"

        await ctx.send(testingvar)

    @commands.command()
    async def globaltest2(self, ctx):
        await ctx.send(testingvar)

def setup(bot):
    bot.add_cog(Testing(bot))