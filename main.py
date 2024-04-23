import asyncio
import datetime
import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
from itertools import cycle
import os

def log(text):
    return print("[" + datetime.datetime.now().strftime("%H:%M:%S") + "] " + text)

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# @client.event
# async def on_command_error(ctx, error):
#     if isinstance(error, commands.MissingRequiredArgument):
#         await ctx.send("Please pass in all requirements")
#     if isinstance(error, commands.MissingPermissions):
#         await ctx.send("You dont have all the requirements")

@client.command()
async def tree_sync(ctx):
    await client.tree.sync()
    log("[Conn] App Commands have been synchronized by someone")


############ Laden der Cogs

async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")
            log(f"[Cogs] cogs/{filename} is loaded")

############ Ausführung

async def main():
    load_dotenv() # Läd die Umgebungsvariabeln
    async with client:
        await load()
        await client.start(str(os.getenv("BOT_TOKEN")))

@client.event
async def on_ready():
    log(f"[Conn] Bot is connected")
    log(f"[Conn] Logged in as {client.user} (ID: {client.user.id})")

asyncio.run(main())