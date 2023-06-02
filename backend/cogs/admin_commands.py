from discord import slash_command, Interaction, Embed, ApplicationContext, User
from discord.ext.commands import Cog, Bot
from discord.ext import commands
from backend.misc.config import Config


class NaginiAdminCog(Cog):
    """
    Classe para métodos administrativos da Nagini.
    """
    def __init__(self, nagini: Bot):
        self.nagini = nagini


    @slash_command(name='kick', description='Removo um membro do servidor.')
    @commands.has_permissions(kick_members=True)
    async def kick_command(self, context: ApplicationContext, user: User, *, reason: str = 'Não especificado') -> None:
        """
        Nagini remove um membro do servidor.

        :params context: Discord application command interaction context.
        :params user: O usuário que deve ser removido.
        :params reason: Motivo pelo qual o usuário está sendo removido. default: 'Não especificado'

        :return None:
        """

        member = context.guild.get_member(user.id) or await context.guild.fetch_member(user.id)

        if member.guild_permissions.administrator:
            embed = Embed(title='Houston, temos um problema! 😶',
            description='O usuário tem permissões administrativas!',
            color=Config.EMBED_COLOR)
            await context.send(embed=embed)
        
        else:
            try:
                embed = Embed(title='Usuário removido! 😵',
                description=f'**{member}** foi removido por **{context.author}**!',
                color=Config.EMBED_COLOR)
                await context.send(embed=embed)

                try:
                    await member.send(f'Você foi removido port **{context.author}**!\nPelo motivo: {reason} 🕵🏻‍♀️')
                
                except Exception:
                    pass
                await member.kick(reason=reason)

            except Exception:
                embed = Embed(title='Hm... 🧐',
                description='Ocorreu um erro ao tentar remover o usuário. Verifique se meu cargo está acima ao do usuário que deseja remover!',
                color=Config.EMBED_COLOR)
                await context.send(embed=embed)


    @slash_command(name='ban', description='Aplico o lendário banhammer em um usuário do servidor.')
    @commands.has_permissions(ban_members=True)
    async def ban_command(self, context: ApplicationContext, user: User, *, reason: str = '💩') -> None:
        """
        Nagini bane um membro do servidor.

        :params context: Discord application command interaction context.
        :params user: O usuário que deve ser banido.
        :params reason: Motivo pelo qual o usuário está sendo banido. default: '💩'

        :return None:
        """

        member = context.guild.get_member(user.id) or await context.guild.fetch_member(user.id)

        try:
            if member.guild_permissions.administrator:
                embed = Embed(title='Jotto matte! 🙅🏻‍♀️',
                description='Boa tentativa espertinho! Este membro é um administrador.',
                color=Config.EMBED_COLOR)
                await context.send(embed=embed)

            else:
                embed = Embed(title='BANHAMMER ATRIBUÍDO 🔨',
                description=f'**{member}** sentiu o peso do martelo de **{context.author}** e foi de Americanas 💀',
                color=Config.EMBED_COLOR)
                embed.add_field(name='Motivo:', value=reason)
                await context.send(embed=embed)

                try:
                    await member.send(f'Você foi banido por **{context.author}**\nMotivo: {reason}')

                except Exception: 
                    pass
                await member.ban(reason=reason)

        except Exception:
            embed = Embed(title='Ora, ora...', description='Não consegui banir o usuário. Veja se o meu cargo é superior ao do usuário.',
            color=Config.EMBED_COLOR)
            await context.send(embed=embed)


    @slash_command(name='hackban', description='Bano um usuário do Discord que não está no servidor.')
    @commands.has_permissions(ban_members=True)
    async def hackban_command(self, context: ApplicationContext, user_id: str, *, reason: str = '💩') -> None:
        """
        Nagini bane um usuário do Discord que não está no servidor.

        :params context: Discord application command interaction context.
        :params user_id: A id do usuário que deve ser banido.
        :params reason: Motivo pelo qual o usuário está sendo banido. default: '💩'

        :return None:
        """

        try:
            await self.nagini.http.ban(user_id, context.guild.id, reason=reason)
            user = self.nagini.get_user(int(user_id)) or await self.nagini.fetch_user(int(user_id))
            embed = Embed(title='BANHAMMER INTERDIMENSIONAL APLICADO',
            description=f'**{user} (ID: {user_id})** foi de arrasta pra cima sem nem entrar no servidor graças a **{context.author}**',
            color=Config.EMBED_COLOR)
            embed.add_field(name='Motivo:', value=reason)
            await context.send(embed=embed)

        except Exception:
            embed = Embed(title='Ih!',
            description='Ocorreu um erro... Verifique se o ID está correto!',
            color=Config.EMBED_COLOR)
            await context.send(embed=embed)


    @slash_command(name='purge', description='Excluo uma quantidade de mensagens do canal de texto.',
    aliases='clear')
    @commands.has_guild_permissions(manage_messages=True)
    async def purge_command(self, context: ApplicationContext, quantity: int) -> None:
        """
        Nagini exclui um numero determinado de mensagens do canal de texto.

        :params context: Discord application command interaction context.
        :params quantity: A quantidade de mensagens a ser excluídas.

        :return None:
        """

        # Refatorar para uma linha apenas
        return_msg = 'mensagens' if quantity > 1 else 'mensagem'

        purged_msg = await context.channel.purge(limit=quantity)
        embed = Embed(title='Hora da faxina! 🧹',
        description=f'**{context.author}** chamou a equipe de limpeza e removeu {quantity} {return_msg}!',
        color=Config.EMBED_COLOR)

        await context.send(embed=embed)


    @slash_command(name='nick', description='Altero o apelido de um membro do servidor!')
    @commands.has_permissions(manage_nicknames=True)
    async def nick_command(self, context: ApplicationContext, user: User, *, nickname: str = None) -> None:
        """
        Nagini altera o apelido de um usuário do servidor.

        :params context: Discord application command interaction context.
        :params user: O usuário que deve ter o apelido alterado.
        :params nickname: O novo apelido que deve ser atribuído ao usuário.

        :return None:
        """
        
        member = context.guild.get_member(user.id) or await context.guild.fetch_member(user.id)

        try:
            await member.edit(nick=nickname)
            embed = Embed(title='Apelido alterado!',
            description=f'**{member}** agora se chama **{nickname}**!', color=Config.EMBED_COLOR)
            await context.send(embed=embed)
        
        except:
            embed = Embed(title='Oh no! 😐',
            description='Aconteceu um problema ao alterar o apelido... Verifique se meu cargo está acima ao do membro.',
            color=Config.EMBED_COLOR)
            await context.send(embed=embed)
