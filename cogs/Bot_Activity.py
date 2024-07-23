import discord
from discord.ext import commands, tasks
from itertools import cycle
from acemeta import log
from flask import Flask, jsonify
import threading

class Bot_Activity(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot_statuses = cycle(["mit der Discord-API", "mit Python-Bots"])  # Liste aller Bot-Status
        self.change_status.start()  # Startet den Bot-Status-Loop, wenn der Cog geladen wird

        # Flask-Server einrichten
        self.app = Flask(__name__)

        @self.app.route('/status')
        def status():
            return jsonify({"status": "Bot is online"}), 200

        # Starten des Flask-Servers in einem separaten Thread
        self.server_thread = threading.Thread(target=self.run_server)
        self.server_thread.start()

    def run_server(self):
        self.app.run(host='0.0.0.0', port=1324)

    @tasks.loop(seconds=5)
    async def change_status(self):
        # Ändert den Bot-Status
        await self.bot.change_presence(activity=discord.Game(next(self.bot_statuses)))

    @change_status.before_loop
    async def before_change_status(self):
        # Warte darauf, dass der Bot bereit ist, bevor der Loop startet
        await self.bot.wait_until_ready()

    @commands.Cog.listener()
    async def on_ready(self):
        log(f"[COGS] {__name__} is ready")

async def setup(bot):
    await bot.add_cog(Bot_Activity(bot))
