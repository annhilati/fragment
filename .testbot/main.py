from dotenv import load_dotenv
import discord
from discord.ext import commands, tasks
import asyncio

import os
import random
from itertools import cycle

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@client.event
async def on_ready():
    await client.tree.sync()
    print("Bot is connected")

@client.tree.command(name="ping", description="Text, Text und nochmal Text")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong")
    print("Hallo")

### Ausführung
load_dotenv() # Läd die Umgebungsvariabeln
async def main():
    async with client:
        await client.start(str(os.getenv("BOT_TOKEN")))

@client.event
async def on_ready():
    print(f"[Conn] Bot is connected")

asyncio.run(main())