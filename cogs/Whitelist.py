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
            repo.download("data/whitelist.json", "temp/whitelist.json", overwrite=True)

            if os.path.exists(self.filepath):
                with open(self.filepath, 'r') as f:
                    self.whitelist = json.load(f)
        else:
            with open(self.filepath, "w") as f:
                # Schreibe eine leere Liste als JSON in die Datei
                json.dump([], f)
            self.whitelist = []

    def save_whitelist(self):
        with open(self.filepath, 'w') as f:
            json.dump(self.whitelist, f, indent=4)
        repo.upload("temp/whitelist.json", "data/whitelist.json", "Whitelist Sync", True)

    def inWhitelist(self, playername):
        return any(entry['name'] == playername for entry in self.whitelist)

    def getUUID(self, playername):
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
        if action.value == "add":
            if self.inWhitelist(playername):
                await interaction.reply(f"{playername} ist bereits in der Whitelist.", mention_author=False, suppress_embeds=True)
                return
            
            uuid = self.getUUID(playername)
            if uuid is None or playername is None:
                await interaction.reply(f"{playername} ist kein registrierter Minecraft-Name.", mention_author=False, suppress_embeds=True)
                return
            
            self.whitelist.append({'playername': playername, 'uuid': uuid})
            try:
                self.save_whitelist()
            except FileExistsError: ...                    
            await interaction.reply(f"{playername} wurde zur Whitelist hinzugefügt.", mention_author=False, suppress_embeds=True)
        
        elif action.value == "remove":
            if not self.inWhitelist(playername):
                await interaction.reply(f"{playername} ist nicht in der Whitelist.", mention_author=False, suppress_embeds=True)
                return
            
            self.whitelist = [entry for entry in self.whitelist if entry['playername'] != playername]
            try:
                self.save_whitelist()
            except FileExistsError: ... 
            await interaction.reply(f"{playername} wurde von der Whitelist entfernt.", mention_author=False, suppress_embeds=True)

        elif action.value == "list":
            await interaction.reply(f"```json\n{fileToStr('temp/whitelist.json')}```", mention_author=False, suppress_embeds=True)
        
        elif action.value == None:
            raise commands.MissingRequiredArgument(param=commands.Parameter(playername='action.value', annotation=str, kind=3))
        
        else:
            raise commands.BadArgument(f"Unbekannter Befehl: {action.value}\nVerwende `add`, `remove` und `list`")

    @commands.Cog.listener()
    async def on_ready(self):
        log(f"[COGS] {__name__} is ready")

async def setup(bot):
    await bot.add_cog(Whitelist(bot))
