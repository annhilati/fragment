import datetime
import discord
from discord.ext import commands
import numexpr
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
    await client.add_cog(Command_Tag(client))

class Command_Tag(commands.Cog):
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
            await ctx.reply(f"{expression} = {answer}")
        except:
            raise commands.BadArgument("Ungültiger Ausdruck")