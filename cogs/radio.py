from discord.ext import commands
from os.path import join

from discord.player import FFmpegOpusAudio
class Radio(commands.Cog):
    """Radio"""
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def tune_in(self, ctx, station):
        """Tune in to a radio station"""
        await ctx.send(f"Tuning in to {station}")
        # Internally, stations are stored as xxx_x.mp3, rather than xxx.x, so we need to replace dots with underscores
        station = station.replace('.', '_')
        station = station.replace("/", "") # Delete any slashes for safety
        # Now we create an audio source:
        src = FFmpegOpusAudio(source=join("radio", f"{station}.mp3"))
        if ctx.author.voice is not None:
            vc = await ctx.author.voice.channel.connect()
        else:
            await ctx.send("You need to be in a voice channel to play a radio station")
            return
        # Now we need to play:
        vc.play(src)

