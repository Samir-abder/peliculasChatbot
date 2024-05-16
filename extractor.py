import discord
from discord.ext import commands
import moviepy.editor

intents = discord.Intents.default()
intents.messages = True  #para que el bot pueda recibir mensajes

bot = commands.Bot(command_prefix='!', intents=intents)

def extraerAudio(video):
    video = moviepy.editor.VideoFileClip(video)
    audio = video.audio
    return audio

@bot.command()
async def convertir(ctx):
    video = ctx.message.attachments[0].url
    audio = extraerAudio(video)
    audio.write_audiofile("etsample.mp3")

    #Crea objeto discord.File con el archivo MP3
    audio_file = discord.File("etsample.mp3")

    #Enviar el archivo MP3 al channel
    await ctx.send(file=audio_file)

    await ctx.send("¡Audio convertido!")



@bot.command()
async def hola(ctx):
    await ctx.send('¡Hola mundo!')

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

bot.run('MTI0MDUyNjMxMjMzMDg4NzIzOA.G8hwA_.q3mM8ALAMaL22PaYVSO9CpTdrZHZ4GfjiF-wX0')
