import asyncio
import discord
from discord.ext import commands

class eCDP(commands.Cog):
    """eCDP Guides but in Discord!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def sochashbrowns(ctx):
        """Hash Browns SELFCHECK"""
        embed = discord.Embed(color=0x7289DA)
        embed.set_author(name="made by oscie - ecdp guides", icon_url="https://oscie.tk/assets/logo.png")
        embed.add_field(
            name="Important!",
            value="All of these answers are meant to be used with a phone with the camera on Google Translate, "
                "as these were taken directly from it. They are not accurate AT ALL but they work flawlessly "
                "with a phone like how it was made.\n\n",
            inline=False
        )
        embed.add_field(
            name="Question Contains\n",
            value="What do you use for packaging\n\nWhat do customers expect\n\nHow long do hashbrowns go in the fryer\n\n"
                "How long do you drain the oil\n\nWhat temperature is the fryer\n\n"
                "What is the holding time of hashbrowns\n\nChoose the six non-enemy oils\n\n"
                "What do you use to clean the station\n\nWhat does it mean to remove the fried\n\n"
                "How many can be placed in the basket"
        )
        embed.add_field(
            name="Answer Contains\n",
            value="Tongs\n\nGolden Brown\n\n2:45+5\n\n5-10s\n\n182°C\n\n10\n\nSkimming\n\nDry Wiper\n\nSkimming\n\n8 Pieces"
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def socfries(ctx):
        """Fries SELFCHECK"""
        embed = discord.Embed(color=0x7289DA)
        embed.set_author(name="made by oscie - ecdp guides", icon_url="https://oscie.tk/assets/logo.png")
        embed.add_field(
            name="Important!",
            value="All of these answers are meant to be used with a phone with the camera on Google Translate, "
                "as these were taken directly from it. They are not accurate AT ALL but they work flawlessly with "
                "a phone like how it was made.\n\n",
            inline=False
        )
        embed.add_field(
            name="Question Contains\n",
            value="How many seconds do the next baskets\n\nIf potato is on floor, use [] to pick up\n\n"
                "When sprinkling salt on fries\n\nExpectations for potatoes\n\nUse special gloves, an apron and []\n\n"
                "How many baskets should one bag\n\nHow long does it take to make potato\n\n"
                "Choose the six non-enemy oils\n\nWhere to store potato bags\n\nWhat is the temp of the fryer"
        )
        embed.add_field(
            name="Answer Contains\n",
            value="30 Seconds\n\nLarge Tongs\n\nTriple Arch\n\nTexture\n\nFace Shield\n\n4\n\n2:55+5\n\n"
                "Nutrients `(3 Chars)`\n\nPotato Freezer\n\n168°C"
        )
        await ctx.send(embed=embed)
    
    @commands.command()
    async def socfoodsafety(ctx):
        """Food Safety SELFCHECK"""
        embed = discord.Embed(color=0x7289DA)
        embed.set_author(name="made by oscie - ecdp guides", icon_url="https://oscie.tk/assets/logo.png")
        embed.add_field(name="Important!", value="All of these answers are meant to be used with a phone with the camera on Google Translate, as these were taken directly from it. They are not accurate AT ALL but they work flawlessly with a phone like how it was made.\n\n", inline=False)
        embed.add_field(name="Question Contains\n", value="3 Principles of food poisoning prevention\n\nCentimetres from the floor\n\nWhat temp should frozen products be\n\n10:1 Burger\n\nNot necessary to prevent secondary\n\nWhat temp should refrigerated items be\n\nNot correct hand wash\n\nWhat is cross-contamination\n\nWhat causes food safety compromisation\n\nWhat is not standard measure")
        embed.add_field(name="Answer Contains\n", value="Do not increase\n\n15cm\n\n-18°C\n\n69°C\n\nCheck Schedule\n\n4°C\n\nRub with arms crossed\n\nSecondary Pollution\n\nAll display items\n\n\nContact me when late")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(eCDP(bot))