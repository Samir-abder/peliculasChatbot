import moviepy.editor
from tkinter.filedialog import *

def extraerAudio(video):
    video = moviepy.editor.VideoFileClip(video)
    audio = video.audio
    return audio


def pruebaTkinter():
    video = askopenfilename()
    audio = extraerAudio(video)
    audio.write_audiofile("sample.mp3")
    print("Completed!")