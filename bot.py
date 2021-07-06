import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from os import listdir
from os.path import isfile, join
import traceback
from bot_types import DbSession
from sqlalchemy import create_engine

load_dotenv()

db = DbSession(create_engine(os.getenv('SQLALCHEMY_URI')))

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

@bot.command()
async def credits(ctx):
    """Credits ig idk"""
    pfp = bot.user.avatar_url
    embed = discord.Embed(color=discord.Color.random(), title="Credits", description="People who I've stolen code from, taken ideas from or have helped me in development.")
    embed.set_author(name="oscie bot 3", icon_url=pfp)
    embed.add_field(name="People", value=f"""
<@667563245107937297> - Helped me with time formatting, stole a couple commands from them
<@650819889434591241> - Assisted me alot with errors and when I couldn't figure out the most stupidest shit ever and got buttons and other stuff working
<@302271402277339146> - [Took a couple ideas from them (sorry btw)](https://www.thediamondk.com/bot.html)
https://discord.gg/dpy - People there helped me quite a bit
<@729135459405529118> - My creator, who coded me
<@264081339316305920> - Telling me how much Python sucks
<@314142411247058946> - Helping me test some commands
{ctx.author.mention} - You, for using me""")
    await ctx.send(embed=embed)



@bot.command()
async def information(ctx):
    """Information about Oscie Bot 3"""
    noteslegal = "¹X signifies version.\nAs of 06/2021, there are 3 versions (1, 2 and 3).\n\n²Date of last update\nThis message will only be updated for an important reason, and we can make changes to this without informing you."

    linkslegal = "[Discord Terms of Service](https://dis.gd/terms) ・ [Discord Community Guidelines](https://discord.com/guidelines) ・ [Discord API Legal](https://discord.com/developers/docs/legal) ・ [Discord API Policy](https://discord.com/developers/docs/policy) ・ [Discord Privacy Policy](https://discord.com/privacy)\n\n[Bot Page](https://oscie.net/bot) ・ [Bot Invite Page](https://bot.oscie.net) ・ [Oscie Website](https://oscie.net)"

    desclegal = "By adding my bot (Oscie Bot X¹) to your guild, you allow me (as the owner) to see the guild name, description, icon, member count, and any other information disclosable by the Discord API. Read more about Discord API's Terms and Conditions at [Discord Developer Policy](https://discord.com/developers/docs/policy) and [Discord Developer Legal](https://discord.com/developers/docs/legal). You may only use this bot in a way that follows the discord guidelines and terms of service, read [Discord TOS](https://dis.gd/terms) for more info. Message last updated²: 2021.06.18.\n\nMessages and Audit Logs will only be monitored in ``no thoughts, head empty (804449200921509913)``"

    anembed = discord.Embed(color=0x7289DA, title="Important Information", description=desclegal)
    anembed.set_author(icon_url = bot.user.avatar_url, name = bot.user.name)
    anembed.add_field(name = "Notes needed", value = noteslegal)
    anembed.add_field(name = "Important Links", value = linkslegal)
    await ctx.send(f"{ctx.author.mention} :wave: Hey there! As you know, I am Oscie Bot 3! By running this, you would like to see this important information. Please read the embed below for that information you requested (it is also at the bottom of https://bot.oscie.net)", embed=anembed)

@bot.command()
async def invite(ctx):
    """Wanna invite my bot? Use this!"""
    await ctx.send("Hey there! Thank you for showing interest into me. To invite me, please use this link:\nhttps://discord.com/api/oauth2/authorize?client_id=848181143169925180&permissions=8&scope=bot")

@bot.command()
async def ping(ctx):
    """What is my ping?"""
    await ctx.send(f"{round(bot.latency * 1000)} ms. Suck on that C#")

@bot.command()
@commands.has_permissions(manage_guild=True, manage_messages=True)
async def say(ctx, *, args):
    """Repeats what you tell it to"""
    logchannel = bot.get_channel(854010015199133727)
    await ctx.channel.purge(limit=1)
    await ctx.send("".join(args))
    await logchannel.send(f"{ctx.author.mention} said {args}")

@bot.event
async def on_ready():
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')
if __name__ == '__main__':
    bot.run(os.getenv("DISCORD_TOKEN"), bot=True, reconnect=True)

# Credit:
# .mii command | SketchMaster2001
# assistance | zurgeg
# more help | discord.gg/dpy