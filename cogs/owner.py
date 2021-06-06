import discord
from discord.ext import commands


class Owner(commands.Cog):
    """Commands that only the owner of the bot can see.
    Mainly just cog maintenence stuff."""

    def __init__(self, bot):
        self.bot = bot
        self.tasks = ""
    
    # Hidden means it won't show up on the default help.
    @commands.command(name='load', hidden=True)
    @commands.is_owner()
    async def cogload(self, ctx, *, cog: str):
        logchannel = self.bot.get_channel(848362560255950888)
        """Command which Loads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
            await logchannel.send(f'<:cross:848374065550458920> - {type(e).__name__} - {e}')

        else:
            await ctx.send('**`SUCCESS`**')
            await logchannel.send('<:check:848374065366433852> - Loading cog success')

    @commands.command(name='unload', hidden=True)
    @commands.is_owner()
    async def cogunload(self, ctx, *, cog: str):
        logchannel = self.bot.get_channel(848362560255950888)
        """Command which Unloads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
            await logchannel.send(f'<:cross:848374065550458920> - {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')
            await logchannel.send('<:check:848374065366433852> - Unloading cog success')

    @commands.command(name='reload', hidden=True)
    @commands.is_owner()
    async def cogreload(self, ctx, *, cog: str):
        logchannel = self.bot.get_channel(848362560255950888)
        """Command which Reloads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
            await logchannel.send(f'<:cross:848374065550458920> - {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')
            await logchannel.send('<:check:848374065366433852> - Reloading cog success')

    @commands.command(hidden=True)
    @commands.is_owner()
    async def shutdown(self, ctx):
        logchannel = self.bot.get_channel(848362560255950888)
        await ctx.send("<:check:848374065366433852> - Shutting down.")
        await logchannel.send('<:check:848374065366433852> - Bot has shut down successfully')
        await self.bot.change_presence(status=discord.Status.invisible)
        await self.bot.close()

    @commands.command(hidden=True)
    @commands.is_owner()
    async def print(self, ctx, *, args):
        """Prints to terminal"""
        await ctx.channel.purge(limit=1)
        await ctx.send("Sent to console.\n**```" + "".join(args) + "```**", delete_after=5)
        print("".join(args))

    @commands.command(hidden=True)
    async def guildlist(self, ctx):
        """A list of the guilds I am in"""
        for guild in self.bot.guilds:
            if guild.member_count == "1":
                memberstr = "member"
            else:
                memberstr = "members"
            await ctx.send(f"ID: {guild.id} - {guild.name} | {guild.member_count} {memberstr}")

    @commands.command()
    @commands.is_owner()
    async def remind(self, ctx, *, content):
        """Reminds me stuff"""
        await ctx.message.delete()
        await ctx.send("Sent suggestion to <#845361102530281532>", delete_after=5)
        meta = self.bot.get_channel(845361102530281532)
        embed = discord.Embed(color=discord.Color.blurple(), description=content, timestamp=datetime.datetime.today())
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await meta.send("<@729135459405529118>", embed=embed)

def setup(bot):
    bot.add_cog(Owner(bot))
