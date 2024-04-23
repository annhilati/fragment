import discord
from discord.ext import commands

class Discord(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Ping.py is ready!")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong!")


async def setup(client):
    await client.add_cog(Discord(client))