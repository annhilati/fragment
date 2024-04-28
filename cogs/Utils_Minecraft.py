import base64
import datetime
import discord
from discord import app_commands
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
    await client.add_cog(Utils_Minecraft(client))


class Utils_Minecraft(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        log(f"[COGS] Utils_Minecraft is ready")

    #-------------------------------------------------#
    #                   Serverping                    #
    #-------------------------------------------------#

    # Embed

    @app_commands.command(name="minecraftserver", description="Erhalte Details über einen Minecraft-Server")
    async def ping(self, interaction: discord.Interaction, server_ip: str):
        server = JavaServer.lookup(server_ip)
        status = server.status()
        query = server.query()

        server_details = discord.Embed(title=f"{server_ip}",
                                     description=f"desc",
                                     color=discord.Color.blurple())
        #server_details.set_thumbnail(url=status.icon)
        # user_details.add_field(name=f"<:Invite:1233105955038957578> Account erstellt",
        #                        value=f"Am {discord.utils.format_dt(member.created_at)}")
        # user_details.add_field(name=f"<:NewMember:1233106416781230181> {member.guild.name} beigetreten",
        #                        value=f"Am {discord.utils.format_dt(member.joined_at)}")
        
        # user_details.add_field(name="  ", value="  ", inline=False) # Dieses Feld sorgt für eine Lücke zwischen den Reihen
        # if member.timed_out_until != None:
        #     user_details.add_field(name=f"<:Timeout:1233356546717515826> Timeout",
        #                           value=f"Bis <t:{str(member.timed_out_until.timestamp())[:-4]}:R>",)
        # else:
        #     user_details.add_field(name=f"<:Timeout:1233356546717515826> Timeout",
        #                            value=f"Nicht im Timeout",)

        await interaction.response.send_message(embed=server_details)

        