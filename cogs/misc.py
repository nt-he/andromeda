from cogs.music import Music
import discord
from discord import embeds
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
import random

noteslegal = "¹X signifies version.\nAs of 06/2021, there are 3 versions (1, 2 and 3). Messages and Audit Logs will only be monitored in ``no thoughts, head empty (804449200921509913)``\n\n²Date of last update\nThis message will only be updated for an important reason, and we can make changes to this without informing you."

linkslegal = "[Discord Terms of Service](https://dis.gd/terms) ・ [Discord Community Guidelines](https://discord.com/guidelines) ・ [Discord API Legal](https://discord.com/developers/docs/legal) ・ [Discord API Policy](https://discord.com/developers/docs/policy) ・ [Discord Privacy Policy](https://discord.com/privacy)\n\n[Bot Page](https://oscie.net/bot) ・ [Bot Invite Page](https://bot.oscie.net) ・ [Oscie Website](https://oscie.net)"

desclegal = "By adding my bot (Oscie Bot X¹) to your guild, you allow me (as the owner) to see the guild name, description, icon, member count, and any other information disclosable by the Discord API. Read more about Discord API's Terms and Conditions at [Discord Developer Policy](https://discord.com/developers/docs/policy) and [Discord Developer Legal](https://discord.com/developers/docs/legal). You may only use this bot in a way that follows the discord guidelines and terms of service, read [Discord TOS](https://dis.gd/terms) for more info. Message last updated²: 2021.06.18"

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
]

player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

