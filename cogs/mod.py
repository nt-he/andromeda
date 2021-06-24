import discord
from discord.ext import commands

class Moderation(commands.Cog):
    """Cog for moderation-ish commands such as banning or clearing"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=5):
        """Clears {amount} messages"""
        logchannel = self.bot.get_channel(854010015199133727)
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f":+1: {amount} messages deleted", delete_after=3)

        embed = discord.Embed(color=0x7289DA, description=f"<:bin:848554827545444402> - {amount} messages deleted in **`{ctx.guild}`**")
        await logchannel.send(embed = embed)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        """Bans the mentioned member"""
        await member.ban(reason=reason, delete_message_days=7)
        await ctx.send(f"{member.mention} was banned for `{reason}`")
        logchannel = self.bot.get_channel(854010015199133727)

        embed = discord.Embed(color=0x7289DA, description=f"<:empty:848375084577325068> - **{member.mention}** was banned from **`{ctx.guild}`** for `{reason}`")
        await logchannel.send(embed=embed)

    @commands.command()
    @commands.has_permissions(ban_members=True, kick_members=True)
    async def unban(self, ctx, *, member):
        """Unbans the mentioned member"""
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")
        logchannel = self.bot.get_channel(854010015199133727)

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"**`{user.name}#{user.discriminator}`** was unbanned")
            
                embed = discord.Embed(color=0x7289DA, description=f"<:empty:848375084577325068> - **{member.mention}** was unbanned from **`{ctx.guild}`**")
                await logchannel.send(embed=embed)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason):
        """Kicks the mentioned member"""
        await member.kick(reason=reason)
        await ctx.send(f"{member.mention} was kicked for `{reason}`")
        logchannel = self.bot.get_channel(854010015199133727)
    
        embed = discord.Embed(color=0x7289DA, description=f"<:empty:848375084577325068> - **{member.mention}** was kicked from **`{ctx.guild}`** for `{reason}`")
        await logchannel.send(embed=embed)

    @commands.command()
    @commands.has_permissions(kick_members=True, manage_roles=True)
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        """Mutes the mentioned member
        nt,he only"""
        if ctx.guild.id != 804449200921509913:
            return
        if reason == None:
            reason = "No reason specified"
        muterole = discord.utils.get(ctx.guild.roles, name="muted")
        if muterole in member.roles:
            await ctx.send(f"{member.mention} is already muted.")
            return
        else:
            await member.add_roles(muterole, reason=reason)
            logchannel = self.bot.get_channel(854010015199133727)
            await ctx.send(f"{member.mention} was just muted for `{reason}`")
            embed = discord.Embed(color=0x7289DA, description=f"<:empty:848375084577325068> - **{member.mention}** was muted from **`{ctx.guild}`** for `{reason}`")
            await logchannel.send(embed=embed)
            return
    
    @commands.command()
    @commands.has_permissions(kick_members=True, manage_roles=True)
    async def unmute(self, ctx, member: discord.Member):
        """Unmutes the mentioned member
        nt,he only"""
        if ctx.guild.id != 804449200921509913:
            await ctx.send("This command can only be ran in `no thoughts, head empty`")
            return
        muterole = discord.utils.get(ctx.guild.roles, name="muted")
        if muterole in member.roles:
            await member.remove_roles(muterole)
            logchannel = self.bot.get_channel(854010015199133727)
            await ctx.send(f"{member.mention} was just unmuted")
            await logchannel.send(f"<:empty:848375084577325068> - **{member.mention}** was unmuted")
            embed = discord.Embed(color=0x7289DA, description=f"<:empty:848375084577325068> - **{member.mention}** was unmuted")
            await logchannel.send(embed=embed)
            return
        else:
            await ctx.send(f"{member.mention} isn't muted.")
            return

def setup(bot):
    bot.add_cog(Moderation(bot))