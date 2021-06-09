import discord
from discord.enums import ChannelType, NotificationLevel
from discord.ext import commands
import time
import os
import requests
import urllib
import binascii
from bs4 import BeautifulSoup
import datetime
import io
import contextlib
import textwrap
from traceback import format_exception 

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
    @commands.has_permissions(manage_guild=True, manage_messages=True)
    async def say(self, ctx, *, args):
        """Repeats what you tell it to"""
        await ctx.channel.purge(limit=1)
        await ctx.send("".join(args))
        print(f"{ctx.author} said {ctx.content}")

    @commands.command()
    async def cmoc(self, ctx, entry_number):
        """Gets a Mii with a CMOC code"""
        global data
        link = requests.get(f"https://miicontestp.wii.rc24.xyz/cgi-bin/htmlsearch.cgi?query={entry_number}").text
        bs = BeautifulSoup(link, "html.parser")
        for file in bs.find("a"), range(1):
            try:
                data = file.get("href")
            except AttributeError:
                pass

        urllib.request.urlretrieve(data, "cmoc.mii")
        with open("cmoc.mii", "rb") as f:
            content = f.read()

        data = binascii.hexlify(content)
        data = str(data)
        m, k = data.split("'", 1)
        k = k.strip("'")
        await ctx.send("The Mii you asked for:")
        await ctx.send("https://miicontestp.wii.rc24.xyz/cgi-bin/render.cgi?data={k}")
        os.remove("cmoc.mii")
    @cmoc.error
    async def mii_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please send a CMOC code. Get one from https://miicontestp.wii.rc24.xyz")
    
    @commands.command()
    async def suggest(self, ctx, *, suggestion):
        """Give me a suggestion for my site, twitch, bot or server. Please specify what the suggestion is for."""
        await ctx.message.delete()
        await ctx.send("Sent suggestion to <#844365106317099038>", delete_after=5)
        meta = self.bot.get_channel(844365106317099038)
        embed = discord.Embed(color=discord.Color.blurple(), description=suggestion, timestamp=datetime.datetime.today())
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await meta.send("<@729135459405529118>", embed=embed)

    @commands.command()   
    async def guildinfo(self, ctx):
        """Get information on the Server you are in."""
        if ctx.message.guild == None:
            await ctx.send("I can only do this in servers.")
            return
        name = str(ctx.guild.name)
        desc = str(ctx.guild.description)
        createdtime = ctx.guild.created_at.strftime("%d/%m/%Y - %H:%M:%S")
        shardid = str(ctx.guild.shard_id)
        owner = str(ctx.guild.owner)
        id = str(ctx.guild.id)
        region = str(ctx.guild.region)
        memberCount = str(ctx.guild.member_count)
        boostamount = str(ctx.guild.premium_subscription_count)
        boostlevel = str(ctx.guild.premium_tier)
        icon = str(ctx.guild.icon_url)
        mfalevel = str(ctx.guild.mfa_level)
        notifications = str(ctx.guild.default_notifications)
        systemchan = str(ctx.guild.system_channel)
        maxmembers = str(ctx.guild.max_members)

        if notifications == "NotificationLevel.all_messages":
            notificationsstr = "All Messages"
        elif notifications == "NotificationLevel.only_mentions":
            notificationsstr = "Mentions Only"

        if region == "europe":
            region = ":flag_eu: Europe"
        elif region == "us-west":
            region = ":flag_us: US West"

        if boostlevel == "1":
            boostlevelstr = "Tier 1"
        elif boostlevel == "2":
            boostlevelstr = "Tier 2"
        elif boostlevel == "3":
            boostlevelstr = "Tier 3"
        else:
            boostlevelstr = "Tier 0"

        if boostamount == "1":
            boostsuffix = " Boost"
        else:
            boostsuffix = " Boosts"

        if mfalevel == "1":
            mfalevelstr = "Verification On"
        else:
            mfalevelstr = "No Verification"

        embed1 = discord.Embed(title=f"{name} Server Information", description=desc, color=discord.Color.blurple())
        embed1.set_thumbnail(url=icon)

        embed1.add_field(name="Owner", value=owner, inline=True)
        embed1.add_field(name="Server ID", value=id, inline=True)
        embed1.add_field(name="Member Count", value=memberCount, inline=True)
        embed1.add_field(name="Created at:", value=createdtime)
        embed1.add_field(name="Boost Level", value=boostlevelstr)
        embed1.add_field(name="Shard ID", value=shardid)
        embed1.add_field(name="Boost Count", value=boostamount + boostsuffix)
        embed1.add_field(name="2FA Verification", value=mfalevelstr)
        embed1.add_field(name="Notification Settings", value=notificationsstr)
        embed1.add_field(name="System Channel", value="#" + systemchan)
        embed1.add_field(name="Max Members", value=maxmembers, inline=True)
        await ctx.send(embed=embed1)


    @commands.command()
    async def credits(self, ctx):
        """Credits ig idk"""
        pfp = self.bot.user.avatar_url
        embed = discord.Embed(color=discord.Color.random(), title="Credits", description="People who I've stolen code from, taken ideas from or have helped me in development.")
        embed.set_author(name="oscie bot 3", icon_url=pfp)
        embed.add_field(name="People", value=f"""
        <@667563245107937297> - Helped me with time formatting, stole a couple commands from them
        <@650819889434591241> - Assisted me alot with errors and when I couldn't figure out the most stupidest shit ever and got buttons and other stuff working
        <@302271402277339146> - [Took a couple ideas from them (sorry btw)](https://www.thediamondk.com/bot.html)
        https://discord.gg/dpy - People there helped me quite a bit
        <@729135459405529118> - My creator, who coded me
        <@264081339316305920> - Telling me how much Python sucks
        <@314142411247058946> - Helping me test some commands
        {ctx.author.mention} - You, for using me""")
        await ctx.send(embed=embed)

    @commands.command()
    async def userremind(self, ctx, *, content):
        await ctx.message.delete()
        await ctx.send("Sent suggestion to <#821432334317912125>", delete_after=5)
        chatchann = self.bot.get_channel(821432334317912125)
        embed = discord.Embed(color=discord.Color.blurple(), description=content, timestamp=datetime.datetime.today())
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await chatchann.send(ctx.author.mention, embed=embed)
    

def setup(bot):
    bot.add_cog(Misc(bot))