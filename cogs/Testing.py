import datetime
import discord
from discord.ext import commands

#-------------------------------------------------#
#             Funktionsdefinitionen               #
#                     log()                       #
#-------------------------------------------------#

def log(text):
    return print("[" + datetime.datetime.now().strftime("%H:%M:%S") + "] " + text)

#-------------------------------------------------#
#                cog-Deklaration                  #
#-------------------------------------------------#

async def setup(client):
    await client.add_cog(Testing(client))


class Testing(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        log(f"[COGS] Testing is ready")

    #-------------------------------------------------#
    #                     Tests                       #
    #-------------------------------------------------#

    @commands.command()
    async def test(self, ctx):
        await ctx.send("https://discord.com/quests/1227767407154561034")
        await ctx.send("https://discord.com/quests/1218004004206804992")

    @commands.command()
    async def test2(self, ctx):
        embed = discord.Embed(color=15774002)
        embed.set_author(name="Es muss ein weiteres Argument angegeben werden.", icon_url="https://cdn.discordapp.com/emojis/1233093266916773991.webp")
        await ctx.send(embed = embed)