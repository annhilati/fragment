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
    await client.add_cog(Command_Tag(client))

class Command_Tag(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        log(f"[COGS] {__name__} is ready")

    #-------------------------------------------------#
    #                Tag-Supercommand                 #
    #-------------------------------------------------#

    @commands.command(aliases=["t"])
    async def tag(self, ctx, arg1=None):
        content = None
        didError = None

        if arg1 in ["discordmod", "dmod", "moddeddiscord", "discord-mod", "modded-discord"]:
            with open("assets/tags/modded-discord.md", 'r', encoding="UTF-8") as file:
                    content = f"{file.read()}"

        elif arg1 in ["protocolls", "ssh", "ftp"]:
            with open("assets/tags/protocolls.md", 'r', encoding="UTF-8") as file:
                    content = f"{file.read()}"

        elif arg1 in ["port"]:
            with open("assets/tags/port.md", 'r', encoding="UTF-8") as file:
                    content = f"{file.read()}"

        #-------------------------------------------------#
        #                     System                      #
        #-------------------------------------------------#

        elif arg1 == None:
            with open("assets/tags/.tags.md", 'r', encoding="UTF-8") as file:
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