def checkWinner(winningConditions, mark):
        global gameOver
        for condition in winningConditions:
            if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
                gameOver = True

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
    async def information(self, ctx):
        """Information about Oscie Bot 3"""

        anembed = discord.Embed(
            color=0x7289DA,
            title="Important Information", 
            description=desclegal
        )
        anembed.set_author(
            icon_url = self.bot.user.avatar_url,
            name = self.bot.user.name
        )
        anembed.add_field(
            name = "Notes needed",
            value = noteslegal
        )
        anembed.add_field(
            name = "Important Links", 
            value = linkslegal
        )
        await ctx.send(f"{ctx.author.mention} :wave: Hey there! As you know, I am Oscie Bot 3! By running this, you would like to see this important information. Please read the embed below for that information you requested (it is also at the bottom of https://bot.oscie.net)", embed=anembed)


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

    commands.group(invoke_without_command=True)
    async def stickers(self, ctx):
        """Shows Sticker store pages
        Usage: "o.store stickers [stickerpack]"""
        await ctx.send(
            'To find the stickers currently avaliable in this store, type `o.help store stickers`. '
            'Please note: These pages will only work if you are in one of these following countries, '
            '`Canada`, `Brazil` or `Japan`.'
        )


    @commands.group(aliases=["servers"], invoke_without_command=True)
    async def invites(self, ctx):
        """Shows Game store invites
        Usage: "o.store invites|servers [servername]\""""
        await ctx.send(
            'These are games that do not have specific (linkable) store pages, '
            'so you will have to join the developers server to obtain the game. '
            'Use `o.help store invites` to see the applicable games.'
        )


    @commands.group(aliases=["games"], invoke_without_command=True)
    async def sku(self, ctx):
        """Shows Game store pages (SKU)
        Usage: "o.store sku|games [gamename]\""""
        await ctx.send(
            'These are games that have store pages that can be directly installed or visited. '
            'Most are free, but there are a few paid in the mix. Use `o.help store sku` for a list of games and price.'
        )


    @commands.group(invoke_without_command=True)
    async def extras(self, ctx):
        """Shows extra store pages
        Usage: "o.store extras [extra]\""""
        await ctx.send(
            'These are store pages that are either for jokes or do nothing. Use `o.help store extras` for a full list')


    @commands.group(invoke_without_command=True)
    async def dlc(self, ctx):
        """Shows DLC pages (needs Base Game)
        Usage: "o.store dlc [game]\""""
        await ctx.send(
            'These are store pages that are DLC (downloadable content) '
            'that are avaliable for discord games that we have in the other store commands. '
            'Use `o.help store dlc` for the list of games with DLC'
        )


    @stickers.command()
    async def whatsupwumpus(self, ctx):
        """What's Up Wumpus - £2.99"""
        await ctx.send('https://ptb.discord.com/store/skus/748286108348973106/what-s-up-wumpus-sticker-pack')


    @stickers.command()
    async def hellowumpus(self, ctx):
        """Hello Wumpus - Free"""
        await ctx.send('https://ptb.discord.com/store/skus/749043407997108384/hello-wumpus-sticker-pack')


    @invites.command()
    async def patchquest(self, ctx):
        """Patch Quest server invite"""
        await ctx.send('Patch Quest (Public Beta) - Free')
        await ctx.send('https://discord.com/invite/pyF5jmP')


    @invites.command()
    async def cookiedragon(self, ctx):
        """Two Kinds Online server invite"""
        await ctx.send('Two Kinds Online (Alpha) - Free')
        await ctx.send('https://discord.gg/cookiedragon')


    @invites.command()
    async def cycle28(self, ctx):
        """Cycle 28 Invite"""
        await ctx.send('Cycle 28 - £0.99 (-50%)')
        await ctx.send('https://discord.gg/FpD4SuYeCm')


    @invites.command()
    async def staysafe(self, ctx):
        """Yellowcake Games Invite"""
        await ctx.send('Stay Safe - £2.99')
        await ctx.send('https://discord.gg/yellowcakegames')


    @invites.command()
    async def hexrunpro(self, ctx):
        """Hex! Run Pro Invite"""
        await ctx.send('Hex! Run Pro - £19.99')
        await ctx.send('https://discord.gg/S9yAhrJrDg')


    @extras.command()
    async def poggers(self, ctx):
        """Poggers"""
        await ctx.send('https://canary.discord.com/store/skus/692146322924372089/poggers')


    @extras.command()
    async def yoshi(self, ctx):
        """Yoshi game"""
        await ctx.send('https://ptb.discord.com/store/skus/710797635388178462/yoshi')


    @extras.command()
    async def wiilink24(self, ctx):
        """Installing WiiLink24"""
        await ctx.send('https://ptb.discord.com/store/skus/806878609302093866/installing-wiilink24')


    @extras.command()
    async def nitro(self, ctx):
        """Discord Nitro Classic"""
        await ctx.send('https://ptb.discord.com/store/skus/715629060331405382/nitro-classic')


    @extras.command()
    async def bge(self, ctx):
        """Best Game Ever"""
        await ctx.send('https://ptb.discord.com/store/skus/461618159171141643/best-game-ever')


    @sku.command()
    async def koth(self, ctx):
        """King of the Hat - £14.99"""
        await ctx.send('https://ptb.discord.com/store/skus/486981988109254667/king-of-the-hat')


    @sku.command()
    async def minionmasters(self, ctx):
        """Minion Masters - Free (DLC)"""
        await ctx.send('https://ptb.discord.com/store/skus/488607666231443456/minion-masters')


    @dlc.command()
    async def minionmasters(self, ctx):
        """Minion Masters DLC - `o.store sku minionmasters`"""
        await ctx.send(
            'https://ptb.discord.com/store/skus/742277397105213440/nightmares\n'
            'https://canary.discord.com/store/skus/515467071924994048/all-masters\n'
            'https://canary.discord.com/store/skus/491564667983101953/premium-upgrade\n'
            'https://canary.discord.com/store/skus/548071645265264650/voidborne-onslaught\n'
            'https://canary.discord.com/store/skus/639095281668849664/crystal-conquest'
        )
        await ctx.send(
            'https://canary.discord.com/store/skus/565546081975533578/accursed-army-pack\n'
            'https://canary.discord.com/store/skus/607929247578849283/might-of-the-slither-lords\n'
            'https://canary.discord.com/store/skus/678878135697145866/zealous-inferno\n'
            'https://canary.discord.com/store/skus/707885099101847622/charging-into-darkness'
        )


    @sku.command()
    async def cdreboot(self, ctx):
        """Cerpe Diem: Reboot - £4.99"""
        await ctx.send('https://canary.discord.com/store/skus/568922402390671360/carpe-diem-reboot')


    @sku.command()
    async def forsakenr(self, ctx):
        """Forsaken Remastered - £16.98"""
        await ctx.send('https://ptb.discord.com/store/skus/494870847777931268/forsaken-remastered')


    @sku.command()
    async def forager(self, ctx):
        """Forager - £14.99"""
        await ctx.send('https://ptb.discord.com/store/skus/530541618504269875/forager')


    @sku.command()
    async def staysafe(self, ctx):
        """Stay Safe - £2.99"""
        await ctx.send('https://ptb.discord.com/store/skus/431807599860514817/stay-safe')


    @sku.command()
    async def steelseraph(self, ctx):
        """Steel Seraph - £1.99 (-33%)"""
        await ctx.send('https://ptb.discord.com/store/skus/555820631007035413/steel-seraph')


    @sku.command()
    async def tanglewood(self, ctx):
        """TANGLEWOOD® - £7.99 (-43%)"""
        await ctx.send('https://ptb.discord.com/store/skus/378315252749565952/tanglewood-r')


    @sku.command()
    async def temtem(self, ctx):
        """Temtem - £30.99"""
        await ctx.send('https://ptb.discord.com/store/skus/558547388583772201/temtem')


    @sku.command()
    async def thevagrant(self, ctx):
        """The Vagrant - £1.99 (-50%)"""
        await ctx.send('https://ptb.discord.com/store/skus/562121024993230868/the-vagrant')


    @sku.command()
    async def underonewing(self, ctx):
        """Under One Wing - £28.99"""
        await ctx.send('https://ptb.discord.com/store/skus/555856535327342592/under-one-wing')


    @sku.command()
    async def newtontree(self, ctx):
        """Newton and the Apple Tree - £38.99"""
        await ctx.send('https://ptb.discord.com/store/skus/555867662442430483/newton-and-the-apple-tree')


    @sku.command()
    async def zombsroyaleio(self, ctx):
        """ZombsRoyale.io - Free"""
        await ctx.send('https://ptb.discord.com/store/skus/519338998791929866/zombsroyale-io')


    @sku.command()
    async def realmroyale(self, ctx):
        """Realm Royale - Free (DLC)"""
        await ctx.send('https://ptb.discord.com/store/skus/518088627234930688/realm-royale')


    @dlc.command()
    async def realmroyale(self, ctx):
        """Realm Royale DLC - `o.store sku realmroyale`"""
        await ctx.send(
            'https://canary.discord.com/store/skus/564916655285600266/realm-royale-bass-drop-bundle\n'
            'https://canary.discord.com/store/skus/595360871472168991/realm-royale-cute-but-deadly-pack'
        )


    @sku.command()
    async def paladins(self, ctx):
        """Paladins - Free"""
        await ctx.send('https://ptb.discord.com/store/skus/528145079819436043/paladins')


    @sku.command()
    async def heartwoods(self, ctx):
        """Heart of the Woods - £10.25 (-32%)"""
        await ctx.send('https://ptb.discord.com/store/skus/555830991168733204/heart-of-the-woods')


    @sku.command()
    async def amagicalgirl(self, ctx):
        """A Magical High School Girl - £4.67 (-53%)"""
        await ctx.send('https://ptb.discord.com/store/skus/555812072969994260/a-magical-high-school-girl')


    @sku.command()
    async def warframe(self, ctx):
        """Warframe - Free"""
        await ctx.send('https://ptb.discord.com/store/skus/494959992483348480/warframe')


    @sku.command()
    async def pickcrafter(self, ctx):
        """Pickcrafter - Free"""
        await ctx.send('https://ptb.discord.com/store/skus/560643262424285194/pickcrafter')


    @sku.command()
    async def assitd(self, ctx):
        """AT SUNDOWN: Shots in the Dark - £11.24"""
        await ctx.send('https://ptb.discord.com/store/skus/487031053454802946/at-sundown-shots-in-the-dark')


    @sku.command()
    async def madmachines(self, ctx):
        """MAD MACHINES - £9.99"""
        await ctx.send('https://ptb.discord.com/store/skus/487272772393762826/mad-machines')


    @sku.command()
    async def avoidplus(self, ctx):
        """Avoid Premium - £5.99"""
        await ctx.send('https://ptb.discord.com/store/skus/586603437299597333/avoid-premium')


    @sku.command()
    async def scpsl(self, ctx):
        """SCP: Secret Laboratory - Free"""
        await ctx.send('https://ptb.discord.com/store/skus/420676877766623232/scp-secret-laboratory')


    @sku.command()
    async def sandboxes(self, ctx):
        """SandBoxes - Free"""
        await ctx.send('https://ptb.discord.com/store/skus/519249930611589141/sandboxes')


    @sku.command()
    async def forestir(self, ctx):
        """Forestir - Free"""
        await ctx.send('https://ptb.discord.com/store/skus/554072621000556584/forestir')


    @sku.command()
    async def ihbad(self, ctx):
        """Its Hard Being A Dog - Free"""
        await ctx.send('https://ptb.discord.com/store/skus/565994833953554432/it-s-hard-being-a-dog')


    @sku.command()
    async def avoid(self, ctx):
        """Avoid - Free"""
        await ctx.send('https://ptb.discord.com/store/skus/601864041731719189/avoid')


    @sku.command()
    async def hagwwii(self, ctx):
        """Heroes & Generals WWII - Free"""
        await ctx.send('https://ptb.discord.com/store/skus/550277544025522176/heroes-generals-wwii')


    @dlc.command()
    async def hagwwii(self, ctx):
        """Heroes & Generals WWII DLC - `o.store sku hagwwii`"""
        await ctx.send(
            'https://ptb.discord.com/store/skus/558205987434266625/1200-gold\n'
            'https://ptb.discord.com/store/skus/565438968167137280/2200-gold\n'
            'https://ptb.discord.com/store/skus/557535890285658122/4800-gold\n'
            'https://ptb.discord.com/store/skus/565441415270629376/13000-gold\n'
            'https://ptb.discord.com/store/skus/565460799355617289/30000-gold'
        )


    @sku.command()
    async def soma(self, ctx):
        """SOMA - £28.99"""
        await ctx.send('https://ptb.discord.com/store/skus/489230107093893120/soma')


    @sku.command()
    async def bannersaga(self, ctx):
        """Banner Saga 3 - £23.99"""
        await ctx.send('https://ptb.discord.com/store/skus/472483394085715979/banner-saga-3')


    @sku.command()
    async def starsonata(self, ctx):
        """Star Sonata 2 - Free"""
        await ctx.send('https://ptb.discord.com/store/skus/459415040227803141/star-sonata-2')


    @sku.command()
    async def taopepel(self, ctx):
        """The Adventures of PepeL - Free"""
        await ctx.send('https://ptb.discord.com/store/skus/554072366213234729/the-adventures-of-pepel')


    @sku.command()
    async def jumplats(self, ctx):
        """Jumplats - Free"""
        await ctx.send('https://ptb.discord.com/store/skus/618864578545319956/jumplats')


    @sku.command()
    async def lftb(self, ctx):
        """Light From The Butt - Free"""
        await ctx.send('https://ptb.discord.com/store/skus/594073512906588179/light-from-the-butt')


    @sku.command()
    async def metald(self, ctx):
        """Metal's Dungeon - £1.99"""
        await ctx.send('https://ptb.discord.com/store/skus/557494559257526272/metal-s-dungeon')


    @sku.command()
    async def mofanima(self, ctx):
        """Masters of Anima - £19.98"""
        await ctx.send('https://ptb.discord.com/store/skus/492418279717994505/masters-of-anima')


    @sku.command()
    async def parkasaurus(self, ctx):
        """Parkasaurus - £19.99"""
        await ctx.send('https://ptb.discord.com/store/skus/508008071411400724/parkasaurus')


    @sku.command()
    async def sinnersfr(self, ctx):
        """Sinner: Sacrifice for Redemption - £18.99"""
        await ctx.send('https://ptb.discord.com/store/skus/489184797936058380/sinner-sacrifice-for-redemption')


    @sku.command()
    async def subnautica(self, ctx):
        """Subnautica - £24.99"""
        await ctx.send('https://ptb.discord.com/store/skus/489926636943441932/subnautica')


    @sku.command()
    async def poe2df(self, ctx):
        """Pillars of Eternity II: Deadfire - £48.99"""
        await ctx.send('https://ptb.discord.com/store/skus/466696214818193408/pillars-of-eternity-ii-deadfire')


    @sku.command()
    async def subnautica2(self, ctx):
        """Subnautica: Below Zero - £24.99"""
        await ctx.send('https://ptb.discord.com/store/skus/535869836748783616/subnautica-below-zero')


    @sku.command()
    async def callofc(self, ctx):
        """Call of Cthulu - £39.99"""
        await ctx.send('https://ptb.discord.com/store/skus/503982482664849408/call-of-cthulhu-r')


    @sku.command()
    async def amnesiatdd(self, ctx):
        """Amnesia: The Dark Descent - £19.99"""
        await ctx.send('https://ptb.discord.com/store/skus/489229235509002261/amnesia-the-dark-descent')


    @sku.command()
    async def hexrun(self, ctx):
        """Hex! Run - £0.99 (-50%)"""
        await ctx.send('https://ptb.discord.com/store/skus/598419143661846528/hex-run')

    @commands.command()
    async def tictactoe(self, ctx, p1 : discord.Member, p2 : discord.Member):
        """Start the TicTacToe game"""
        global player1
        global player2
        global turn
        global gameOver
        global count

        if gameOver:
            global board
            board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                     ":white_large_square:", ":white_large_square:", ":white_large_square:",
                     ":white_large_square:", ":white_large_square:", ":white_large_square:"]
            turn = ""
            gameOver = False
            count = 0

            player1 = p1
            player2 = p2

            #print the board
            line = ""
            for x in range(len(board)):
                if x == 2 or x == 5 or x == 8:
                    line += " " + board[x]
                    await ctx.send(line)
                    line = " "
                else:
                    line += " " + board[x]

            # determine who goes first
            num = random.randint(1, 2)
            if num == 1:
                turn = player1
                await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
            elif num == 2:
                turn = player2
                await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
        else:
            await ctx.send("A game is already in progress! Finish it before starting a new one.")

    @commands.command()
    async def place(self, ctx, pos : int):
        """Place your piece on the board"""
        global turn
        global player1
        global player2
        global board
        global count

        if not gameOver:
            mark = ""
            if turn == ctx.author:
                if turn == player1:
                    mark = ":regional_indicator_x:"
                elif turn == player2:
                    mark = ":o2:"
                if 0 < pos < 10 and board[pos - 1] == ":white_large_square:":
                    board[pos - 1] = mark
                    count += 1

                    # print board
                    line = ""
                    for x in range(len(board)):
                        if x == 2 or x == 5 or x == 8:
                            line += " " + board[x]
                            await ctx.send(line)
                            line = " "
                        else:
                            line += " " + board[x]

                    checkWinner(winningConditions, mark)
                    if gameOver:
                        await ctx.send(mark + " wins!")
                    elif count >= 9:
                        await ctx.send("It's a tie!")
                    
                    # switch turns
                    if turn == player1:
                        turn = player2
                    elif turn == player2:
                        turn = player1

                else:
                    await ctx.send("Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile.")
            else:
                await ctx.send("It is not your turn.")
        else:
            await ctx.send("Please start a new game using the `o.tictactoe` command.")

    @tictactoe.error
    async def tictactoe_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please mention 2 players for this command.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Please make sure to mention/ping players (ie. <@848181143169925180>)")

    @place.error
    async def place_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please enter a position you would like to mark.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Please make sure to enter an integer.")

    @commands.command()
    async def sochashbrowns(self, ctx):
        """Hash Browns SELFCHECK"""
        # TODO: Put the actual Japanese in here
        embed = discord.Embed(color=0x7289DA)
        embed.set_author(name="made by oscie - ecdp guides", icon_url="https://oscie.tk/assets/logo.png")
        embed.add_field(name="Important!", value="All of these answers are meant to be used with a phone with the camera on Google Translate, as these were taken directly from it. They are not accurate AT ALL but they work flawlessly with a phone like how it was made.\n\n", inline=False)
        embed.add_field(name="Question Contains\n", value="What do you use for packaging\n\nWhat do customers expect\n\nHow long do hashbrowns go in the fryer\n\nHow long do you drain the oil\n\nWhat temperature is the fryer\n\nWhat is the holding time of hashbrowns\n\nChoose the six non-enemy oils\n\nWhat do you use to clean the station\n\nWhat does it mean to remove the fried\n\nHow many can be placed in the basket")
        embed.add_field(name="Answer Contains\n",value="Tongs\n\nGolden Brown\n\n2:45+5\n\n5-10s\n\n182°C\n\n10\n\nSkimming\n\nDry Wiper\n\nSkimming\n\n8 Pieces")
        await ctx.send(embed=embed)

    @commands.command()
    async def socfries(self, ctx):
        """Fries SELFCHECK"""
        embed = discord.Embed(color=0x7289DA)
        embed.set_author(name="made by oscie - ecdp guides", icon_url="https://oscie.tk/assets/logo.png")
        embed.add_field(name="Important!", value="All of these answers are meant to be used with a phone with the camera on Google Translate, as these were taken directly from it. They are not accurate AT ALL but they work flawlessly with a phone like how it was made.\n\n", inline=False)
        embed.add_field(name="Question Contains\n", value="How many seconds do the next baskets\n\nIf potato is on floor, use [] to pick up\n\nWhen sprinkling salt on fries\n\nExpectations for potatoes\n\nUse special gloves, an apron and []\n\nHow many baskets should one bag\n\nHow long does it take to make potato\n\nChoose the six non-enemy oils\n\nWhere to store potato bags\n\nWhat is the temp of the fryer")
        embed.add_field(name="Answer Contains\n", value="30 Seconds\n\nLarge Tongs\n\nTriple Arch\n\nTexture\n\nFace Shield\n\n4\n\n2:55+5\n\nNutrients `(3 Chars)`\n\nPotato Freezer\n\n168°C")
        await ctx.send(embed=embed)
    
    @commands.command()
    async def socfoodsafety(self, ctx):
        """Food Safety SELFCHECK"""
        embed = discord.Embed(color=0x7289DA)
        embed.set_author(name="made by oscie - ecdp guides", icon_url="https://oscie.tk/assets/logo.png")
        embed.add_field(name="Important!", value="All of these answers are meant to be used with a phone with the camera on Google Translate, as these were taken directly from it. They are not accurate AT ALL but they work flawlessly with a phone like how it was made.\n\n", inline=False)
        embed.add_field(name="Question Contains\n", value="3 Principles of food poisoning prevention\n\nCentimetres from the floor\n\nWhat temp should frozen products be\n\n10:1 Burger\n\nNot necessary to prevent secondary\n\nWhat temp should refrigerated items be\n\nNot correct hand wash\n\nWhat is cross-contamination\n\nWhat causes food safety compromisation\n\nWhat is not standard measure")
        embed.add_field(name="Answer Contains\n", value="Do not increase\n\n15cm\n\n-18°C\n\n69°C\n\nCheck Schedule\n\n4°C\n\nRub with arms crossed\n\nSecondary Pollution\n\nAll display items\n\n\nContact me when late")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Misc(bot))