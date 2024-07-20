import discord
from discord.ext import commands
import json
import os
import requests

from lib.system import *

class Whitelist(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.whitelist_path = os.path.join('data', 'whitelist.json')
        self.load_whitelist()

    def load_whitelist(self):
        if os.path.exists(self.whitelist_path):
            with open(self.whitelist_path, 'r') as f:
                self.whitelist = json.load(f)
        else:
            self.whitelist = []

    def save_whitelist(self):
        with open(self.whitelist_path, 'w') as f:
            json.dump(self.whitelist, f, indent=4)

    def is_in_whitelist(self, name):
        return any(entry['name'] == name for entry in self.whitelist)

    def get_minecraft_uuid(self, name):
        response = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{name}")
        if response.status_code == 200:
            data = response.json()
            return data['id']
        return None

    @commands.command(name='whitelist')
    async def whitelist_add(self, ctx, cmd=None, name=None):
        if cmd == "add":
            if self.is_in_whitelist(name):
                await ctx.reply(f"{name} ist bereits in der Whitelist.", mention_author=False, suppress_embeds=True)
                return
            
            uuid = self.get_minecraft_uuid(name)
            if uuid is None:
                await ctx.reply(f"{name} ist kein registrierter Minecraft-Name.", mention_author=False, suppress_embeds=True)
                return
            
            self.whitelist.append({'name': name, 'uuid': uuid})
            self.save_whitelist()
            await ctx.send(f"{name} wurde zur Whitelist hinzugefügt.")
        elif cmd == "list":
            await ctx.reply(f"```json\n{getfiletext("data/whitelist.json")}```", mention_author=False, suppress_embeds=True)
        elif cmd == None:
            raise commands.MissingRequiredArgument(param=commands.Parameter(name='cmd', annotation=str, kind=3))
        else:
            raise commands.BadArgument(f"Unbekannter Befehl: {cmd}")

    @commands.Cog.listener()
    async def on_ready(self):
        log(f"[COGS] {__name__} is ready")

async def setup(bot):
    await bot.add_cog(Whitelist(bot))