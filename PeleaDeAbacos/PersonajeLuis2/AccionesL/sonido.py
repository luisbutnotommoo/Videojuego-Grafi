import pygame
import os
from PersonajeLuis2.AccionesL import recursos
import threading


#ruta_actual = os.path.dirname(__file__)
ruta_actual = "PersonajeLuis2"

archivo = recursos.ambiente[0][2]

# Crear canales separados para los sonidos
canal_archivo = pygame.mixer.Channel(0)
canal_miaw = pygame.mixer.Channel(1)

# Locks para evitar conflictos de concurrencia
lock_archivo = threading.Lock()
lock_miaw = threading.Lock()

def set_archivo(index):
    global archivo
    archivo = recursos.ambiente[index][2]

def play():
    def play_thread():
        with lock_archivo:
            sonido = pygame.mixer.Sound(archivo)
            canal_archivo.play(sonido)
    
    threading.Thread(target=play_thread).start()
    
def stop():
    with lock_archivo:
        canal_archivo.stop()

def maullido(expresion):
    def maullido_thread():
        with lock_miaw:
            miaw = os.path.join(ruta_actual, 'Sonidos', f'miaw{expresion}.mp3')
            sonido_miaw = pygame.mixer.Sound(miaw)
            canal_miaw.play(sonido_miaw)
    
    threading.Thread(target=maullido_thread).start()