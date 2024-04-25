import discord
from discord.ext import commands

class BotErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.reply(f"<:Info:1233093266916773991> Ein Argument entsprach nicht den Erwartungen: {error}", mention_author=False)

        elif isinstance(error, commands.MissingPermissions):
            await ctx.reply(f"<:Info:1233093266916773991> Dir fehlt die Berechtigung dazu", mention_author=False)
        
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.reply(f"<:Info:1233093266916773991> Es muss ein weiteres Argument angegeben werden.", mention_author=False)

        #-------------------------------------------------#
#                Error-Handling                   #
#-------------------------------------------------#

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.reply(f"<:Info:1233093266916773991> Ein Argument entsprach nicht den Erwartungen: {error}", mention_author=False)
    if isinstance(error, commands.MissingPermissions):
        await ctx.reply(f"<:Info:1233093266916773991> Dir fehlt die Berechtigung dazu", mention_author=False)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply(f"<:Info:1233093266916773991> Es muss ein weiteres Argument angegeben werden.", mention_author=False)

# Funktion, um den Cog zum Bot hinzuzufügen
def setup(bot):
    bot.add_cog(BotErrorHandler(bot))