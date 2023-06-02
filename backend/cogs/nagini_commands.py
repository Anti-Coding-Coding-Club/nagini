import discord
import platform
from discord import slash_command, Interaction, Embed, ApplicationCommand
from discord.ext.commands import Cog, Bot
import random
import json
import datetime
import logging

logger = logging.getLogger(__name__)

from backend.misc.config import Config

with open('./backend/misc/data.json') as file:
    data = json.load(file)


class NaginiCommandsCog(Cog):
    def __init__(self, nagini: Bot):
        self.nagini = nagini


    @slash_command(name='info', description='Informações gerais...')
    async def info_command(self, interaction: Interaction) -> None:
        now = datetime.datetime.today()
        nagini_bday = '06-08-2022'

        embed = Embed(title='Minhas informações pessoais', color=Config.EMBED_COLOR)
        embed.add_field(name='Servidores que estou:', value=f'🔺 `{len(self.nagini.guilds)}`', inline=False)
        embed.add_field(name='Minha versão atual:', value=f'✨ `{Config.NAGINI_VERSION}`', inline=False)
        embed.add_field(name='Desenvolvida por:', value='🔶 `@shinilol1`', inline=False)
        embed.add_field(name='🏓 Pong!', value=f'Minha latência está em {round(self.nagini.latency * 1000)}ms.', inline=False)
        embed.set_footer(text=f'Versão do Python: 3.11.2')
        if now.strftime('%d-%m-%Y') == nagini_bday:
            embed.add_field(name='Hoje é meu aniversário!', value='🥳 🎊', inline=False)
        embed.set_thumbnail(url=Config.NAGINI_LOGO_URL)

        await interaction.respond(embed=embed)

    @slash_command(name='serverinfo', description='Informações gerais do servidor.')
    async def server_command(self, context: ApplicationCommand) -> None:
        now = datetime.datetime.today()
        server_bday = context.guild.created_at.strftime('%d-%m-%Y')

        roles = [role.name for role in context.guild.roles]

        if len(roles) > 50:
                roles = roles[:50]
                roles.append(f'> Exibindo[50/{len(roles)}] cargos')

        roles = ", ".join(roles)
        embed = Embed(title=f'Informações sobre {context.guild}', color=Config.EMBED_COLOR)

        if context.guild.icon is not None:
            embed.set_thumbnail(url = context.guild.icon.url)
        
        embed.add_field(name='ID', value=context.guild.id, inline=False)
        embed.add_field(name='Membros', value=context.guild.member_count, inline=False)
        embed.add_field(name=f'Cargos ({len(context.guild.roles)})', value=roles, inline=False)
        embed.add_field(name=f'Invite:', value='https://discord.gg/qhdD4eVfmb', inline=False)
        embed.set_footer(text=f'Criado em: {context.guild.created_at.strftime("%d-%m-%Y")}')
        
        if now.strftime('%d-%m-%Y') == server_bday:
            embed.add_field(name='Hoje é aniversário do servidor!', value='🥳 🎊', inline=False)

        await context.respond(embed=embed)


    @slash_command(name='quote', decription='Conto um segredo...')
    async def quote_command(self, context: ApplicationCommand) -> None:
        quotes = data["quotes"]

        await context.respond(random.choice(quotes))

    @slash_command(name='commands', description='Mostro a lista de comandos.')
    async def commands_command(self, interaction: Interaction) -> None:
        embed = Embed(title='Comandos Disponíveis', color=Config.EMBED_COLOR)
        embed.add_field(name='/commands', value='Mostro a lista de comandos.', inline=False)
        embed.add_field(name='/info', value='Mostro minhas informações.', inline=False)
        embed.add_field(name='/serverinfo', value='Mostro as informações do servidor.', inline=False)
        embed.add_field(name='/kick', value='Removo um membro do servidor.', inline=False)
        embed.add_field(name='/nick', value='Altero o apelido de algum membro.', inline=False)
        embed.add_field(name='/ban', value='Aplico o lendário banhammer em um membro.', inline=False)
        embed.add_field(name='/purge', value='Deleto uma quantidade x de mensagens no canal de texto.', inline=False)
        embed.add_field(name='/hackband', value='Sento o banhammer em algum desavisado fora do servidor.', inline=False)
        embed.add_field(name='/quote', value='Conto um segredo meu.', inline=False)

        embed.set_footer(text=f'Versão atual: {Config.NAGINI_VERSION}')
        await interaction.respond(embed=embed)