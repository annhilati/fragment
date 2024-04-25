import datetime
import discord
from discord import app_commands
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
    await client.add_cog(Utils_Member(client))

class Utils_Member(commands.Cog):
    def __init__(self, client: commands.Bot) -> None:
        self.client = client

    #-------------------------------------------------#
    #          Benutzerdetails-Kontextpunkt           #
    #-------------------------------------------------#

        self.ctx_menu = app_commands.ContextMenu(
            name='Benutzerdetails anzeigen',
            callback=self.user_details)
        self.client.tree.add_command(self.ctx_menu)
    async def cog_unload(self) -> None:
        self.client.tree.remove_command(self.ctx_menu.name, type=self.ctx_menu.type)

    @app_commands.guild_only()
    async def user_details(self, interaction: discord.Interaction, member: discord.Member) -> None:
        if member.bot == False:
            user_details = discord.Embed(title=f"{member.global_name}",
                                     description=f"Username: `{member}`\nID: `{member.id}`",
                                     #color=discord.Color.blurple()
                                     color=member.color)
        else:
            user_details = discord.Embed(title=f"{member.name}",
                                     description=f"Username: `{member}`\nID: `{member.id}`",
                                     color=discord.Color.blurple())
        user_details.set_thumbnail(url=member.avatar)
        user_details.add_field(name=f"<:Invite:1233105955038957578> Account erstellt",
                               value=f"Am {discord.utils.format_dt(member.created_at)}")
        user_details.add_field(name=f"<:NewMember:1233106416781230181> {member.guild.name} beigetreten",
                               value=f"Am {discord.utils.format_dt(member.joined_at)}")
        await interaction.response.send_message(embed = user_details)

    ######### 
        
    @commands.Cog.listener()
    async def on_ready(self):
        log(f"[COGS] Utils_Member is ready")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong!")
