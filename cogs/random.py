import discord
from discord.ext import commands
import os
import random

from discord.ext.commands.errors import CommandRegistrationError

class Random(commands.Cog):
    """Stuff so random that it cant be in misc"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def sandwich(self, ctx, *args):
        """Gets a random sandwich"""
        image = os.listdir('sandwiches/')
        imgString = random.choice(image)  # Selects a random element from the list
        path = "sandwiches/" + imgString
        await ctx.send((imgString), file=discord.File(path))
    
    @commands.command()
    async def postsandwich(self, ctx, *, arg):
        """Posts a sandwich to the sandwich folder"""
        imageName = os.path.join('sandwiches/', f"{arg}.png")
        await ctx.message.attachments[0].save(imageName)
        await ctx.message.delete()
        await ctx.send(f'Posted your sandwich', delete_after=5)
        logchannel = self.bot.get_channel(848362560255950888)
        await logchannel.send(f"<:empty:848375084577325068> - A sandwich was added to the sandwich folder (`{imageName}`)")

    @commands.command()
    async def postmii(self, ctx):
        """Posts a mii to the mii folder"""
        imageName = os.path.join("miis/", f"{ctx.author.id}.png")
        await ctx.message.attachments[0].save(imageName)
        await ctx.message.delete()
        await ctx.send(f'Posted your mii', delete_after=5)
        logchannel = self.bot.get_channel(848362560255950888)
        await logchannel.send(f"<:empty:848375084577325068> - A mii was added to the mii folder (`{imageName}`)")
    @commands.command()
    async def mii(self, ctx, user: discord.User):
        """Get's a user's Mii."""
        try:
            mii = discord.File(os.path.join("miis/", f"{user.id}.png"))
        except:
            await ctx.send("That person doesn't have a Mii!")
        embed = discord.Embed(title="The Mii you Requested", colour=discord.Colour(0xba151b), description=f"Here is <@{user.id}>'s Mii")
        embed.set_image(url=f"attachment://{user.id}.png")
        await ctx.send(embed=embed, file=mii)
        
def setup(bot):
    bot.add_cog(Random(bot)) 

# Credit TDK for the Mii command