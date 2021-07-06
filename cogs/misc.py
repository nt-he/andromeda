import discord
import os
import requests
import urllib
import binascii
import datetime
import wikipedia

from bs4 import BeautifulSoup
from discord.ext import commands

from traceback import format_exception


class Misc(commands.Cog):
    """Commands that don't really have a category that fits them."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True)
    async def secret(self, ctx):
        """How did you find me?"""
        await ctx.channel.purge(limit=1)
        await ctx.send("Hey you! How the hell did you find me?\nI'm meant to be hiding ya know. Don't let anyone see you sent this kiddo.", delete_after=3)

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
        elif region == "us-central":
            region = ":flag_us: US Central"

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
    async def remind(self, ctx, *, content):
        """Sends a message in my server to remind me"""
        await ctx.message.delete()
        if ctx.author.id == 729135459405529118:
            await ctx.send("Sent suggestion to <#844365106317099038>", delete_after=5)
            remindchann = self.bot.get_channel(844365106317099038)
            embed = discord.Embed(color=discord.Color.blurple(), description=content, timestamp=datetime.datetime.today())
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await remindchann.send("<@729135459405529118>", embed=embed)
        else:
            await ctx.send("Sent suggestion to <#821432334317912125>", delete_after=5)
            chatchann = self.bot.get_channel(821432334317912125)
            embed = discord.Embed(color=discord.Color.blurple(), description=content, timestamp=datetime.datetime.today())
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            await chatchann.send(ctx.author.mention, embed=embed)

    @commands.command()
    async def repeat(self, ctx, times: int, *, content):
        """Send something many times"""
        await ctx.message.delete()
        count = 0
        if times == 1:
            r = "."
        else:
            r = "s."
        #if times > 5 and discord.Permissions.manage_messages not in ctx.author:
        #    await ctx.send(f"{ctx.author.mention} You do not have `MANAGE_MESSAGES` so you cannot send more than 5 messages at a time.")
        #    return
        while count < times:
            count = count + 1
            await ctx.send(content)
        logchannel = self.bot.get_channel(854010015199133727)
        await logchannel.send(f"<:invitesub:848556391337558017> {ctx.author} ran the `repeat` command and sent `{content}` `{times}` time{r}")

    @commands.command()
    async def roleme(self, ctx, type, *role):
        """Gives you a role (nt,he only)"""
        if type == None:
            await ctx.send("You need to give a type. 'List', 'Add' and 'Remove'")
            return
        if role == None:
            await ctx.send("You forgot a role, run `o.roleme list`")
            return
        if ctx.guild == 804449200921509913:
            await ctx.send("This command can only be ran in nt,he")
            return

        member = ctx.author
        botupdatesrole = discord.utils.get(ctx.guild.roles, name="bot updates")
        contentupdatesrole = discord.utils.get(ctx.guild.roles, name="content updates")
        serverupdatesrole = discord.utils.get(ctx.guild.roles, name="server updates")
        ereviverole = discord.utils.get(ctx.guild.roles, name="e revive")
        everybodyvotesrole = discord.utils.get(ctx.guild.roles, name="everybody votes")
        musiddjrole = discord.utils.get(ctx.guild.roles, name="dj")
        vcpartyrole = discord.utils.get(ctx.guild.roles, name="vc party")

        if type == "list":
            await ctx.send("""```
Here is a list of roles that o.roleme can give you.
no thoughts, head empty only

  botupdates       Get Updates on the bot
  contentupdates   I ping this when I stream
  serverupdates    Major Server updates cause this ping
  erevive          Revive #e, never used lol
  everybodyvotes   To be honest, I just use #updates
  musicdj          Lets you have more control over music
  vcparty          If we all have a VC, join us!

Type o.help for a list of commands.
Use this command with "o.roleme add" or "o.roleme remove"
                ```""")

        elif type == "add":
            if role == None:
                await ctx.send("You need to pick a role. Use `o.roleme list` to see all.")
                return
            elif role == "botupdates":
                if botupdatesrole in member.roles:
                    await ctx.send(f"You already have this role.")
                    return
                await member.add_roles(botupdatesrole)
                await ctx.send("You have been given the role `bot updates`!")
            elif role == "contentupdates":
                if botupdatesrole in member.roles:
                    await ctx.send("You already have this role.")
                    return
                await member.add_roles(contentupdatesrole)
                await ctx.send("You have been given the role `content updates`!")
            elif role == "serverupdates":
                if serverupdatesrole in member.roles:
                    await ctx.send("You already have this role.")
                    return
                await member.add_roles(serverupdatesrole)
                await ctx.send("You have been given the role `server updates`!")
            elif role == "erevive":
                if ereviverole in member.roles:
                    await ctx.send("You already have this role.")
                    return
                await member.add_roles(ereviverole)
                await ctx.send("You have been given the role `e revive`!")
            elif role == "everybodyvotes":
                if everybodyvotesrole in member.roles:
                    await ctx.send("You already have this role.")
                    return
                await member.add_roles(everybodyvotesrole)
                await ctx.send("You have been given the role `everybody votes`!")
            elif role == "musicdj":
                if musiddjrole in member.roles:
                    await ctx.send("You already have this role.")
                    return
                await member.add_roles(musiddjrole)
                await ctx.send("You have been given the role `dj`!")
            elif role == "vcparty":
                if vcpartyrole in member.roles:
                    await ctx.send("You already have this role.")
                    return
                await member.add_roles(vcpartyrole)
                await ctx.send("You have been given the role `vc party`!")

        elif type == "remove":
            if role == None:
                await ctx.send("You need to pick a role. Use `o.roleme list` to see all.")
                return
            elif role == "botupdates":
                if botupdatesrole not in member.roles:
                    await ctx.send(f"You dont have this role.")
                    return
                await member.add_roles(botupdatesrole)
                await ctx.send("The role `bot updates` has been removed.")
            elif role == "contentupdates":
                if botupdatesrole not in member.roles:
                    await ctx.send("You dont have this role.")
                    return
                await member.add_roles(contentupdatesrole)
                await ctx.send("The role `content updates` has been removed.")
            elif role == "serverupdates":
                if serverupdatesrole not in member.roles:
                    await ctx.send("You dont have this role.")
                    return
                await member.add_roles(serverupdatesrole)
                await ctx.send("The role `server updates` has been removed.")
            elif role == "erevive":
                if ereviverole not in member.roles:
                    await ctx.send("You dont have this role.")
                    return
                await member.add_roles(ereviverole)
                await ctx.send("The role `e revive` has been removed.")
            elif role == "everybodyvotes":
                if everybodyvotesrole not in member.roles:
                    await ctx.send("You dont have this role.")
                    return
                await member.add_roles(everybodyvotesrole)
                await ctx.send("The role `everybody votes` has been removed.")
            elif role == "musicdj":
                if musiddjrole not in member.roles:
                    await ctx.send("You dont have this role.")
                    return
                await member.add_roles(musiddjrole)
                await ctx.send("The role `dj` has been removed.")
            elif role == "vcparty":
                if vcpartyrole not in member.roles:
                    await ctx.send("You dont have this role.")
                    return
                await member.add_roles(vcpartyrole)
                await ctx.send("The role `vc party` has been removed.")

    @commands.command(aliases=["tryitandsee", "tryit"])
    async def tias(self, ctx):
        await ctx.message.delete()
        await ctx.send("https://tryitands.ee/")

    
    #roleme list
    #roleme add
    #roleme remove

    
    @commands.command(description="Posts your Mii to the Mii folder.\nThis will upload your Mii as a png to a folder where someone can run 'o.mii <ping>' and find your Mii")
    async def postmii(self, ctx):
        """Posts a Mii to the mii folder"""
        imageName = os.path.join("miis/", f"{ctx.author.id}.png")
        await ctx.message.delete()

        await ctx.send(content="Posted your Mii", delete_after=5)
        await ctx.message.attachments[0].save(imageName)
            
    @commands.command()
    async def mii(self, ctx, user: discord.User):
        """Get's a user's Mii."""
        if user is None:
            user = ctx.author.id
        try:
            mii = discord.File(os.path.join("miis/", f"{user.id}.png"))
        except:
            await ctx.send("That person doesn't have a Mii!")
            return
        embed = discord.Embed(title="The Mii you Requested", colour=discord.Colour(0xba151b), description=f"Here is <@{user.id}>'s Mii")
        embed.set_image(url=f"attachment://{user.id}.png")
        await ctx.send(embed=embed, file=mii)

    @commands.command()
    async def website(self, ctx):
        """Get a Website Index"""
        await ctx.send("remind me to do this")

    @commands.command()
    async def wikipedia(self, ctx, *, query : str):
        result = wikipedia.page(query)
        await ctx.send(result.summary)

    @commands.command()
    async def google(self, ctx, *, query : str):
        result = query.replace(" ", "+")
        await ctx.send(f"https://lmgtfy.app/#gsc.tab=0&gsc.q={result}")


def setup(bot):
    bot.add_cog(Misc(bot))