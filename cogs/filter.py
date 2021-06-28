from discord.ext import commands
import re

class Filter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    def on_message():
        badwords = [re.compile(regex) for regex in open("badwords/en.txt").readlines()]
        for badword in badwords:
            if badword.search(message.content):
                await message.delete()
        await bot.process_commands(message)