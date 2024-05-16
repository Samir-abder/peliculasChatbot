import discord
from discord.ext import commands
import moviepy.editor

bot = commands.Bot(command_prefix='!')

def extraerAudio(video):
    video = moviepy.editor.VideoFileClip(video)
    audio = video.audio
    return audio

@bot.command()
async def convertir(ctx):
    video = ctx.message.attachments[0].url
    audio = extraerAudio(video)
    audio.write_audiofile("sample.mp3")
    await ctx.send("¡Audio convertido!")

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

bot.run('TU_TOKEN_DEL_BOT')
