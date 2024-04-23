import asyncio
import datetime
import discord
from discord import app_commands
from discord.ext import commands, tasks
from dotenv import load_dotenv
from itertools import cycle
import os

def timestamp():
    return "[" + datetime.datetime.now().strftime("%H:%M:%S") + "]"

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# @client.event
# async def on_command_error(ctx, error):
#     if isinstance(error, commands.MissingRequiredArgument):
#         await ctx.send("Please pass in all requirements")
#     if isinstance(error, commands.MissingPermissions):
#         await ctx.send("You dont have all the requirements")

############ Apps

@client.tree.context_menu(name='Show Join Date')
async def show_join_date(interaction: discord.Interaction, member: discord.Member):
    # The format_dt function formats the date time into a human readable representation in the official client
    await interaction.response.send_message(f'{member} joined at {discord.utils.format_dt(member.joined_at)}')

############ Laden der Cogs

async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")
            print(timestamp(), f"[Cogs] cogs/{filename} is loaded")

############ Ausführung

async def main():
    load_dotenv() # Läd die Umgebungsvariabeln
    async with client:
        await load()
        await client.start(str(os.getenv("BOT_TOKEN")))

@client.event
async def on_ready():
    guilds_tree_sync = [1104421499827388566, 890190896530849792]
    for guild_id in guilds_tree_sync:
        guild = discord.Object(id=guild_id)
        await client.tree.sync(guild=guild)  # Synchronisiert für jeden Server in der Liste
    print(timestamp(), f"[Conn] Bot is connected")
    print(timestamp(), f"[Conn] Logged in as {client.user} (ID: {client.user.id})")

asyncio.run(main())