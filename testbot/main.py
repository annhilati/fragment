from dotenv import load_dotenv
import discord
from discord.ext import commands, tasks

import os
import random
from itertools import cycle

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

bot_status = cycle(["1", "2", "3"])
@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(bot_status)))



@client.command()
async def ping(ctx):
    await ctx.send("Pong")

@client.command()
async def magic_eightball(ctx, *, question):
    with open("discord-bot/magic_eightball.txt", "r") as f:
        random_responses = f.readlines()
        response = random.choice(random_responses)
    await ctx.send(response)



@client.event
async def on_ready():
    print("Bot is connected")
    change_status.start()

load_dotenv()
client.run(str(os.getenv("BOT_TOKEN")))