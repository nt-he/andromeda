import discord
from discord.enums import NotificationLevel
from discord.ext import commands
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
        channel = self.bot.get_channel(848362560255950888)
        await channel.send("<:check:848374065366433852> - Bot is online!\nGuilds:")
        for guild in self.bot.guilds:
            if guild.member_count == "1":
                memberstr = "member"
            else:
                memberstr = "members"
            await channel.send(f"``` - ID: {guild.id} - {guild.name} | {guild.member_count} {memberstr}```")
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        syschannel = guild.system_channel
        if syschannel == None:
            return
        else:
            await syschannel.send(f":wave: Hey, I'm Oscie Bot 3! Thank you for inviting me to your server. To get started, run `o.help`.")

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        logchannel = self.bot.get_channel(848362560255950888)
        await logchannel.send(f"<:invitesub:848556391337558017> - I was just removed from **`{guild}`**")

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
            embed.set_author(name=f"'{message.author.display_name}#{message.author.discriminator}' says...", icon_url=message.author.avatar_url)
            await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Listeners(bot))