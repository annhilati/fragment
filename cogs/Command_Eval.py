import datetime
import discord
from discord.ext import commands
from numpy import *
import numexpr


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
    await client.add_cog(Command_Eval(client))

class Command_Eval(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        log(f"[COGS] {__name__} is ready")

    #-------------------------------------------------#
    #                  Eval-Command                   #
    #-------------------------------------------------#

    @commands.command(aliases=["calc", "solve"])
    async def eval(self, ctx, *, expression: str):
        try:
            answer = numexpr.evaluate(expression)
            await ctx.reply(f"```\n>>> {expression}\n= {answer}```", mention_author=False)
        except:
            raise commands.BadArgument("Ungültiger Ausdruck. Es wird ein algebraischer Term erwartet")