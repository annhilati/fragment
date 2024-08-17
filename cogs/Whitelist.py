import discord
from discord import app_commands
from discord.ext import commands
from acemeta import log, GitHub, fileToStr
import json
import os
import requests
from dotenv import load_dotenv

load_dotenv()
repo = GitHub.Repository("annhilati/fragment", token=os.getenv("GH_TOKEN")) 

class Whitelist(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.localdir = "temp/whitelist.json"
        self.load_whitelist()

    def load_whitelist(self):
        if not os.path.exists('temp'):
            os.makedirs('temp')
        if repo.exists("data/whitelist.json"):
            repo.download("data/whitelist.json", self.localdir, overwrite=True)

            if os.path.exists(self.localdir):
                with open(self.localdir, 'r') as f:
                    self.whitelist = json.load(f)
        else:
            with open(self.localdir, "w") as f:
                # Schreibe eine leere Liste als JSON in die Datei
                json.dump([], f)
            self.whitelist = []

    def save_whitelist(self):
        with open(self.localdir, 'w') as f:
            json.dump(self.whitelist, f, indent=4)
        repo.upload(self.localdir, "data/whitelist.json", "Whitelist Sync", True)

    def in_whitelist(self, playername):
        return any(entry['name'] == playername for entry in self.whitelist)

    def get_uuid(self, playername):
        response = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{playername}")
        if response.status_code == 200:
            data = response.json()
            return data['id']
        return None

    @app_commands.command(name="whitelist", description="Whitelist bearbeiten")
    @app_commands.describe(action="Aktion auswählen: add, remove, list", playername="Name des Spielers")
    @app_commands.choices(action=[
        app_commands.Choice(name="add", value="add"),
        app_commands.Choice(name="remove", value="remove"),
        app_commands.Choice(name="list", value="list")])
    async def whitelistCMD(self, interaction: discord.Interaction,
                           action: app_commands.Choice[str],
                           playername: str = None):
        
        #-------------------------------------------------#
        #                       add                       #
        #-------------------------------------------------#

        if action.value == "add":
            if playername is None:
                await interaction.response.send_message("Bitte gib einen Spielernamen an.", ephemeral=True)
                return
            
            if self.in_whitelist(playername):
                await interaction.response.send_message(f"{playername} ist bereits in der Whitelist.", ephemeral=True)
                return
            
            uuid = self.get_uuid(playername)
            if uuid is None:
                await interaction.response.send_message(f"{playername} ist kein registrierter Minecraft-Name.", ephemeral=True)
                return
            
            self.whitelist.append({'name': playername, 'uuid': uuid})
            try:
                self.save_whitelist()
            except Exception as e:
                await interaction.response.send_message(f"Fehler beim Speichern der Whitelist: {e}", ephemeral=True)
                return
            await interaction.response.send_message(f"{playername} wurde zur Whitelist hinzugefügt.", ephemeral=True)
        
        #-------------------------------------------------#
        #                      remove                     #
        #-------------------------------------------------#

        elif action.value == "remove":
            if playername is None:
                await interaction.response.send_message("Bitte gib einen Spielernamen an.", ephemeral=True)
                return

            if not self.in_whitelist(playername):
                await interaction.response.send_message(f"{playername} ist nicht in der Whitelist.", ephemeral=True)
                return
            
            self.whitelist = [entry for entry in self.whitelist if entry['name'] != playername]
            try:
                self.save_whitelist()
            except Exception as e:
                await interaction.response.send_message(f"Fehler beim Speichern der Whitelist: {e}", ephemeral=True)
                return
            await interaction.response.send_message(f"{playername} wurde von der Whitelist entfernt.", ephemeral=True)

        #-------------------------------------------------#
        #                       list                      #
        #-------------------------------------------------#

        elif action.value == "list":
            if not self.whitelist:
                await interaction.response.send_message("Die Whitelist ist leer.", ephemeral=True)
                return
            whitelist_str = fileToStr(self.localdir)
            await interaction.response.send_message(f"```json\n{whitelist_str}\n```", ephemeral=True)
        
        else:
            await interaction.response.send_message(f"Unbekannte Aktion: {action.value}. Verwende `add`, `remove` oder `list`.", ephemeral=True)

    @commands.Cog.listener()
    async def on_ready(self):
        log(f"[COGS] {__name__} is ready")

async def setup(bot):
    await bot.add_cog(Whitelist(bot))
