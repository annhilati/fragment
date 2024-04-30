import datetime
import discord
from discord.ext import commands
import os

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
    await client.add_cog(Commands_Tag(client))

class Commands_Tag(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        log(f"[COGS] Commands_Tag is ready")

    #-------------------------------------------------#
    #                Tag-Supercommand                 #
    #-------------------------------------------------#

    @commands.command()
    async def tag(self, ctx, arg1=None, arg2=None):
        content = None
        if arg1 == "law":
            if arg2 == "discordmod" or "dmod" or "moddeddiscord" or "discord-mod" or "modded-discord":
                with open("cogs/tags/law_modded-discord.md", 'r') as file:
                    content = file.read()
                

        #-------------------------------------------------#
        #                  Error Raising                  #
        #-------------------------------------------------#

            elif arg2 == None:
                raise commands.MissingRequiredArgument(param=commands.Parameter(name='arg2', annotation=str, kind=3))
                content = None
            else:
                raise commands.BadArgument("Unbekannter Tag")
                content = None
        elif arg1 == None:
            raise commands.MissingRequiredArgument(param=commands.Parameter(name='arg1', annotation=str, kind=3))
            content = None
        else:
            raise commands.BadArgument("Unbekannter Tag")
            content = None
        await ctx.reply(f"{content}", mention_author=False)