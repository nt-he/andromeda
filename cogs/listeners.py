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
    async def on_member_join(self, member):
        
        logchannel = self.bot.get_channel(848362560255950888)
        syschannel = member.guild.system_channel

        await logchannel.send(f"<:inviteadd:848556391664189440> - **{member.mention}** just joined **`{member.guild}`**")
        if syschannel == None:
            return
        else:
            await syschannel.send(f":wave: **{member.mention}** just joined the server, say Hey!")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        
        logchannel = self.bot.get_channel(848362560255950888)
        syschannel = member.guild.system_channel

        await logchannel.send(f"<:invitesub:848556391337558017> - **{member.mention}** just left **`{member.guild}`**")
        if syschannel == None:
            return
        else:
            await syschannel.send(f":wave: **{member.mention}** just left the server, bye!")

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        logchannel = self.bot.get_channel(848362560255950888)
        syschannel = guild.system_channel

        await logchannel.send(f"<:inviteadd:848556391664189440> - I was just added to **`{guild}`**")
        if syschannel == None:
            return
        else:
            await syschannel.send(f":wave: Hey, I'm Oscie Bot 3! Thank you for inviting me to your server. To get started, run `o.help`.")

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        logchannel = self.bot.get_channel(848362560255950888)
        await logchannel.send(f"<:invitesub:848556391337558017> - I was just removed from **`{guild}`**")

    @commands.Cog.listener()
    async def on_member_unban(self, guild, user):
        logchannel = self.bot.get_channel(848362560255950888)
        await logchannel.send(f"<:empty:848375084577325068> - **{user.mention}** was unbanned from **`{guild}`**")
        
    @commands.Cog.listener()
    async def on_invite_create(self, invite):
        logchannel = self.bot.get_channel(848362560255950888)
        await logchannel.send(f"<:invitecreate:848558377282174977> - An invite (<{invite}>) was created in **`{invite.guild}`**")

    @commands.Cog.listener()
    async def on_invite_delete(self, invite):
        logchannel = self.bot.get_channel(848362560255950888)
        await logchannel.send(f"<:invitedelete:848558377395290123> - An invite (<{invite}>) was deleted in **`{invite.guild}`**")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id != 806378095334391879:
            return
        if message.content != "e":
            await message.delete()

        


def setup(bot):
    bot.add_cog(Listeners(bot))