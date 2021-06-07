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
    async def cogload(self, ctx):
        logchannel = self.bot.get_channel(848362560255950888)
        """Command which Loads a Module.
        Remember to use dot path. e.g: cogs.owner"""
        components = []
        disabled_components = []
        index = 0 # For pangination, which I will implement soon
        for extension in [f.replace('.py', '') for f in listdir('cogs') if isfile(join('cogs', f))]:
            if 'cogs.' + extension not in self.bot.extensions:
                if len(components) >= 4:
                    index += 4
                    break
                components.append(Button(label=extension, style=3))
                disabled_components.append(Button(label=extension, style=3, disabled=True))
        if index == 4:
            components.append(Button(label='Next Page', style=1))
            disabled_components.append(Button(label='Next Page', style=1, disabled=True))
        message = await ctx.send(f'What extension do you want to load?', components=components)
        try:
            interaction = await self.bot.wait_for("button_click", timeout=10, check=lambda res: res.user.id == ctx.author.id and res.channel.id == ctx.channel.id) 
        except asyncio.TimeoutError:
            await message.delete()
            await ctx.send("You timed out and no cogs were loaded.", delete_after=5)
        if interaction.component.label != 'Next Page':
            try:
                self.bot.load_extension("cogs." + interaction.component.label)
            except Exception as e:
                await interaction.respond(content=f'**`ERROR:`** {type(e).__name__} - {e}')
                await message.edit(components=disabled_components)
            else:
                await interaction.respond(content=f'**`SUCCESS`**')
                await message.edit(components=disabled_components)
        else:
            # Pagination
            await interaction.respond(type=6)
            while True:
                components = []
                for extension in [f.replace('.py', '') for f in listdir('cogs')[index:] if isfile(join('cogs', f))]:
                    if 'cogs.' + extension not in self.bot.extensions:
                        if len(components) == 4: break
                        print(extension)
                        components.append(Button(label=extension, style=3))
                        disabled_components.append(Button(label=extension, style=3, disabled=True))
                        index += 1
                if len(components) == 4:
                    components.append(Button(label='Next Page', style=1))
                    disabled_components.append(Button(label='Next Page', style=1, disabled=True))
                print("edit message")
                await message.edit(components=components)

                try:
                    interaction = await self.bot.wait_for("button_click", timeout=10, check=lambda res: res.user.id == ctx.author.id and res.channel.id == ctx.channel.id) 
                except asyncio.TimeoutError:
                    await message.delete()
                    await ctx.send("You timed out and no cogs were loaded.", delete_after=5)
                if interaction.component.label != 'Next Page':
                    try:
                        self.bot.load_extension("cogs." + interaction.component.label)
                    except Exception as e:
                        await interaction.respond(content=f'**`ERROR:`** {type(e).__name__} - {e}')
                        await message.edit(components=disabled_components)
                        break
                    else:
                        await interaction.respond(content=f'**`SUCCESS`**')
                        await message.edit(components=disabled_components)
                        break
                await interaction.respond(type=6)

    @commands.command(name='unload', hidden=True)
    @commands.is_owner()
    async def cogunload(self, ctx):
        components = []
        disabled_components = []
        index = 0 # For pangination, which I will implement soon
        for extension in self.bot.extensions:
            if len(components) >= 4:
                index += 4
                break
            components.append(Button(label=extension[5:], style=3))
            disabled_components.append(Button(label=extension[5:], style=3, disabled=True))
        if index == 4:
            components.append(Button(label='Next Page', style=1))
            disabled_components.append(Button(label='Next Page', style=1, disabled=True))
        message = await ctx.send(f'What extension do you want to unload?', components=components)
        try:
            interaction = await self.bot.wait_for("button_click", timeout=10, check=lambda res: res.user.id == ctx.author.id and res.channel.id == ctx.channel.id) 
        except asyncio.TimeoutError:
            await message.delete()
            await ctx.send("You timed out and no cogs were unloaded.", delete_after=5)
        if interaction.component.label != 'Next Page':
            try:
                self.bot.unload_extension("cogs." + interaction.component.label)
            except Exception as e:
                await interaction.respond(content=f'**`ERROR:`** {type(e).__name__} - {e}')
                await message.edit(components=disabled_components)
            else:
                await interaction.respond(content=f'**`SUCCESS`**')
                await message.edit(components=disabled_components)
        else:
            # Pagination
            await interaction.respond(type=6)
            while True:
                components = []
                for extension in list(self.bot.extensions.keys())[index:]:
                    if len(components) == 4: break
                    print(extension)
                    components.append(Button(label=extension[5:], style=3))
                    disabled_components.append(Button(label=extension[5:], style=3, disabled=True))
                    index += 1
                if len(components) == 4:
                    components.append(Button(label='Next Page', style=1))
                    disabled_components.append(Button(label='Next Page', style=1, disabled=True))
                print("edit message")
                await message.edit(components=components)

                try:
                    interaction = await self.bot.wait_for("button_click", timeout=10, check=lambda res: res.user.id == ctx.author.id and res.channel.id == ctx.channel.id) 
                except asyncio.TimeoutError:
                    await message.delete()
                    await ctx.send("You timed out and no cogs were loaded.", delete_after=5)
                if interaction.component.label != 'Next Page':
                    try:
                        self.bot.load_extension("cogs." + interaction.component.label)
                    except Exception as e:
                        await interaction.respond(content=f'**`ERROR:`** {type(e).__name__} - {e}')
                        await message.edit(components=disabled_components)
                        break
                    else:
                        await interaction.respond(content=f'**`SUCCESS`**')
                        await message.edit(components=disabled_components)
                        break
                await interaction.respond(type=6)

    @commands.command(name='reload', hidden=True)
    @commands.is_owner()
    async def cogreload(self, ctx):
        components = []
        disabled_components = []
        index = 0 # For pangination, which I will implement soon
        for extension in self.bot.extensions:
            if len(components) >= 4:
                index += 4
                break
            components.append(Button(label=extension[5:], style=3))
            disabled_components.append(Button(label=extension[5:], style=3, disabled=True))
        if index == 4:
            components.append(Button(label='Next Page', style=1))
            disabled_components.append(Button(label='Next Page', style=1, disabled=True))
        message = await ctx.send(f'What extension do you want to reload?', components=components)
        try:
            interaction = await self.bot.wait_for("button_click", timeout=10, check=lambda res: res.user.id == ctx.author.id and res.channel.id == ctx.channel.id) 
        except asyncio.TimeoutError:
            await message.delete()
            await ctx.send("You timed out and no cogs were reloaded.", delete_after=5)
        if interaction.component.label != 'Next Page':
            try:
                self.bot.unload_extension("cogs." + interaction.component.label)
                self.bot.reload_extension("cogs." + interaction.component.label)
            except Exception as e:
                await interaction.respond(content=f'**`ERROR:`** {type(e).__name__} - {e}')
                await message.edit(components=disabled_components)
            else:
                await interaction.respond(content=f'**`SUCCESS`**')
                await message.edit(components=disabled_components)
        else:
            # Pagination
            await interaction.respond(type=6)
            while True:
                components = []
                for extension in list(self.bot.extensions.keys())[index:]:
                    if len(components) == 4: break
                    print(extension)
                    components.append(Button(label=extension[5:], style=3))
                    disabled_components.append(Button(label=extension[5:], style=3, disabled=True))
                    index += 1
                if len(components) == 4:
                    components.append(Button(label='Next Page', style=1))
                    disabled_components.append(Button(label='Next Page', style=1, disabled=True))
                print("edit message")
                await message.edit(components=components)

                try:
                    interaction = await self.bot.wait_for("button_click", timeout=10, check=lambda res: res.user.id == ctx.author.id and res.channel.id == ctx.channel.id) 
                except asyncio.TimeoutError:
                    await message.delete()
                    await ctx.send("You timed out and no cogs were loaded.", delete_after=5)
                if interaction.component.label != 'Next Page':
                    try:
                        self.bot.load_extension("cogs." + interaction.component.label)
                    except Exception as e:
                        await interaction.respond(content=f'**`ERROR:`** {type(e).__name__} - {e}')
                        await message.edit(components=disabled_components)
                        break
                    else:
                        await interaction.respond(content=f'**`SUCCESS`**')
                        await message.edit(components=disabled_components)
                        break
                await interaction.respond(type=6)

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
    @commands.is_owner()
    async def remind(self, ctx, *, content):
        """Sends a message in my server to remind me"""
        await ctx.message.delete()
        await ctx.send("Sent suggestion to <#845361102530281532>", delete_after=5)
        meta = self.bot.get_channel(845361102530281532)
        embed = discord.Embed(color=discord.Color.blurple(), description=content, timestamp=datetime.datetime.today())
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        await meta.send("<@729135459405529118>", embed=embed)

    @commands.command()
    @commands.is_owner()
    async def ownerhelp(self, ctx):
        """Sends all the owner commands"""
        await ctx.send("```Oscie Bot 3 is a multi-use bot, that has many uses. It uses discord.ext and a cog system. Thank you for using me :D\n\nThese are commands that only the owner of the bot can see.\nMainly just cog maintenence stuff.\n\n  load          Loads the specified cog\n  unload        Unloads the specified cog\n  reload        Reloads the specified cog\n  shutdown      Shuts down the bot in a bad way\n  print         Prints the content of the message to console\n  guildlist     Sends all the guilds the bot is in\n  remind        Sends a message in my server to remind me\n\nType o.help for a list of public commands.\nYou can also type o.help command for more info on an owner command.```", delete_after=20)

def setup(bot):
    bot.add_cog(Owner(bot))
