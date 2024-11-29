import pygame as py

py.init()
py.mixer.init()

def play(filename):
    audio = filename
    py.mixer.music.load(audio)
    py.mixer.music.play()
    
def stop():
    py.mixer.music.stop()
    