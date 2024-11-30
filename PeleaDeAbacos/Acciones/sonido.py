import pygame

pygame.init()
pygame.mixer.init()

def sonido(FileName):

    audio_file=FileName
    pygame.mixer.music.load(audio_file)
    pygame.mixer_music.play()
    
def stopsonido():
    pygame.mixer_music.stop()
    