import discord
from discord.ext import commands
from discord_components.button import Button
class Status(commands.Cog):
    """Commands that change the bot's status.
    Owner only!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def status(self, ctx):
        components = [
            Button(label="Streaming", id="streaming", style=1),
            Button(label="Do not Disturb", id="dnd", style=4),
            Button(label="Idle", id="idle", style=2),
            Button(label="Online", id="online", style=3),
            Button(label="Invisible", id="offline", style=2)
        ]
        message = await ctx.send("What would you like me to set my status to", components=components)
        try:
            interaction = await self.bot.wait_for("button_click", timeout=5, check=lambda res: res.user.id == ctx.author.id and res.channel.id == ctx.channel.id) 
        except:
            await ctx.send("You timed out and the status was not changed", delete_after=5)
            await message.delete()
        if interaction.component.id == "streaming":
            logchannel = self.bot.get_channel(848362560255950888)
            await self.bot.change_presence(activity=discord.Streaming(name="Doing bot things", url="https://www.youtube.com/watch?v=uVRHh8Jxtp0"), status=discord.Status.dnd)
            await interaction.respond(content="<:status:848563270134792242> - Status changed!")
            await logchannel.send("<:status:848563270134792242> - Status changed to **`Streaming`**")
            await message.delete()
        if interaction.component.id == "dnd":
            logchannel = self.bot.get_channel(848362560255950888)
            await self.bot.change_presence(activity=discord.Game(name="Doing bot things"), status=discord.Status.dnd)
            await interaction.respond(content="<:status:848563270134792242> - Status changed!")
            await logchannel.send("<:status:848563270134792242> - Status changed to **`Do not Disturb`**")
            await message.delete()
        if interaction.component.id == "idle":
            logchannel = self.bot.get_channel(848362560255950888)
            await self.bot.change_presence(activity=discord.Game(name="Doing bot things"), status=discord.Status.idle)
            await interaction.respond(content="<:status:848563270134792242> - Status changed!")
            await logchannel.send("<:status:848563270134792242> - Status changed to **`Idle`**")
            await message.delete()
        if interaction.component.id == "online":
            logchannel = self.bot.get_channel(848362560255950888)
            await self.bot.change_presence(activity=discord.Game(name="Doing bot things"), status=discord.Status.online)
            await interaction.respond(content="<:status:848563270134792242> - Status changed!")
            await logchannel.send("<:status:848563270134792242> - Status changed to **`Online`**")
            await message.delete()
        if interaction.component.id == "offline":
            logchannel = self.bot.get_channel(848362560255950888)
            await self.bot.change_presence(activity=discord.Game(name="Doing bot things"), status=discord.Status.offline)
            await interaction.respond(content="<:status:848563270134792242> - Status changed!")
            await logchannel.send("<:status:848563270134792242> - Status changed to **`Offline`**")
            await message.delete()

def setup(bot):
    bot.add_cog(Status(bot))