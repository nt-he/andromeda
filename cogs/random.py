import discord
from discord.ext import commands
import os
import random
from discord.ext.commands.converter import EmojiConverter

from discord.ext.commands.errors import CommandRegistrationError
from discord_components import Button
from discord_components.button import ButtonStyle
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
        await ctx.send("This command has (and originally was from) Img.Bot\nhttps://www.thediamondk.com/bot.html")


    @commands.command()
    async def postmii(self, ctx):
        """Posts a Mii to the mii folder"""
        imageName = os.path.join("miis/", f"{ctx.author.id}.png")
        await ctx.message.delete()
        message = await ctx.send(f'Are you sure?', components=[Button(label="No", style=3), Button(label="Yes", style=4)])
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
            await interaction.respond(content="Your Mii was not posted.")
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
    @commands.command()
    async def rainbow_buttons(self, ctx):
        await ctx.send('bruh moment', components=[Button(label=color, style=color, url="https://www.example.com", id=f"std{color}") for color in range(1, 6)])
        await ctx.send('disabled buttons', components=[Button(label=color, style=color, url="https://www.example.com", disabled=True, id=f"disabled{color}") for color in range(1, 6)])
        await ctx.send('emoji buttons', components=[Button(label=color, style=color, url="https://www.example.com", id=f"emoji{color}", emoji=await self.bot.get_guild(783461298531860492).fetch_emoji(832034254565277757)) for color in range(1, 6)])
        try:
            interaction = await self.bot.wait_for("button_click", timeout=5, check=lambda res: res.user.id == ctx.author.id and res.channel.id == ctx.channel.id) 
            # Explanation (for oscie):
            # Wait for a button to be clicked (or error out if the number of seconds waited reaches 5), and make sure that the person pressing the button is the author
        except:
            # The user timed out
            await ctx.send("You timed out")
        if interaction.component.id.startswith("std"):
            # The user pressed a button with the "std" ID we set above.
            # In this case, the standard buttons' IDs start with std
            # so we can tell that a normal button has been pressed
            await interaction.respond(content="You pressed a normal button!") # Respond to the interaction
        if interaction.component.id.startswith("emoji"):
            # The user pressed a button with an emoji
            await interaction.respond(content="You pressed a <:tro:851113675804901396> emoji button")
        # Additionally:
        # In this scenario, for my own convienence, I used a list comprehension
        # List comprehensions look something like this: [int(i) for i in some_random_list] and they allow you
        # to form lists without needing to use .append()
        # Here is a brief explanation:
        # For every value (i) in some_random_list, call int(i) and append the return of that function to the list.
        # So, a list comprehension looks like this:
        # some_random_list = ["1", "2", "3"]
        # intified = [int(i) for i in some_random_list]
        # intified is now [1, 2, 3]
        # However, normally, you should use a normal list:
        # components=[Button(label="You get the idea", style=1)]
def setup(bot):
    bot.add_cog(Random(bot)) 

# Credit TDK for the Mii command