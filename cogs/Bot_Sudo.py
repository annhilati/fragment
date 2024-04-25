import datetime
import discord
from discord.ext import commands, tasks

def log(text):
    return print("[" + datetime.datetime.now().strftime("%H:%M:%S") + "] " + text)

async def setup(client):
    await client.add_cog(Bot_Sudo(client))

class Bot_Sudo(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    #-------------------------------------------------#
    #                  Sudo-Befehle                   #
    #-------------------------------------------------#

    @commands.command()
    async def sudo(self, ctx, arg1=None, arg2=None):
        log(f"[Sudo] {ctx.author.name} ({ctx.author.id}) executed \"{ctx.message.content}\" in {ctx.guild.name} ({ctx.guild.id})")
        if arg1 == "sync":
            if arg2 == self.client.user.id:
                await self.client.tree.sync()
                await ctx.message.add_reaction("✅")
                await ctx.reply(f"Es wurde eine Anfrage zur Synchronisation der App-Commands für alle Guilden versendet.\nDie Synchronisation kann einige Minuten bis Stunden dauern.", mention_author=False, silent=True, delete_after=10)
                log(f"[Conn] {ctx.author.name} ({ctx.author.id}) in {ctx.guild.name} ({ctx.guild.id}) requestes a global synchronization of all App-Commands. Synchronization can take several minutes to hours.")
            elif arg2 == None
                raise commands.BadArgument("Hier wird ein Code erwartet")
            else:
                raise commands.BadArgument("Falscher Code")
        elif arg1 == None:
            raise commands.MissingRequiredArgument(param=commands.Parameter(name='arg1', annotation=str, kind=3))
        else:
            raise commands.MissingRequiredArgument(param=commands.Parameter(name='arg1', annotation=str, kind=3))

    @commands.Cog.listener()
    async def on_ready(self):
        log(f"[Cogs] Bot_Sudo is ready")