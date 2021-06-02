import discord
from discord.ext import commands

from dotenv import load_dotenv

import os
from os import listdir
from os.path import isfile, join

import sys, traceback

def get_prefix(bot, message):
    """A callable Prefix for our bot. This could be edited to allow per server prefixes."""

    # Notice how you can use spaces in prefixes. Try to keep them simple though.
    prefixes = ['o.']

    # Check to see if we are outside of a guild. e.g DM's etc.
    if not message.guild:
        # Only allow ? to be used in DMs
        return 'o.'

    # If we are in a guild, we allow for the user to mention us or use any of the prefixes in our list.
    return commands.when_mentioned_or(*prefixes)(bot, message)

cogs_dir = "cogs"
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(activity=discord.Streaming(name="Doing bot things", url="https://twitch.tv/0scie"), command_prefix=get_prefix, status=discord.Status.dnd, description="Bot desc", intents=intents)

if __name__ == '__main__':
    for extension in [f.replace('.py', '') for f in listdir(cogs_dir) if isfile(join(cogs_dir, f))]:
        try:
            bot.load_extension(cogs_dir + "." + extension)
        except (discord.ClientException, ModuleNotFoundError):
            print(f'Failed to load extension {extension}.')
            traceback.print_exc()

@bot.event
async def on_ready():
    """http://discordpy.readthedocs.io/en/rewrite/api.html#discord.on_ready"""
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')

load_dotenv()
bot.run(os.getenv("DISCORD_TOKEN"), bot=True, reconnect=True)