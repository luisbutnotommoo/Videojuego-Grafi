import pygame
import os
import tkinter.messagebox as mbox

ruta_carpeta_audios = os.path.dirname(__file__)

class MP3:

    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.canal_ambiente = pygame.mixer.Channel(0)
        self.canal_personaje = pygame.mixer.Channel(1)

        self.sonido_ambiente=None
        self.sonido_personaje=None

    def __set_archivo__(self,nombre_audio,canal):
        ruta_archivo=os.path.join(ruta_carpeta_audios, nombre_audio)
        if ruta_archivo is not None:
            if canal==0:
                self.sonido_ambiente = pygame.mixer.Sound(ruta_archivo)
            if canal==1:
                self.sonido_personaje = pygame.mixer.Sound(ruta_archivo)
        else:
            mbox.showwarning(title="Alerta",message="No se encontro el sonido")

    def detener_sonido(self,canal):
        if canal==0:
            self.canal_ambiente.stop()
        if canal==1:
            self.canal_personaje.stop()
    
    def reproducir_sonido_fondo(self,nombre_sonido):
        if nombre_sonido is not None:
            self.__set_archivo__(nombre_sonido,0)
        if not self.canal_ambiente.get_busy():
             self.canal_ambiente.play(self.sonido_ambiente,loops=-1)
        

    def reproducir_sonido_personaje(self,nombre_sonido):
        self.__set_archivo__(nombre_sonido,1)
        if not self.canal_personaje.get_busy():
            self.canal_personaje.play(self.sonido_personaje)
        