import pygame
import os
import PersonajeLuis.AccionesLuis.recursos as recursos
import threading

pygame.init()
pygame.mixer.init()

ruta_actual = os.path.dirname(__file__)

archivo = recursos.ambiente[0][2]

# creamos canales separados para los sonidos
canal_archivo = pygame.mixer.Channel(0)
canal_miaw = pygame.mixer.Channel(1)

# hilos para evitar conflictos al reproducir
hilo_ambiente = threading.Lock()
hilo_miaw = threading.Lock()

# asignar sonido del ambiente
def set_archivo(index):
    global archivo
    archivo = recursos.ambiente[index][2]

def play():
    def play_thread():
        with hilo_ambiente:
            sonido = pygame.mixer.Sound(archivo)
            canal_archivo.play(sonido)
    
    threading.Thread(target=play_thread).start()
    
def stop():
    with hilo_ambiente:
        canal_archivo.stop()

# asignamos el sonido wav segun la expresion
def maullido(expresion):
    def maullido_thread():
        with hilo_miaw:
            miaw = os.path.join(ruta_actual, 'Sonidos', f'miaw{expresion}.wav')
            sonido_miaw = pygame.mixer.Sound(miaw)
            canal_miaw.play(sonido_miaw)
    
    threading.Thread(target=maullido_thread).start()