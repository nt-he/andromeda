import asyncio
import discord
from discord.ext import commands
import datetime

class MessageLog(commands.Cog):
    """Logs message changes"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        channel = self.bot.get_channel(854010015199133727)
        guild = self.bot.get_guild(804449200921509913)

        if message.author == self.bot.user:
            return
        if message.guild is not guild:
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

def setup(bot):
    bot.add_cog(MessageLog(bot))