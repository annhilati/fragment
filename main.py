from dotenv import load_dotenv
import discord
from discord.ext import commands
import asyncio
import os

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@client.event
async def on_ready():
    print("Bot is connected")

async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")
            print(f"{filename[:-3]} is loaded")

load_dotenv()
async def main():
    async with client:
        await load()
        await client.start(str(os.getenv("BOT_TOKEN")))

asyncio.run(main())