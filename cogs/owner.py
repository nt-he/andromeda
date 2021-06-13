import discord
from discord.ext import commands
from os import listdir
from os.path import join, isfile
from discord_components import Button
import asyncio
import datetime
class Owner(commands.Cog):
    """Commands that only the owner of the bot can see.
    Mainly just cog maintenence stuff."""

    def __init__(self, bot):
        self.bot = bot
        self.tasks = ""
    global interaction
    # Hidden means it won't show up on the default help.
    @commands.command(name='load', hidden=True)
    @commands.is_owner()
    async def cog_load(self, ctx, *, cog: str):
        """Command which Loads a Module."""
        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')

    @commands.command(name='unload', hidden=True)
    @commands.is_owner()
    async def cog_unload(self, ctx, *, cog: str):
        """Command which Unloads a Module."""
        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')

    @commands.command(name='reload', hidden=True)
    @commands.is_owner()
    async def cog_reload(self, ctx, *, cog: str):
        """Command which Reloads a Module."""
        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')


    @commands.command(hidden=True)
    @commands.is_owner()
    async def shutdown(self, ctx):
        """Shuts down the bot in a bad way"""
        logchannel = self.bot.get_channel(848362560255950888)
        await ctx.send("<:check:848374065366433852> - Shutting down.")
        await logchannel.send('<:check:848374065366433852> - Bot has shut down successfully')
        await self.bot.change_presence(status=discord.Status.invisible)
        await self.bot.close()

    @commands.command(hidden=True)
    @commands.is_owner()
    async def print(self, ctx, *, args):
        """Prints the content of the message to console"""
        await ctx.channel.purge(limit=1)
        await ctx.send("Sent to console.\n**```" + "".join(args) + "```**", delete_after=5)
        print("".join(args))

    @commands.command()
    #@commands.is_owner()
    async def privatemsg(self, ctx, *, content):
        """DMs the pinged member"""
        await ctx.message.delete()
        member = ctx.message.mentions[0]
        await member.send(content)
    
    @commands.command()
    #@commands.is_owner()
    async def multiplemsg(self, ctx, times: int, *, content):
        """Sends many messages in DMs"""
        member = ctx.message.mentions[0]

        await ctx.message.delete()

        for i in range(times):
            await member.send("".join(content))

    @commands.command()
    @commands.is_owner()
    async def ownerhelp(self, ctx):
        """Sends all the owner commands"""
        await ctx.send("""```
Oscie Bot 3 is a multi-use bot, that has many uses. It uses discord.ext and a cog system. Thank you for using me :D

These are commands that only the owner of the bot can see.
Mainly just cog maintenence stuff.

  load          Loads the specified cog
  unload        Unloads the specified cog
  reload        Reloads the specified cog
  shutdown      Shuts down the bot in a bad way
  print         Prints the content of the message to console
  guildlist     Sends all the guilds the bot is in
  privatemsg    DMs the pinged member
  multiplemsg   Sends many messages in DMs
  
Type o.help for a list of public commands.
You can also type o.help command for more info on an owner command.
```""", delete_after=20)

def setup(bot):
    bot.add_cog(Owner(bot))
