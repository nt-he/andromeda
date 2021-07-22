from discord.ext import commands
from os.path import join
from discord.player import FFmpegOpusAudio
import discord
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
            await ctx.send(f"""**A serious error has occured**
Report this to <@{self.bot.owner_id}>, 
and send them this information:
> Line number: 41
> Reason: Bottom of if else hit
> Variables:
> Author VC: {ctx.author.voice.channel.id}
> Bot VC: {ctx.voice_client.channel.id}
""")
        # Now we need to play:
        ctx.voice_client.play(src, after=lambda e: print('Player error: %s' % e) if e else None)
    @commands.command()
    async def stop(self, ctx):
        """Disconnect from the radio station"""
        ctx.voice_client.stop()
        await ctx.voice_client.disconnect()
    @commands.command()
    async def join(self, ctx, *, channel: discord.VoiceChannel=None):
        """Join a voice channel"""
        if channel is None:
            channel = ctx.author.voice.channel
        if ctx.voice_client is not None:
            await ctx.voice_client.move_to(channel)
        else:
            await channel.connect()





def setup(bot):
    bot.add_cog(Radio(bot))
