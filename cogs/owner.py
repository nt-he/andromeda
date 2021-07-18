import discord
from discord.ext import commands

from time import time
import os
import sys
from inspect import getsource
from bot import db
import models
import traceback
import dotenv
from pprint import pprint
from io import StringIO
class Owner(commands.Cog):
    """Commands that only the owner of the bot can see.
    Mainly just cog maintenence stuff."""

    def __init__(self, bot):
        self.bot = bot
        dotenv.load_dotenv()
        self.trusted_users = os.environ.get("TRUSTED_USERS").split(',') if os.environ.get("TRUSTED_USERS") else [self.bot.owner_id]
        self.trusted_users = [int(i) for i in self.trusted_users]
    @commands.command(name='load', hidden=True)
    @commands.is_owner()
    async def cogload(self, ctx, *, cog: str):
        """Command which Loads a Module."""
        logchannel = self.bot.get_channel(854010015199133727)
        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
            embed = discord.Embed(color=0x7289DA, description="<:cross:848374065550458920> - Failed to load cog")
            await logchannel.send(embed=embed)
        else:
            await ctx.send('**`SUCCESS`**')
            embed = discord.Embed(color=0x7289DA, description="<:check:848374065366433852> - Loaded cog successfully")
            await logchannel.send(embed=embed)


    @commands.command(name='unload', hidden=True)
    @commands.is_owner()
    async def cogunload(self, ctx, *, cog: str):
        """Command which Unloads a Module."""
        logchannel = self.bot.get_channel(854010015199133727)
        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
            embed = discord.Embed(color=0x7289DA, description="<:cross:848374065550458920> - Failed to unload cog")
            await logchannel.send(embed=embed)
        else:
            await ctx.send('**`SUCCESS`**')
            embed = discord.Embed(color=0x7289DA, description="<:check:848374065366433852> - Unloaded cog successfully")
            await logchannel.send(embed=embed)


    @commands.command(name='reload', hidden=True)
    @commands.is_owner()
    async def cogreload(self, ctx, *, cog: str):
        """Command which Reloads a Module."""
        logchannel = self.bot.get_channel(854010015199133727)
        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
            embed = discord.Embed(color=0x7289DA, description="<:cross:848374065550458920> - Failed to reload cog")
            await logchannel.send(embed=embed)
        else:
            await ctx.send('**`SUCCESS`**')
            embed = discord.Embed(color=0x7289DA, description="<:check:848374065366433852> - Reloaded cog successfully")
            await logchannel.send(embed=embed)


    @commands.command(hidden=True)
    @commands.is_owner()
    async def shutdown(self, ctx):
        """Shuts down the bot in a bad way"""
        logchannel = self.bot.get_channel(854010015199133727)
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


    @commands.command(hidden=True)
    @commands.is_owner()
    async def privatemsg(self, ctx, *, content):
        """DMs the pinged member"""
        await ctx.message.delete()
        member = ctx.message.mentions[0]
        await member.send(content)

    
    @commands.command(hidden=True)
    @commands.is_owner()
    async def multiplemsg(self, ctx, times: int, *, content):
        """Sends many messages in DMs"""
        member = ctx.message.mentions[0]

        await ctx.message.delete()

        for i in range(times):
            await member.send("".join(content))

        
    @commands.group(hidden=True, invoke_without_subcommand=True)
    @commands.is_owner()
    async def status(self, ctx):
        """Set the bot's status"""

    @status.command()
    @commands.is_owner()
    async def streaming(self, ctx):
        await ctx.send("Setting status to Streaming", delete_after=5)
        await self.bot.change_presence(activity=discord.Streaming(name="Bot Things", url="https://www.youtube.com/watch?v=uVRHh8Jxtp0"), status=discord.Status.dnd)
    @status.command()
    @commands.is_owner()
    async def listen(self, ctx):
        await ctx.send("Setting status to Listening", delete_after=5)
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="To the Beat"))
    @status.command()
    @commands.is_owner()
    async def watch(self, ctx):
        await ctx.send("Setting status to Watching", delete_after=5)
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you sleep..."))
    @status.command()
    @commands.is_owner()
    async def compete(self, ctx):
        await ctx.send("Setting status to Competing", delete_after=5)
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name="no thoughts, head empty"))
    @status.command()
    @commands.is_owner()
    async def online(self, ctx):
        await ctx.send("Setting status to Online", delete_after=5)
        await self.bot.change_presence(status=discord.Status.online)
    @status.command()
    @commands.is_owner()
    async def invisible(self, ctx):
        await ctx.send("Setting status to Invisible", delete_after=5)
        await self.bot.change_presence(status=discord.Status.invisible)
    @status.command()
    @commands.is_owner()
    async def idle(self, ctx):
        await ctx.send("Setting status to Idle", delete_after=5)
        await self.bot.change_presence(status=discord.Status.idle)
    @status.command()
    @commands.is_owner()
    async def donotdisturb(self, ctx):
        await ctx.send("Setting status to Do not Disturb", delete_after=5)
        await self.bot.change_presence(status=discord.Status.dnd)


    def resolve_variable(self, variable):
        if hasattr(variable, "__iter__"):
            var_length = len(list(variable))
            if (var_length > 100) and (not isinstance(variable, str)):
                return f"<a {type(variable).__name__} iterable with more than 100 values ({var_length})>"
            elif (not var_length):
                return f"<an empty {type(variable).__name__} iterable>"
        
        if (not variable) and (not isinstance(variable, bool)):
            return f"<an empty {type(variable).__name__} object>"
        return (variable if (len(f"{variable}") <= 1000) else f"<a long {type(variable).__name__} object with the length of {len(f'{variable}'):,}>")
    

    def prepare(self, string):
        arr = string.strip("```").replace("py\n", "").replace("python\n", "").split("\n")
        if not arr[::-1][0].replace(" ", "").startswith("return"):
            arr[len(arr) - 1] = "return " + arr[::-1][0]
        return "".join(f"\n\t{i}" for i in arr)
    

    @commands.command(pass_context=True, aliases=['eval', 'exec', 'evaluate'], hidden=True)
    @commands.is_owner()
    async def _eval(self, ctx, *, code: str):
        silent = ("-s" in code)
        
        code = self.prepare(code.replace("-s", ""))
        args = {
            "discord": discord,
            "sauce": getsource,
            "sys": sys,
            "os": os,
            "imp": __import__,
            "this": self,
            "ctx": ctx
        }
        
        try:
            exec(f"async def func():{code}", args)
            a = time()
            response = await eval("func()", args)
            if silent or (response is None) or isinstance(response, discord.Message):
                del args, code
                return
            
            await ctx.send(f"```py\n{self.resolve_variable(response)}````{type(response).__name__} | {(time() - a) / 1000} ms`")
        except Exception as e:
            await ctx.send(f"Error occurred:```\n{type(e).__name__}: {str(e)}```")
        
        del args, code, silent

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
  privatemsg    DMs the pinged member
  multiplemsg   Sends many messages in DMs
  status        Changes the bot's status (GROUP)
  eval          Run Python code from Discord
  
Type o.help for a list of public commands.
You can also type o.help command for more info on an owner command.
```""", delete_after=20)
    @commands.command()
    @commands.is_owner()
    async def cache(self, ctx, user: discord.User):
        """Caches a user's info into a database."""
        u = db.session.query(models.CachedUser).get(id=user.id) if db.session.query(models.CachedUser).get(id=user.id) else models.CachedUser(id=user.id)
        u.name = user.name
        u.discriminator = user.discriminator
        db.session.add(u)
        db.session.commit()
        await ctx.send("Cached user.")

    @commands.command()
    async def eval_sql(self, ctx, *, code: str):
        """Evaluates a SQL statement"""
        if ctx.author.id in self.trusted_users:
            try:
                out = db._engine.execute(code)
            except Exception as e:
                await ctx.send(f"An error has occured:\n```{e}```")
                return
            out_dict = out.__dict__
            output = StringIO()
            pprint(out_dict, stream=output)
            await ctx.send(f"```py\n{output.getvalue()}```")
        else:
            await ctx.send("You are not allowed to use this command.")

        


def setup(bot):
    bot.add_cog(Owner(bot))
