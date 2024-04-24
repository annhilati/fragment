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
    if isinstance(error, commands.MissingPermissions):
        await ctx.reply("Fehlende Berechtigung", mention_author=False)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply("Fehlende Argumente", mention_author=False)

#-------------------------------------------------#
#                  Sudo-Befehle                   #
#-------------------------------------------------#

@client.command()
async def sudo(ctx, arg1, arg2):
    log(f"[Sudo] {ctx.author.name} ({ctx.author.id}) executed \"{ctx.message.content}\" in {ctx.guild.name} ({ctx.guild.id})")
    if arg1 == "sync":
        if arg2 == client.user.id:
            await client.tree.sync()
        await ctx.message.add_reaction("✅")
        await ctx.reply(f"Es wurde eine Anfrage zur Synchronisation der App-Commands für alle Guilden versendet.\nDie Synchronisation kann einige Minuten bis Stunden dauern.", mention_author=False, silent=True, delete_after=10)
        log(f"[Conn] {ctx.author.name} ({ctx.author.id}) in {ctx.guild.name} ({ctx.guild.id}) requestes a global synchronization of all App-Commands. Synchronization can take several minutes to hours.")

#-------------------------------------------------#
#                 Hauptprogramm                   #
#-------------------------------------------------#

async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")
            log(f"[Cogs] cogs/{filename} is loaded")

async def main():
    load_dotenv() # Läd die Umgebungsvariabeln
    async with client:
        await load()
        await client.start(str(os.getenv("BOT_TOKEN")))

@client.event
async def on_ready():
    log(f"[Conn] Bot is connected")
    log(f"[Conn] Logged in as {client.user} (ID: {client.user.id})")

asyncio.run(main()) # Diese Zeile wird fortlaufend ausgeführt und sollte deswegen am Ende stehen