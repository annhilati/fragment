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

def fix(text):
    return (text.encode("utf-8")).decode("utf-8")

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
    async def tag(self, ctx, arg1=None, arg2=None, arg3=None):
        content = None
        didError = None
        if arg1 == "law":

            if arg2 in ["discordmod", "dmod", "moddeddiscord", "discord-mod", "modded-discord"]:
                with open("cogs/tags/law_modded-discord.md", 'r') as file:
                    content = f"{arg3}\n{file.read()}"
                
        #-------------------------------------------------#
        #                  Error Raising                  #
        #-------------------------------------------------#

            elif arg2 == None:
                raise commands.MissingRequiredArgument(param=commands.Parameter(name='arg2', annotation=str, kind=3))
                didError = True
            else:
                raise commands.BadArgument("Unbekannter Tag")
                didError = True
        elif arg1 == None:
            raise commands.MissingRequiredArgument(param=commands.Parameter(name='arg1', annotation=str, kind=3))
            didError = True
        else:
            raise commands.BadArgument("Unbekannter Tag oder Tag-Kategorie")
            didError = True
        
        #-------------------------------------------------#
        #                      Aktion                     #
        #-------------------------------------------------#

        if didError == False:
            await ctx.message.delete()
            await ctx.send(f"{content}", mention_author=False, suppress_embeds=True)
        else:
            pass