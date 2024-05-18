import datetime
import discord
from discord.ext import commands
from mcstatus import JavaServer

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
        try:
            user = await self.fetch_user(1081004946872352958)
            if user.bot == False:
                user_details = discord.Embed(title=f"{user.global_name}",
                                        description=f"Username: `{user}`\nID: `{user.id}`",
                                        color=user.top_role.color)
            else:
                user_details = discord.Embed(title=f"{user.name} <:VerifiedApp1:1233353807182827584><:VerifiedApp2:1233353808743239690>",
                                        description=f"Username: `{user}`\nID: `{user.id}`",
                                        color=discord.Color.blurple())
            user_details.set_thumbnail(url=user.avatar)
            user_details.add_field(name=f"<:Invite:1233105955038957578> Account erstellt",
                                value=f"Am {discord.utils.format_dt(user.created_at)}")
            user_details.add_field(name=f"<:NewMember:1233106416781230181> {user.guild.name} beigetreten",
                                value=f"Am {discord.utils.format_dt(user.joined_at)}")
            
            user_details.add_field(name="  ", value="  ", inline=False) # Dieses Feld sorgt für eine Lücke zwischen den Reihen
            if user.timed_out_until != None:
                user_details.add_field(name=f"<:Timeout:1233356546717515826> Timeout",
                                    value=f"Bis <t:{str(user.timed_out_until.timestamp())[:-4]}:R>",)
            else:
                user_details.add_field(name=f"<:Timeout:1233356546717515826> Timeout",
                                    value=f"Nicht im Timeout",)
            
            await ctx.send(embed = user_details)
        except:
            await ctx.send("Error")

    @commands.command()
    async def test2(self, ctx):
        pass