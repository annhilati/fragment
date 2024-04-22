from dotenv import load_dotenv
import discord
from discord.ext import commands

import os
import random

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@client.event
async def on_ready():
    print("Bot is connected")

@client.command()
async def ping(ctx):
    await ctx.send("Pong")

@client.command()
async def magic_eightball(ctx, *, question):
    with open("discord-bot/magic_eightball.txt", "r") as f:
        random_responses = f.readlines()
        response = random.choice(random_responses)
    await ctx.send(response)

load_dotenv()
client.run(str(os.getenv("BOT_TOKEN")))