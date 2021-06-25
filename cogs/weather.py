import python_weather
import asyncio
import os
import discord
import time

from discord.ext import tasks, commands
from dotenv import load_dotenv

class Weather(commands.Cog):
    """Does weather stuff."""

    def __init__(self, bot):
        self.bot = bot
        self.hourlyforecast.start()
        self.fivedayforecast.start()

    @tasks.loop(seconds=3600)
    async def hourlyforecast(self):
        await self.bot.wait_until_ready()
        load_dotenv()
        channel = self.bot.get_channel(806042609704501268)

        client = python_weather.Client(format=python_weather.METRIC)
        weather = await client.find(os.getenv("HOME_TOWN"))
        embed = discord.Embed(color=0x7289DA, title="Weather Update for `HOME_TOWN`", description=f"Last updated at: `{weather.current.date}`")
        embed.add_field(name="Sky", value=f"`{weather.current.sky_text}`", inline=True)
        embed.add_field(name="Temp", value=f"`{weather.current.temperature}°C`", inline=True)

        await channel.send("<@729135459405529118>", embed=embed)
        await client.close()

    @tasks.loop(seconds=345600)
    async def fivedayforecast(self):
        await self.bot.wait_until_ready()
        load_dotenv()
        channel = self.bot.get_channel(806042609704501268)

        client = python_weather.Client(format=python_weather.METRIC)
        weather = await client.find(os.getenv("HOME_TOWN"))
        embed = discord.Embed(color=0x7289DA, title="Forecast Update")

        for forecast in weather.forecasts:
            embed.add_field(name=forecast.day, value=f"Sky: `{forecast.sky_text}` - Temp: `{forecast.temperature}°C`\nLow: `{forecast.low}°C` - High: `{forecast.high}°C`\nPrecip: `{forecast.precip}`", inline=True)

        await channel.send("<@729135459405529118>", embed=embed)
        await client.close()

    @commands.command()
    async def getweather(self, ctx):
        """Gets weather - Won't be worked on"""

        client = python_weather.Client(format=python_weather.METRIC)

        load_dotenv()
        weather = await client.find(os.getenv("HOME_TOWN"))

        for forecast in weather.forecasts:
            await ctx.send(f"{str(forecast.date)} | {forecast.sky_text} | {forecast.temperature}")

        await client.close()

    @commands.command()
    async def gettemp(self, ctx):
        """Gets temp - Won't be worked on"""
        client = python_weather.Client(format=python_weather.METRIC)
        
        load_dotenv()
        weather = await client.find(os.getenv("HOME_TOWN"))

        await ctx.send(weather.current.temperature)

        await client.close()

    @commands.command()
    async def getskytext(self, ctx):
        """Gets Sky Text - Won't be worked on"""
        client = python_weather.Client(format=python_weather.METRIC)
        
        load_dotenv()
        weather = await client.find(os.getenv("HOME_TOWN"))

        await ctx.send(weather.current.sky_text)

        await client.close()

    @commands.command()
    async def getforecast(self, ctx):
        """Gets Forecast - Won't be worked on"""
        load_dotenv()
        client = python_weather.Client(format=python_weather.METRIC)
        weather = await client.find(os.getenv("HOME_TOWN"))

        await ctx.send(f"The current temperature is `{weather.current.temperature}°C`.\nThe sky seems `{weather.current.sky_text}` right now.")

        await client.close()

    @commands.command()
    async def areaforecast(self, ctx, *, place:str):
        """Gets Area Forecast - Won't be worked on"""
        load_dotenv()
        client = python_weather.Client(format=python_weather.METRIC)
        weather = await client.find(str(place))

        await ctx.send(f"The current temperature is `{weather.current.temperature}°C`.\nThe sky seems `{weather.current.sky_text}` right now.")

        await client.close()

    if __name__ == "__main__":
        loop = asyncio.get_event_loop()
        loop.run_until_complete(getweather())
        loop.run_until_complete(getskytext())
        loop.run_until_complete(gettemp())
        loop.run_until_complete(getforecast())
        loop.run_until_complete(areaforecast())
        loop.run_until_complete(hourlyforecast())
        loop.run_until_complete(fivedayforecast())

def setup(bot):
    bot.add_cog(Weather(bot))
    