from discord.ext import commands
import python_weather
import asyncio
from dotenv import load_dotenv
import os

class Weather(commands.Cog):
    """Does weather stuff."""

    def __init__(self, bot):
        self.bot = bot

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

    if __name__ == "__main__":
        loop = asyncio.get_event_loop()
        loop.run_until_complete(getweather())
        loop.run_until_complete(getskytext())
        loop.run_until_complete(gettemp())
        loop.run_until_complete(getforecast())

def setup(bot):
    bot.add_cog(Weather(bot))