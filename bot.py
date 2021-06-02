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
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')

load_dotenv()
bot.run(os.getenv("DISCORD_TOKEN"), bot=True, reconnect=True)