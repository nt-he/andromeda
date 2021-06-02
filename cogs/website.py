import discord
from discord.ext import commands

class Website(commands.Cog):
    """Commands that contain links to my site and sub-sites"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def main(self, ctx):
        """Main site, has stuff about projects"""
        await ctx.send("https://oscie.tk")

    @commands.command()
    async def cdn(self, ctx):
        """Site I use to host files"""
        await ctx.send("https://cdn.oscie.tk")

    @commands.command()
    async def wiimanual(self, ctx):
        """Wii Menu Manual on a website!"""
        await ctx.send("https://wii.oscie.tk/mini/startup.html")

    @commands.command()
    async def dms(self, ctx):
        """My Discord DM archive"""
        await ctx.send("https://discord.oscie.tk")

    @commands.command()
    async def neun(self, ctx):
        """LOUD: Neun Site"""
        await ctx.send("https://neun.oscie.tk")

    @commands.command()
    async def openletter(self, ctx):
        """Exposing people since 2021"""
        await ctx.send("https://openletter.oscie.tk")

    @commands.command()
    async def siteindex(self, ctx):
        """Index of all the sites"""
        await ctx.send("https://oscie.tk/siteindex")

    

def setup(bot):
    bot.add_cog(Website(bot))