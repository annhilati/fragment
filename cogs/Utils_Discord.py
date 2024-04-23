import datetime
import discord
from discord import app_commands
from discord.ext import commands

def log(text):
    return print("[" + datetime.datetime.now().strftime("%H:%M:%S") + "] " + text)

async def setup(client):
    await client.add_cog(Utils_Discord(client))

class Utils_Discord(commands.Cog):
    def __init__(self, client: commands.Bot) -> None:
        self.client = client
        self.user_details = app_commands.ContextMenu(
            name='Benutzerdetails anzeigen',
            callback=self.show_join_date,
        )
        self.client.tree.add_command(self.user_details)

    async def cog_unload(self) -> None:
        self.client.tree.remove_command(self.user_details.name, type=self.user_details.type)

    @app_commands.guilds()
    async def show_join_date(self, interaction: discord.Interaction, member: discord.Member) -> None:
        await interaction.response.send_message(f'{member} joined at {discord.utils.format_dt(member.joined_at)}')
        
    @commands.Cog.listener()
    async def on_ready(self):
        log(f"[Cogs] Utils_Discord is ready")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong!")
