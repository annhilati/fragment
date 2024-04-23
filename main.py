import asyncio
import datetime
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

def timestamp():
    return "[" + datetime.datetime.now().strftime("%H:%M:%S") + "]"


client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

### Laden der Cogs
async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")
            print(timestamp(), f"[Cogs] cogs/{filename} is loaded")

### Ausführung
load_dotenv() # Läd die Umgebungsvariabeln
async def main():
    async with client:
        await load()
        await client.start(str(os.getenv("BOT_TOKEN")))

@client.event
async def on_ready():
    print(timestamp(), f"[Conn] Bot is connected")

asyncio.run(main())