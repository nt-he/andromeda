import discord
from discord.ext import commands

class Errors(commands.Cog):
    """This cog only contains information about errors and how to handle them.
    Nothing to see here!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        logchannel = self.bot.get_channel(848362560255950888)
        if isinstance(error, commands.DisabledCommand):
            await logchannel.send(f"<:cross:848374065550458920> - Error: Command is disabled")
            await ctx.send(f"<:cross:848374065550458920> - Sorry, that command is disabled.")
        elif isinstance(error, commands.MissingRequiredArgument):
            await logchannel.send(f"<:cross:848374065550458920> - Error: Missing Required Arguments")
            await ctx.send(f"<:cross:848374065550458920> - Sorry, you forgot some important information when running that command.")
        elif isinstance(error, commands.CommandNotFound):
            await logchannel.send(f"<:cross:848374065550458920> - Error: Command cannot be found")
            await ctx.send(f"<:cross:848374065550458920> - Sorry, that command is not a valid command.")
        elif isinstance(error, commands.NoPrivateMessage):
            await logchannel.send(f"<:cross:848374065550458920> - Error: Command is guild only")
            await ctx.send(f"<:cross:848374065550458920> - Sorry, that command can only be used in servers.")
        elif isinstance(error, commands.BadArgument):
            await logchannel.send(f"<:cross:848374065550458920> - Error: I recieved a bad argument")
            await ctx.send(f"<:cross:848374065550458920> - I recieved a bad argument.")
        elif isinstance(error, commands.MessageNotFound):
            await logchannel.send(f"<:cross:848374065550458920> - Error: Message not found")
            await ctx.send(f"<:cross:848374065550458920> - Sorry, I cannot find that message.")
        elif isinstance(error, commands.UserNotFound):
            await logchannel.send(f"<:cross:848374065550458920> - Error: User not found")
            await ctx.send(f"<:cross:848374065550458920> - Sorry, I cannot find that user.")
        elif isinstance(error, commands.MemberNotFound):
            await logchannel.send(f"<:cross:848374065550458920> - Error: Member not found")
            await ctx.send(f"<:cross:848374065550458920> - Sorry, I cannot find that member.")
        elif isinstance(error, commands.ChannelNotFound):
            await logchannel.send(f"<:cross:848374065550458920> - Error: cannot find specified channel")
            await ctx.send(f"<:cross:848374065550458920> - Sorry, I cant find that channel.")
        elif isinstance(error, commands.ChannelNotReadable):
            await logchannel.send(f"<:cross:848374065550458920> - Error: Cannot read channel")
            await ctx.send(f"<:cross:848374065550458920> - Sorry, I cannot read messages in that channel")
        elif isinstance(error, commands.RoleNotFound):
            await logchannel.send(f"<:cross:848374065550458920> - Error: Role not found")
            await ctx.send(f"<:cross:848374065550458920> - Sorry, I cannot find that role.")
        elif isinstance(error, commands.EmojiNotFound):
            await logchannel.send(f"<:cross:848374065550458920> - Error: Specified emoji cannot be found")
            await ctx.send(f"<:cross:848374065550458920> - Sorry, I cannot find that emoji.")
        elif isinstance(error, commands.PrivateMessageOnly):
            await logchannel.send(f"<:cross:848374065550458920> - Error: Command can only be used in private messages")
            await ctx.send(f"<:cross:848374065550458920> - Sorry, that command can only be used in DMs")
        elif isinstance(error, commands.NotOwner):
            await logchannel.send(f"<:cross:848374065550458920> - Error: User is not owner")
            await ctx.send(f"<:cross:848374065550458920> - Sorry, this command can only be used by the bot's owner")
        elif isinstance(error, commands.MissingPermissions):
            await logchannel.send(f"<:cross:848374065550458920> - Error: Author does not have permission to run Command")
            await ctx.send(f"<:cross:848374065550458920> - Sorry, you do not have the correct permissions to run that command.")
        elif isinstance(error, commands.BotMissingPermissions):
            await logchannel.send(f"<:cross:848374065550458920> - Error: I do not have permission in **`{ctx.guild}`**")
            await ctx.send(f"<:cross:848374065550458920> - Sorry, I do not have permission to run that.")
        elif isinstance(error, commands.MissingRole):
            await logchannel.send(f"<:cross:848374065550458920> - Error: Author does not have the right role")
            await ctx.send(f"<:cross:848374065550458920> - Sorry, you do not have the role that is needed to use that command.")
        elif isinstance(error, commands.CommandOnCooldown):
            await logchannel.send(f"<:cross:848374065550458920> - Error: Command is on cooldown")
            await ctx.send(f"<:cross:848374065550458920> - Sorry, that command is on cooldown.")
        else:
            raise error

def setup(bot):
    bot.add_cog(Errors(bot))