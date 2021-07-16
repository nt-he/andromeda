from discord.ext import commands
import re

class Filter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        badwords = [re.compile(regex) for regex in open("badwords/en.txt").readlines()]
        for badword in badwords:
            if badword.search(message.content):
                await message.delete()
        await self.bot.process_commands(message)
def setup(bot):
    bot.add_cog(Filter(bot))