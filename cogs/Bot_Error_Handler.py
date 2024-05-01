import datetime
import discord
from discord.ext import commands

#-------------------------------------------------#
#             Funktionsdefinitionen               #
#                     log()                       #
#-------------------------------------------------#

def log(text):
    return print("[" + datetime.datetime.now().strftime("%H:%M:%S") + "] " + text)

#-------------------------------------------------#
#                cog-Deklaration                  #
#-------------------------------------------------#

async def setup(client):
    await client.add_cog(Bot_Error_Handler(client))

class Bot_Error_Handler(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        log(f"[COGS] Bot_Error_Handler is ready")

    #-------------------------------------------------#
    #                Error-Handling                   #
    #-------------------------------------------------#

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(title=f"{error}", color=15774002)
            embed.set_author(name="Ein Argument entsprach nicht den Erwartungen", icon_url="https://cdn.discordapp.com/emojis/1233093266916773991.webp")
            await ctx.reply(embed = embed, mention_author=False)

        # elif isinstance(error, commands.MissingPermissions):
        #     embed = discord.Embed(title=f"{error}", color=15774002)
        #     embed.set_author(name="Dir fehlt die Berechtigung dazu", icon_url="https://cdn.discordapp.com/emojis/1233093266916773991.webp")
        #     await ctx.reply(embed = embed, mention_author=False)
        
        elif isinstance(error, commands.MissingRequiredArgument):
            #embed = discord.Embed(title=f"{error}", color=15774002)
            embed = discord.Embed(title=f"", color=15774002)
            embed.set_author(name="Es muss ein weiteres Argument angegeben werden.", icon_url="https://cdn.discordapp.com/emojis/1233093266916773991.webp")
            await ctx.reply(embed = embed, mention_author=False)
