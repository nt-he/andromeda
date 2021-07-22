import discord
from discord.ext import commands
from os.path import join
import requests
from discord import FFmpegPCMAudio
from aiohttp import ClientSession
class StreamingMP3Source(discord.AudioSource):
    def __init__(self, url):
        self.url = url
        self.sess = requests.get(self.url, stream=True)
        self.buffers = []
        print("'mogus")
        super().__init__()
    def read(self):
        if len(self.buffers) < 5:
            # Buffer queue is not full.
            # Get more data.
            for n in range(0, 5 - len(self.buffers)):
                self.buffers.append(self.sess.raw.read(1764000))
        return self.buffers.pop()
    def is_opus(self):
        return False
    def cleanup(self):
        print("'mogus III")

class Radio(commands.Cog):
    """Radio"""
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def tune_in(self, ctx):
        """Tune in to a radio station"""
        # Now we create an audio source:
        
        src = StreamingMP3Source("http://antenna5stream.neotel.mk:8000/live128")
        if ctx.voice_client is None and ctx.author.voice is not None:
            await ctx.author.voice.channel.connect()
        elif ctx.voice_client is not None:
            pass # We're already in a voice channel
        elif ctx.author.voice.channel is None:
            await ctx.send("You need to be in a voice channel to play a radio station")
            return
        elif ctx.voice_client is not None:
            await ctx.voice.client.move_to(ctx.author.voice.channel)
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
        await ctx.send("Source created.")
        # Now we need to play:
        ctx.voice_client.play(src, after=lambda e: print('Player error: %s' % e) if e else None)
    @commands.command()
    async def tune_out(self, ctx):
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
