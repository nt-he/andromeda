import discord
from discord.enums import NotificationLevel
from discord.ext import commands
import datetime
import time

class Listeners(commands.Cog):
    """This cog listens for updates and then does stuff.
    It mostly prints it to my logging channel but thats really it."""

    def __init__(self, bot):
        self.bot = bot

    dashemote = "<:empty:848375084577325068>"
    checkemote = "<:check:848374065366433852>"
    crossemote = "<:cross:848374065550458920>"
    binemote = "<:bin:848554827545444402>"
    invitesub = "<:invitesub:848556391337558017>"
    inviteadd = "<:inviteadd:848556391664189440>"
    unbanned = ""
    banned = ""
    invitecreate = "<:invitecreate:848558377282174977>"
    invitedelete = "<:invitedelete:848558377395290123>"
    status = "<:status:848563270134792242>"

    @commands.Cog.listener()
    async def on_ready(self):
        logchannel = self.bot.get_channel(848362560255950888)

        embed1 = discord.Embed(color=0x7289DA, title="<:check:848374065366433852> - Bot is online! Guilds:")
        await logchannel.send(embed=embed1)

        for guild in self.bot.guilds:
            if guild.member_count == "1":
                memberstr = "member"
            else:
                memberstr = "members"

            name = str(guild.name)
            id = str(guild.id)
            members = str(guild.member_count) + " " + memberstr
            owner = str(guild.owner.mention)
            systemchan = str(guild.system_channel)
            icon = str(guild.icon_url)
            region = str(guild.region)
            desc = str(guild.description)

            if systemchan is None:
                systemchan = "None"
            else:
                systemchan = "#" + systemchan

            if region == "europe":
                region = ":flag_eu: Europe"
            elif region == "us-west":
                region = ":flag_us: US West"
            elif region == "us-central":
                region = ":flag_us: US Central"

            embed2 = discord.Embed(color=0x7289DA)
            embed2.add_field(name="Name", value=name, inline=True)
            embed2.add_field(name="Guild ID", value=id, inline=True)
            embed2.add_field(name="Owner", value=owner, inline=True)
            embed2.add_field(name="Members", value=members, inline=True)
            embed2.add_field(name="System Channel", value=systemchan, inline=True)
            embed2.add_field(name="Region", value=region, inline=True)
            embed2.add_field(name="Description", value=desc, inline=False)
            embed2.set_thumbnail(url=icon)
            await logchannel.send(embed=embed2)

        time.sleep(7)

        embed3 = discord.Embed(color=0x7289DA, timestamp=datetime.datetime.today())
        embed3.set_footer(text="Bot started at ")
        await logchannel.send(embed=embed3)

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        syschannel = guild.system_channel
        logchannel = self.bot.get_channel(848362560255950888)

        name = str(guild.name)
        id = str(guild.id)
        members = str(guild.member_count)
        owner = str(guild.owner.mention)
        systemchan = str(guild.system_channel)
        icon = str(guild.icon_url)
        region = str(guild.region)
        desc = str(guild.description)

        if members == "1":
            members = "member"
        else:
            members = "members"

        if systemchan is None:
            systemchan = "None"
        else:
            systemchan = "#" + systemchan

        if region == "europe":
            region = ":flag_eu: Europe"
        elif region == "us-west":
            region = ":flag_us: US West"
        elif region == "us-central":
            region = ":flag_us: US Central"

        embed = discord.Embed(color=0x7289DA, description="I was just added to **`{guild}`**")
        embed.add_field(name="Name", value=name, inline=True)
        embed.add_field(name="Guild ID", value=id, inline=True)
        embed.add_field(name="Owner", value=owner, inline=True)
        embed.add_field(name="Members", value=members, inline=True)
        embed.add_field(name="System Channel", value=systemchan, inline=True)
        embed.add_field(name="Region", value=region, inline=True)
        embed.add_field(name="Description", value=desc, inline=False)
        embed.set_thumbnail(url=icon)
        await logchannel.send(embed=embed)
        
        if syschannel == None:
            return
        else:
            await syschannel.send(f":wave: Hey, I'm Oscie Bot 3! Thank you for inviting me to your server. To get started, run `o.help`.")
            

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        logchannel = self.bot.get_channel(848362560255950888)
        
        name = str(guild.name)
        members = str(guild.member_count)
        owner = str(guild.owner.mention)
        icon = str(guild.icon_url)

        if members == "1":
            members = "member"
        else:
            members = "members"

        embed = discord.Embed(color=0x7289DA, description="I was just added to **`{guild}`**")
        embed.add_field(name="Name", value=name, inline=True)
        embed.add_field(name="Owner", value=owner, inline=True)
        embed.add_field(name="Members", value=members, inline=True)
        embed.set_thumbnail(url=icon)
        await logchannel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id != 806378095334391879:
            return
        if message.content != "e":
            await message.delete()

    @commands.Cog.listener()
    async def on_message(self, message):
        """For LNH - Returns 'sans pee pee' when it is said"""
        lnhsanschan = 704391659093360762
        if message.channel.id != lnhsanschan:
            return
        else:
            if message.content == "sans pee pee":
                await message.send("sans pee pee")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        elif str(message.channel.type) == "private": 
            channel = self.bot.get_channel(853400947714818088)
            embed = discord.Embed(color=discord.Color.blurple(), description=message.content)
            embed.set_author(name=f"'{message.author.display_name}#{message.author.discriminator}'' says...", icon_url=message.author.avatar_url)
            await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Listeners(bot))