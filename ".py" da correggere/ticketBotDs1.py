import discord
from discord.ext import commands

intens = discord.Intens.default()
intens.typing = False
intens.presences = False
description = "Ciao! L'autore di questo bot è RobertoFonzies! Il bot in questione ti sarà di aiuto nell'apertura dei ticket, un modo per metterti in contatto con l'assistenza."

bot = commands.Bot(command_prefix = "/", description=description, intens=intens)

@bot.event
async def on_ready():
    print(f"Siamo online come {bot.user}")