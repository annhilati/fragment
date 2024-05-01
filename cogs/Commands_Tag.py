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
    async def tag(self, ctx, arg1=None):
        content = None
        didError = None

        if arg1 in ["discordmod", "dmod", "moddeddiscord", "discord-mod", "modded-discord"]:
            with open("cogs/tags/modded-discord.md", 'r', encoding="UTF-8") as file:
                    content = f"{file.read()}"

        elif arg1 in ["protocolls", "ssh", "ftp"]:
            with open("cogs/tags/protocolls.md", 'r', encoding="UTF-8") as file:
                    content = f"{file.read()}"

        elif arg1 in ["port"]:
            with open("cogs/tags/port.md", 'r', encoding="UTF-8") as file:
                    content = f"{file.read()}"

        #-------------------------------------------------#
        #                     System                      #
        #-------------------------------------------------#

        elif arg1 == None:
            with open("cogs/tags/.tags.md", 'r', encoding="UTF-8") as file:
                    content = f"{file.read()}"
        else:
            raise commands.BadArgument("Unbekannter Tag oder Tag-Kategorie")
            didError = True
        
        #-------------------------------------------------#
        #                      Aktion                     #
        #-------------------------------------------------#

        if didError != True:
            await ctx.message.delete()
            await ctx.send(f"{content}", mention_author=False, suppress_embeds=True)
        else:
            pass