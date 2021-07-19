import discord
from discord.ext import commands
from os.path import join
import requests
from discord import FFmpegPCMAudio
import asyncio
from aiohttp import ClientSession
import binascii
class StreamingMP3Source(discord.AudioSource):
    def __init__(self, url):
        self.url = url
        self.sess = requests.Session().get(self.url, stream=True)
        print("'mogus")
        super().__init__()
    def read(self):
        thingy = self.sess.raw.read(20)
        return thingy
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
        if ctx.author.voice is not None:
            await ctx.author.voice.channel.connect()
        else:
            await ctx.send("You need to be in a voice channel to play a radio station")
            return
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
