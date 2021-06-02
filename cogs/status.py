import discord
from discord.ext import commands

class Status(commands.Cog):
    """Commands that change the bot's status.
    Owner only!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def stream(self, ctx):
        """Sets status to Streaming"""
        logchannel = self.bot.get_channel(848362560255950888)
        await self.bot.change_presence(activity=discord.Streaming(name="Doing bot things", url="https://www.youtube.com/watch?v=uVRHh8Jxtp0"), status=discord.Status.dnd)
        await ctx.send("<:status:848563270134792242> - Status changed!", delete_after=5)
        await logchannel.send("<:status:848563270134792242> - Status changed to **`Streaming`**")
    
    @commands.command()
    @commands.is_owner()
    async def dnd(self, ctx):
        """Sets status to Do Not Disturb"""
        logchannel = self.bot.get_channel(848362560255950888)
        await self.bot.change_presence(activity=discord.Game(name="Doing bot things"), status=discord.Status.dnd)
        await ctx.send("<:status:848563270134792242> - Status changed!", delete_after=5)
        await logchannel.send("<:status:848563270134792242> - Status changed to **`Do not Disturb`**")

    @commands.command()
    @commands.is_owner()
    async def idle(self, ctx):
        """Sets status to Idle"""
        logchannel = self.bot.get_channel(848362560255950888)
        await self.bot.change_presence(activity=discord.Game(name="Doing bot things"), status=discord.Status.idle)
        await ctx.send("<:status:848563270134792242> - Status changed!", delete_after=5)
        await logchannel.send("<:status:848563270134792242> - Status changed to **`Idle`**")

    @commands.command()
    @commands.is_owner()
    async def online(self, ctx):
        """Sets status to Online"""
        logchannel = self.bot.get_channel(848362560255950888)
        await self.bot.change_presence(activity=discord.Game(name="Doing bot things"), status=discord.Status.online)
        await ctx.send("<:status:848563270134792242> - Status changed!", delete_after=5)
        await logchannel.send("<:status:848563270134792242> - Status changed to **`Online`**")

    @commands.command()
    @commands.is_owner()
    async def invisible(self, ctx):
        """Sets status to Invisible"""
        logchannel = self.bot.get_channel(848362560255950888)
        await self.bot.change_presence(activity=discord.Game(name="Doing bot things"), status=discord.Status.invisible)
        await ctx.send("<:status:848563270134792242> - Status changed!", delete_after=5)
        await logchannel.send("<:status:848563270134792242> - Status changed to **`Invisible`**")

def setup(bot):
    bot.add_cog(Status(bot))