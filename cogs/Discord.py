import datetime
import discord
from discord.ext import commands

def log(text):
    return print("[" + datetime.datetime.now().strftime("%H:%M:%S") + "] " + text)

class Discord(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        log(f"[Cogs] Discord is ready")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong!")


async def setup(client):
    await client.add_cog(Discord(client))
