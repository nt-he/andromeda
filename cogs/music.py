import discord
from discord.ext import commands
import wavelink
import os
from dotenv import load_dotenv
import datetime
from discord.ext import commands
import discord
import sys
import youtube_dl
import ffmpeg

class Music(commands.Cog):
    """This cog will be for music commands in the future."""

    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def leave(self, ctx):
        """Disconnects the bot from the VC"""
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice != None:
            if voice.is_connected():
                await voice.disconnect()
                embed2 = discord.Embed(color=discord.Color.random(), description="I have now left the VC")
                embed2.set_author(name="oscie bot 2 voice", icon_url="https://oscie.tk/assets/Logo.png")
                await ctx.send(embed=embed2)
            else:
                await ctx.send("idk")  
        elif voice == None:
            embed2 = discord.Embed(color=discord.Color.random(), description="I am not in a VC")
            embed2.set_author(name="oscie bot 2 voice", icon_url="https://oscie.tk/assets/Logo.png")
            await ctx.send(embed=embed2)
        else:
            return

    @commands.command()
    async def play(self, ctx, url: str):
        """Plays the music - NOTHING OVER 15 MINUTES"""
        song_there = os.path.isfile("song.mp3")
        try:
            if song_there:
                os.remove("song.mp3")
        except PermissionError:
            await ctx.send("Wait for music to end or `o.stop` lol")
            return

        voiceChannel = discord.utils.get(ctx.guild.voice_channels, name="radio")
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice == None:
            await voiceChannel.connect()
            await ctx.send("It worked!")
        else:
            await ctx.send("im already in a vc")

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file, "song.mp3")

        if voice != None:
            voice.play(discord.FFmpegPCMAudio("song.mp3"))


    @commands.command()
    async def pause(self, ctx):
        """Pauses currently playing music"""
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice.is_playing():
            voice.pause()
            await ctx.send("music paused")
        else:
            await ctx.send("no music is playing")

    @commands.command()
    async def resume(self, ctx):
        """Resumes paused music"""
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice.is_paused():
            voice.resume()
            await ctx.send("resumed")
        else:
            await ctx.send("music isnt paused")

    @commands.command()
    async def stop(self, ctx):
        """Stops the current playing song"""
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        voice.stop()
        await ctx.send("music stopped")

def setup(bot):
    bot.add_cog(Music(bot))
