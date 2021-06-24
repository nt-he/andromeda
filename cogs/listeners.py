import discord
from discord.enums import NotificationLevel
from discord.ext import commands
import datetime
import time

from discord.ext.commands.core import bot_has_permissions

noteslegal = "¹X signifies version.\nAs of 06/2021, there are 3 versions (1, 2 and 3). Messages and Audit Logs will only be monitored in ``no thoughts, head empty (804449200921509913)``\n\n²Date of last update\nThis message will only be updated for an important reason, and we can make changes to this without informing you."

linkslegal = "[Discord Terms of Service](https://dis.gd/terms) ・ [Discord Community Guidelines](https://discord.com/guidelines) ・ [Discord API Legal](https://discord.com/developers/docs/legal) ・ [Discord API Policy](https://discord.com/developers/docs/policy) ・ [Discord Privacy Policy](https://discord.com/privacy)\n\n[Bot Page](https://oscie.net/bot) ・ [Bot Invite Page](https://bot.oscie.net) ・ [Oscie Website](https://oscie.net)"

desclegal = "By adding my bot (Oscie Bot X¹) to your guild, you allow me (as the owner) to see the guild name, description, icon, member count, and any other information disclosable by the Discord API. Read more about Discord API's Terms and Conditions at [Discord Developer Policy](https://discord.com/developers/docs/policy) and [Discord Developer Legal](https://discord.com/developers/docs/legal). You may only use this bot in a way that follows the discord guidelines and terms of service, read [Discord TOS](https://dis.gd/terms) for more info. Message last updated²: 2021.06.18"


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
        logchannel = self.bot.get_channel(854010015199133727)

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

        embed3 = discord.Embed(color=0x7289DA, title="Important Information", description=desclegal)
        embed3.set_author(icon_url = self.bot.user.avatar_url, name = self.bot.user.name)
        embed3.add_field(name = "Notes needed", value = noteslegal)
        embed3.add_field(name = "Important Links", value = linkslegal)

        await logchannel.send(embed = embed3)

        embed4 = discord.Embed(color=0x7289DA, timestamp=datetime.datetime.today())
        embed4.set_footer(text="Bot started at (UTC)")
        await logchannel.send(embed = embed4)

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        syschannel = guild.system_channel
        logchannel = self.bot.get_channel(854010015199133727)

        name = str(guild.name)
        id = str(guild.id)
        members = str(guild.member_count)
        owner = str(guild.owner.mention)
        ownerdm = guild.owner
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

        embed = discord.Embed(color=0x7289DA, description=f"I was just added to **`{guild}`**")
        embed.add_field(name="Name", value=name, inline=True)
        embed.add_field(name="Guild ID", value=id, inline=True)
        embed.add_field(name="Owner", value=owner, inline=True)
        embed.add_field(name="Members", value=members, inline=True)
        embed.add_field(name="System Channel", value=systemchan, inline=True)
        embed.add_field(name="Region", value=region, inline=True)
        embed.add_field(name="Description", value=desc, inline=False)
        embed.set_thumbnail(url=icon)
        await logchannel.send(embed=embed)
        
        embed3 = discord.Embed(color=0x7289DA, title="Important Information", description=desclegal)
        embed3.set_author(icon_url = self.bot.user.avatar_url, name = self.bot.user.name)
        embed3.add_field(name = "Notes needed", value = noteslegal)
        embed3.add_field(name = "Important Links", value = linkslegal)

        if syschannel == None:
            return
        else:
            await syschannel.send(f":wave: Hey, I'm Oscie Bot 3! Thank you for inviting me to your server. To get started, run `o.help` in either DMs or in {guild}. First, you need to be aware of some stuff. Please read the embed below:", embed = embed3)
            await syschannel.send(f"{owner.mention} please read the above.")
        
        #await ownerdm.send(f":wave: Hey, I'm Oscie Bot 3! Thank you for inviting me to {guild}}. To get started, run `o.help` in either DMs or in {guild}. First, you need to be aware of some stuff. Please read the embed below:", embed = anembed)
            


    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        logchannel = self.bot.get_channel(854010015199133727)
        
        name = str(guild.name)
        members = str(guild.member_count)
        owner = str(guild.owner.mention)
        icon = str(guild.icon_url)

        if members == "1":
            members = "member"
        else:
            members = "members"

        embed = discord.Embed(color=0x7289DA, description=f"I was just added to **`{guild}`**")
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

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        channel = self.bot.get_channel(854010015199133727)
        guild = self.bot.get_guild(804449200921509913)

        if message.author == self.bot.user:
            return
        if message.guild is not guild:
            return
        if message.content.startswith("o."):
            return
        
        embed = discord.Embed(color=0x7289DA, title="Message Deleted", timestamp=datetime.datetime.today())
        embed.set_author(name=message.author, icon_url=message.author.avatar_url)
        embed.add_field(name="Content", value=message.content)
        embed.add_field(name="In Channel", value=f"<#{message.channel.id}>")
        await channel.send(embed = embed)
    
    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        channel = self.bot.get_channel(854010015199133727)
        guild = self.bot.get_guild(804449200921509913)

        if before.author == self.bot.user:
            return
        if before.guild is not guild:
            return

        embed = discord.Embed(color=0x7289DA, title="Message Edited", timestamp=datetime.datetime.today())
        embed.set_author(name=before.author, icon_url=before.author.avatar_url)
        embed.add_field(name="Before", value=before.content, inline=True)
        embed.add_field(name="After", value=after.content, inline=True)
        embed.add_field(name="In Channel", value=f"<#{before.channel.id}>", inline=False)
        await channel.send(embed = embed)

    @commands.Cog.listener()
    async def on_reaction_clear(self, message, reactions):
        channel = self.bot.get_channel(854010015199133727)
        guild = self.bot.get_guild(804449200921509913)

        if message.author == self.bot.user:
            return
        if message.guild is not guild:
            return

        embed = discord.Embed(color=0x7289DA, title="Reactions Cleared", timestamp=datetime.datetime.today())
        embed.set_author(name=message.author, icon_url=message.author.avatar_url)
        embed.add_field(name="Message Content", value=message.content)
        embed.add_field(name="Reactions Removed", value=str(reactions))
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):
        logchannel = self.bot.get_channel(854010015199133727)
        guild = self.bot.get_guild(804449200921509913)

        if channel.guild is not guild:
            return

        embed = discord.Embed(color=0x7289DA, title="Channel Deleted", timestamp=datetime.datetime.today())
        embed.add_field(name="Channel Name", value=channel)
        embed.add_field(name="ID", value=channel.id)
        await logchannel.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        logchannel = self.bot.get_channel(854010015199133727)
        guild = self.bot.get_guild(804449200921509913)

        if channel.guild is not guild:
            return

        embed = discord.Embed(color=0x7289DA, title="Channel Created", timestamp=datetime.datetime.today())
        embed.add_field(name="Name", value=channel)
        embed.add_field(name="ID", value=channel.id)
        embed.add_field(name="Mention", value=channel.mention)
        await logchannel.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_channel_update(self, before, after):
        logchannel = self.bot.get_channel(854010015199133727)
        guild = self.bot.get_guild(804449200921509913)

        if before.guild is not guild:
            return

        if before.category or after.category == "Personal Stuff":
            return

        if after.position != before.position:
            return

        embed = discord.Embed(color=0x7289DA, title="Channel Edited", timestamp=datetime.datetime.today())
        embed.add_field(name="Name Before", value=before.name)
        embed.add_field(name="Name After", value=after.name)
        embed.add_field(name="Category Before", value=before.category)
        embed.add_field(name="Category After", value=after.category)
        embed.add_field(name="Position Before", value=before.position)
        embed.add_field(name="Position After", value=after.position)
        embed.add_field(name="Topic Before", value=before.topic)
        embed.add_field(name="Topic After", value=after.topic)
        embed.add_field(name="Channel Mention", value=before.mention)
        await logchannel.send(embed=embed)


    @commands.Cog.listener()
    async def on_webhooks_update(self, channel):
        logchannel = self.bot.get_channel(854010015199133727)
        guild = self.bot.get_guild(804449200921509913)

        if channel.guild is not guild:
            return

        await logchannel.send(str(channel))

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        logchannel = self.bot.get_channel(854010015199133727)
        if isinstance(error, commands.DisabledCommand):
            await logchannel.send(f"<:cross:848374065550458920> - Error: Command is disabled")
            await ctx.send(f"<:cross:848374065550458920> - Sorry, that command is disabled.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await logchannel.send(f"<:cross:848374065550458920> - Error: Missing Required Arguments")
            await ctx.send(f"<:cross:848374065550458920> - Sorry, you forgot some important information when running that command.")
        elif isinstance(error, commands.CommandNotFound):
            await logchannel.send(f"<:cross:848374065550458920> - Error: Command cannot be found")
            await ctx.send(f"<:cross:848374065550458920> - Sorry, that command is not a valid command.")
        elif isinstance(error, commands.NoPrivateMessage):
            await logchannel.send(f"<:cross:848374065550458920> - Error: Command is guild only")
            await ctx.send(f"<:cross:848374065550458920> - Sorry, that command can only be used in servers.")
        elif isinstance(error, commands.BadArgument):
            await logchannel.send(f"<:cross:848374065550458920> - Error: I recieved a bad argument")
            await ctx.send(f"<:cross:848374065550458920> - I recieved a bad argument.")
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        logchannel = self.bot.get_channel(854010015199133727)
        if isinstance(error, commands.MessageNotFound):
            await logchannel.send(f"<:cross:848374065550458920> - Error: Message not found")
            await ctx.send(f"<:cross:848374065550458920> - Sorry, I cannot find that message.")
        elif isinstance(error, commands.UserNotFound):
            await logchannel.send(f"<:cross:848374065550458920> - Error: User not found")
            await ctx.send(f"<:cross:848374065550458920> - Sorry, I cannot find that user.")
        elif isinstance(error, commands.MemberNotFound):
            await logchannel.send(f"<:cross:848374065550458920> - Error: Member not found")
            await ctx.send(f"<:cross:848374065550458920> - Sorry, I cannot find that member.")
        elif isinstance(error, commands.ChannelNotFound):
            await logchannel.send(f"<:cross:848374065550458920> - Error: cannot find specified channel")
            await ctx.send(f"<:cross:848374065550458920> - Sorry, I cant find that channel.")
        elif isinstance(error, commands.ChannelNotReadable):
            await logchannel.send(f"<:cross:848374065550458920> - Error: Cannot read channel")
            await ctx.send(f"<:cross:848374065550458920> - Sorry, I cannot read messages in that channel")
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        logchannel = self.bot.get_channel(854010015199133727)
        if isinstance(error, commands.RoleNotFound):
            await logchannel.send(f"<:cross:848374065550458920> - Error: Role not found")
            await ctx.send(f"<:cross:848374065550458920> - Sorry, I cannot find that role.")
        elif isinstance(error, commands.EmojiNotFound):
            await logchannel.send(f"<:cross:848374065550458920> - Error: Specified emoji cannot be found")
            await ctx.send(f"<:cross:848374065550458920> - Sorry, I cannot find that emoji.")
        elif isinstance(error, commands.PrivateMessageOnly):
            await logchannel.send(f"<:cross:848374065550458920> - Error: Command can only be used in private messages")
            await ctx.send(f"<:cross:848374065550458920> - Sorry, that command can only be used in DMs")
        elif isinstance(error, commands.NotOwner):
            await logchannel.send(f"<:cross:848374065550458920> - Error: User is not owner")
            await ctx.send(f"<:cross:848374065550458920> - Sorry, this command can only be used by the bot's owner")
        elif isinstance(error, commands.MissingPermissions):
            await logchannel.send(f"<:cross:848374065550458920> - Error: Author does not have permission to run Command")
            await ctx.send(f"<:cross:848374065550458920> - Sorry, you do not have the correct permissions to run that command.")
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        logchannel = self.bot.get_channel(854010015199133727)
        if isinstance(error, commands.BotMissingPermissions):
            await logchannel.send(f"<:cross:848374065550458920> - Error: I do not have permission in **`{ctx.guild}`**")
            await ctx.send(f"<:cross:848374065550458920> - Sorry, I do not have permission to run that.")
        elif isinstance(error, commands.MissingRole):
            await logchannel.send(f"<:cross:848374065550458920> - Error: Author does not have the right role")
            await ctx.send(f"<:cross:848374065550458920> - Sorry, you do not have the role that is needed to use that command.")
        elif isinstance(error, commands.CommandOnCooldown):
            await logchannel.send(f"<:cross:848374065550458920> - Error: Command is on cooldown")
            await ctx.send(f"<:cross:848374065550458920> - Sorry, that command is on cooldown.")
        elif isinstance(error, AttributeError):
            await logchannel.send(f"<:cross:848374065550458920> - Error: Attribute Error (Read Terminal)")
            raise error
        else:
            raise error


def setup(bot):
    bot.add_cog(Listeners(bot))