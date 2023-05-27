from discord import Intents, Activity, ActivityType, Game
from discord.ext.commands import Bot
import discord
import platform
import random
import json
import os
import logging
import dotenv

dotenv.load_dotenv()
token = str(os.getenv("TOKEN"))

from asyncio import run

with open('./backend/misc/data.json') as file:
    data = json.load(file)


class Nagini(Bot):
    def __init__(self):
        super().__init__(intents=Intents.all())

    def run(self):
        print('[*] Iniciando. . .')
        self.load_extension('backend.cogs')

        super().run(token, reconnect=True)
    
    async def on_ready(self):
        self.client_id = (await self.application_info()).id

        try:
            statuses = data["status"]
            await self.change_presence(activity=Game(random.choice(statuses),min=5))
        
        except: pass

        print(f'[*] Nagini online (lantencia: {self.latency*1000:,.0f} ms)')
        print(f'[*] Python: {platform.python_version()}')
        print(f'[*] Rodando em: {platform.system()}, {platform.release()}, {os.name}')
        print('--------------------------')
