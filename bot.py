import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from os import listdir
from os.path import isfile, join
import traceback

def get_prefix(bot, message):
    prefixes = ['o.']
    if not message.guild:
        return 'o.'
    return commands.when_mentioned_or(*prefixes)(bot, message)

cogs_dir = "cogs"
intents = discord.Intents.default()
intents.members = True
description = """Oscie Bot 3 is a multi-use bot, that has many uses. It uses discord.ext and a cog system. Thank you for using me :D"""
bot = commands.Bot(activity=discord.Activity(type=discord.ActivityType.streaming, name="Doing bot things", url="https://twitch.tv/0scie"), command_prefix=get_prefix, status=discord.Status.dnd, description=description, intents=intents)

if __name__ == '__main__':
    for extension in [f.replace('.py', '') for f in listdir(cogs_dir) if isfile(join(cogs_dir, f))]:
        try:
            bot.load_extension(cogs_dir + "." + extension)
        except (discord.ClientException, ModuleNotFoundError):
            print(f'Failed to load extension {extension}.')
            traceback.print_exc()

@bot.event
async def on_ready():
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')
load_dotenv()
bot.run(os.getenv("DISCORD_TOKEN"), bot=True, reconnect=True)

# Credit:
# .mii command | SketchMaster2001
# assistance | zurgeg
# more help | discord.gg/dpy