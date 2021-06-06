import discord
from discord.ext import commands
import os
import random

from discord.ext.commands.errors import CommandRegistrationError
from discord_components import Button
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
        await ctx.message.delete()
        message = await ctx.send(f'Are you sure?', components=[Button(label="No"), Button(label="Yes")])
        try:
            interaction = await self.bot.wait_for("button_click", timeout=5, check=lambda res: res.user.id == ctx.author.id and res.channel.id == ctx.channel.id)
        except:
            await ctx.send("You timed out and your sandwich was not posted.")
        if interaction.component.label == "Yes":
            await interaction.respond(content="Posted your sandwich")
            await ctx.message.attachments[0].save(imageName)
            await message.delete()
        if interaction.component.label == "No":
            await interaction.respond(content="Your sandwich was not posted.")
            await message.delete()


    @commands.command()
    async def postmii(self, ctx):
        """Posts a Mii to the mii folder"""
        imageName = os.path.join("miis/", f"{ctx.author.id}.png")
        await ctx.message.delete()
        message = await ctx.send(f'Are you sure?', components=[Button(label="No"), Button(label="Yes")])
        try:
            interaction = await self.bot.wait_for("button_click", timeout=5, check=lambda res: res.user.id == ctx.author.id and res.channel.id == ctx.channel.id)
        except:
            await ctx.send("You timed out and your Mii was not posted.")
            await message.delete()
        if interaction.component.label == "Yes":
            await interaction.respond(content="Posted your Mii")
            await ctx.message.attachments[0].save(imageName)
            await message.delete()
        if interaction.component.label == "No":
            await interaction.respond(content="Your sandwich was not Mii.")
            await message.delete()
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