import asyncio
import datetime
import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
import os

#-------------------------------------------------#
#             Funktionsdefinitionen               #
#                     log()                       #
#-------------------------------------------------#

def log(text):
    return print("[" + datetime.datetime.now().strftime("%H:%M:%S") + "] " + text)

#-------------------------------------------------#
#               Initialisierung                   #
#                 Botinstanz                      #
#-------------------------------------------------#

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

#-------------------------------------------------#
#                Error-Handling                   #
#-------------------------------------------------#

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.reply(f"Error BadArgument: {error}", mention_author=False)
    if isinstance(error, commands.MissingPermissions):
        await ctx.reply(f"Fehlende Berechtigung", mention_author=False)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply(f"Fehlende Argumente", mention_author=False)

#-------------------------------------------------#
#                 Hauptprogramm                   #
#-------------------------------------------------#

async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")
            log(f"[COGS] cogs/{filename} is loaded")

async def main():
    load_dotenv() # Läd die Umgebungsvariabeln
    async with client:
        await load()
        await client.start(str(os.getenv("BOT_TOKEN")))

@client.event
async def on_ready():
    log(f"[AUTH] Bot is connected")
    log(f"[AUTH] Logged in as {client.user} (ID: {client.user.id})")

asyncio.run(main()) # Diese Zeile wird fortlaufend ausgeführt und sollte deswegen am Ende stehen