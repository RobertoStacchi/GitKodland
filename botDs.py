
import discord
from discord.ext import commands

# la variabile intents contiene i permessi al bot
intents = discord.Intents.default()
# abilita il permesso a leggere i contenuti dei messaggi
intents.message_content = True
# crea un bot e passa gli indents
client = discord.Client(intents=intents)
# descrizione del bot
description = "Ciao! Questo è il primo bot di RobertoFonzies! Il bot in questione ti sarà di aiuto in certe circostanze di assistenza tecnica, come l'apertura dei ticket.\nSpero che ti piaccia il mio bot!"

#Prefisso del bot e la sua struttura per eseguire delle istruzioni
bot = commands.Bot(command_prefix='/', description=description, intents=intents)

@client.event
async def on_ready():
    print(f'Abbiamo fatto l\'accesso come {client.user}')

#Omaggiare l'entrata del membro
@bot.command(name='ciao')
async def ciao(ctx):
    await ctx.send('Ciao!')

#Dare l'arrivederci al membro uscito    
@bot.command(name='arrivederci')
async def arrivederci(ctx):
    await ctx.send('\\U0001f642')

@bot.event
async def on_message(message):
    #Se il messaggio non rientra nelle automatizzazioni del bot, esso si ferma
    if message.author == bot.user:
        return
    #Prende il messaggio che è stato inviato e controlla se contiene un comando che il bot riconosce
    await bot.process_commands(message)

#Quando il membro entra
@bot.command
async def entrato(ctx, member: discord.Member):
    await ctx.send(f'{member.name} entra {discord.utils.format_dt(member.joined_at)}')

#Quando il membro esce
@bot.command
async def uscito(ctx, member: discord.Member):
    await ctx.send(f'{member.name} esce {discord.utils.format_dt(member.joined_at)}')

#Ripete il contenuto di un messaggio a piacere quante volte si vuole
@bot.command()
async def ripeti(ctx, times: int, content="ripetendo..."):
    for i in range(times):
        await ctx.send(content)

#Token del bot di Discord
client.run("TOKEN")
