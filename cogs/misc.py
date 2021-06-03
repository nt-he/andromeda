import discord
from discord.enums import NotificationLevel
from discord.ext import commands
import time
import os
import requests
import urllib
import binascii
from bs4 import BeautifulSoup
import datetime

class Misc(commands.Cog):
    """Commands that don't really have a category that fits them."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def invite(self, ctx):
        """Wanna invite my bot? Use this!"""
        await ctx.send("Hey there! Thank you for showing interest into me. To invite me, please use this link:\nhttps://discord.com/api/oauth2/authorize?client_id=848181143169925180&permissions=8&scope=bot")

    @commands.command(hidden=True)
    async def secret(self, ctx):
        """How did you find me?"""
        await ctx.channel.purge(limit=1)
        await ctx.send("Hey you! How the hell did you find me?\nI'm meant to be hiding ya know. Don't let anyone see you sent this kiddo.", delete_after=3)

    @commands.command()
    async def ping(self, ctx):
        """What is my ping?"""
        await ctx.send(f"{round(self.bot.latency * 1000)} ms. Suck on that C#")

    @commands.command()
    @commands.is_owner()
    async def print(self, ctx, *, args):
        """Prints to terminal"""
        await ctx.channel.purge(limit=1)
        await ctx.send("Sent to console.\n**```" + "".join(args) + "```**", delete_after=5)
        print("".join(args))

    @commands.command()
    @commands.has_permissions(manage_guild=True, manage_messages=True)
    async def say(self, ctx, *, args):
        """Repeats what you tell it to"""
        await ctx.channel.purge(limit=1)
        await ctx.send("".join(args))
        print(f"{ctx.author} said {ctx.content}")

    @commands.Cog.listener()
    async def on_message(self, message):
        """For LNH - Returns 'sans pee pee' when it is said"""
        lnhsanschan = 704391659093360762
        if message.channel.id != lnhsanschan:
            return
        else:
            if message.content == "sans pee pee":
                await message.send("sans pee pee")

    @commands.command()
    async def mii(self, ctx, entry_number):
        """Gets a Mii with a CMOC code"""
        global data
        link = requests.get(f"https://miicontestp.wii.rc24.xyz/cgi-bin/htmlsearch.cgi?query={entry_number}").text
        bs = BeautifulSoup(link, "html.parser")
        for file in bs.find("a"), range(1):
            try:
                data = file.get("href")
            except AttributeError:
                pass

        urllib.request.urlretrieve(data, "./cmoc.mii")
        with open("./cmoc.mii", "rb") as f:
            content = f.read()

        data = binascii.hexlify(content)
        data = str(data)
        m, k = data.split("'", 1)
        k = k.strip("'")
        await ctx.send("The Mii you asked for:")
        await ctx.send("https://miicontestp.wii.rc24.xyz/cgi-bin/render.cgi?data={k}")
        os.remove("./cmoc.mii")
    @mii.error
    async def mii_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please send a CMOC code. Get one from https://miicontestp.wii.rc24.xyz")
    
    @commands.command()
    async def suggest(self, ctx, *, suggestion):
        """Give me a suggestion for my site. Please specify what the suggestion is for."""
        await ctx.message.delete()
        await ctx.send("Sent suggestion to <#844365106317099038>", delete_after=5)
        meta = self.bot.get_channel(844365106317099038)
        embed = discord.Embed(color=discord.Color.blurple(), description=suggestion, timestamp=datetime.datetime.today())
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await meta.send("<@729135459405529118>", embed=embed)

def setup(bot):
    bot.add_cog(Misc(bot))