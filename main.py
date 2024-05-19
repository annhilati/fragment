from lib.system import *
import asyncio
import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
import os

#-------------------------------------------------#
#               Initialisierung                   #
#                 Botinstanz                      #
#-------------------------------------------------#

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

#-------------------------------------------------#
#                 Hauptprogramm                   #
#-------------------------------------------------#

async def loadCogs():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")
            log(f"[COGS] cogs/{filename} is loaded")

async def main():
    load_dotenv() # Läd die Umgebungsvariabeln
    async with client:
        await loadCogs()
        await client.start(str(os.getenv("BOT_TOKEN")))

@client.event
async def on_ready():
    log(f"[AUTH] Bot is connected")
    log(f"[AUTH] Logged in as {client.user} (ID: {client.user.id})")

asyncio.run(main()) # Diese Zeile wird fortlaufend ausgeführt und sollte deswegen am Ende stehen