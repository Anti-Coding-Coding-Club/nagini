import discord, abc

class Config(abc.ABC):
    """
    Nagini basic configurations.
    """


    NAGINI_VERSION = '2.0'
    NAGINI_LOGO_URL = 'https://preview.redd.it/76h72zxnc3a51.jpg?auto=webp&s=b9190c5ac58b2e92c3062841132e5141202946f1'
    EMBED_COLOR = discord.Colour.dark_purple()