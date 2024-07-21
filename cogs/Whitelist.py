import discord
from discord.ext import commands
import json
import os
import requests
from dotenv import load_dotenv
from acemeta import log, fileToStr, GitHub

load_dotenv()

repo = GitHub.Repository("annhilati/fragment", token=os.getenv("GH_TOKEN")) 

class Whitelist(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.filepath = os.path.join('temp', 'whitelist.json')
        self.load_whitelist()

    def load_whitelist(self):
        if repo.exists("data/whitelist.json"):
            repo.download("data/whitelist.json", "temp/whitelist.json", overwrite=True)

            if os.path.exists(self.filepath):
                with open(self.filepath, 'r') as f:
                    self.whitelist = json.load(f)
        else:
            with open(self.filepath, "w") as f:
                f.write("[]")
            self.whitelist = []

    def save_whitelist(self):
        with open(self.filepath, 'w') as f:
            json.dump(self.whitelist, f, indent=4)
        repo.upload("temp/whitelist.json", "data/whitelist.json", "Whitelist Sync", True)

    def inWhitelist(self, name):
        return any(entry['name'] == name for entry in self.whitelist)

    def getUUID(self, name):
        response = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{name}")
        if response.status_code == 200:
            data = response.json()
            return data['id']
        return None

    @commands.command(name='whitelist')
    async def whitelistCMD(self, ctx, cmd=None, name=None):
        if cmd == "add":
            if self.inWhitelist(name):
                await ctx.reply(f"{name} ist bereits in der Whitelist.", mention_author=False, suppress_embeds=True)
                return
            
            uuid = self.getUUID(name)
            if uuid is None:
                await ctx.reply(f"{name} ist kein registrierter Minecraft-Name.", mention_author=False, suppress_embeds=True)
                return
            
            self.whitelist.append({'name': name, 'uuid': uuid})
            try:
                self.save_whitelist()
            except FileExistsError: ...                    
            await ctx.reply(f"{name} wurde zur Whitelist hinzugefügt.", mention_author=False, suppress_embeds=True)
        
        elif cmd == "remove":
            if not self.inWhitelist(name):
                await ctx.reply(f"{name} ist nicht in der Whitelist.", mention_author=False, suppress_embeds=True)
                return
            
            self.whitelist = [entry for entry in self.whitelist if entry['name'] != name]
            try:
                self.save_whitelist()
            except FileExistsError: ... 
            await ctx.reply(f"{name} wurde von der Whitelist entfernt.")

        elif cmd == "list":
            await ctx.reply(f"```json\n{fileToStr("temp/whitelist.json")}```", mention_author=False, suppress_embeds=True)
        
        elif cmd == None:
            raise commands.MissingRequiredArgument(param=commands.Parameter(name='cmd', annotation=str, kind=3))
        
        else:
            raise commands.BadArgument(f"Unbekannter Befehl: {cmd}\nVerwende `add`, `remove` und `list`")

    @commands.Cog.listener()
    async def on_ready(self):
        log(f"[COGS] {__name__} is ready")

async def setup(bot):
    await bot.add_cog(Whitelist(bot))