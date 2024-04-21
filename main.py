from dotenv import load_dotenv
import os

import discord
from discord.ext import commands

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@client.event
async def on_ready():
    print("Bot is connected")

@client.command()
async def ping(ctx):
    await ctx.send("Pong")

load_dotenv()
client.run(str(os.getenv("BOT_TOKEN")))