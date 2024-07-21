import datetime
import discord
from discord import app_commands
from discord.ext import commands
from acemeta import log

async def setup(bot):
    await bot.add_cog(App_Member(bot))

class App_Member(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    #-------------------------------------------------#
    #          Benutzerdetails-Kontextpunkt           #
    #-------------------------------------------------#

        self.ctx_menu = app_commands.ContextMenu(
            name='Benutzerdetails anzeigen',
            callback=self.user_details)
        self.bot.tree.add_command(self.ctx_menu)
    async def cog_unload(self) -> None:
        self.bot.tree.remove_command(self.ctx_menu.name, type=self.ctx_menu.type)


    @app_commands.guild_only()
    async def user_details(self, interaction: discord.Interaction, member: discord.Member) -> None:
        
        # Embed
        if member.bot == False:
            user_details = discord.Embed(title=f"{member.global_name}",
                                     description=f"Username: `{member}`\nID: `{member.id}`",
                                     color=member.top_role.color)
        else:
            user_details = discord.Embed(title=f"{member.name} <:VerifiedApp1:1233353807182827584><:VerifiedApp2:1233353808743239690>",
                                     description=f"Username: `{member}`\nID: `{member.id}`",
                                     color=discord.Color.blurple())
        user_details.set_thumbnail(url=member.avatar)
        user_details.add_field(name=f"<:Invite:1233105955038957578> Account erstellt",
                               value=f"Am {discord.utils.format_dt(member.created_at)}")
        user_details.add_field(name=f"<:NewMember:1233106416781230181> {member.guild.name} beigetreten",
                               value=f"Am {discord.utils.format_dt(member.joined_at)}")
        
        user_details.add_field(name="  ", value="  ", inline=False) # Dieses Feld sorgt für eine Lücke zwischen den Reihen
        if member.timed_out_until != None:
            user_details.add_field(name=f"<:Timeout:1233356546717515826> Timeout",
                                   value=f"Bis <t:{str(member.timed_out_until.timestamp())[:-4]}:R>",)
        else:
            user_details.add_field(name=f"<:Timeout:1233356546717515826> Timeout",
                                   value=f"Nicht im Timeout",)
        
        await interaction.response.send_message(embed = user_details)

    ######### 
        
    @commands.Cog.listener()
    async def on_ready(self):
        log(f"[COGS] {__name__} is ready")