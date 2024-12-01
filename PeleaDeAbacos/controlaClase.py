import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
from Acciones import boceto as b
import sys
import os
from Acciones.boceto import PersonajesDeTodos
from menuPersonajesPruebas import SeleccionPersonaje
from PersonajeStarenka.claseEscenarioStar import PersonajeStarenka
#from PersonajeLuis.clasePrincipalLuis import PersonajeLuis
from PersonajeEmma.claseEmma import PersonajeEmma
#from PersonajeLin.machote.main_sincolision import MainLin
from Acciones.propiedadesPersonajes import Propiedades
from nivel2 import Nivel2
from nivel import Nivel1
import subprocess
directorio_script = os.path.dirname(os.path.abspath(__file__))

class controlaClase:
    def __init__(self):
        self.personajesJugables = []

    def main(self):
        while True:
            self.personajesJugables=[]
            menu = SeleccionPersonaje()
            menu.run()

            # Aquí puedes verificar si el menú fue cerrado
            if menu.bandera==1:  
                break  

            z = 0
            for i in range(2):
                if (i == 1):
                    z = 4
                if menu.guardado[i] == 0:
                    self.personajesJugables.append(z + menu.guardado[i])
                elif menu.guardado[i] == 1:
                    self.personajesJugables.append(z + menu.guardado[i])
                elif menu.guardado[i] == 2:
                    self.personajesJugables.append(z + menu.guardado[i])
                elif menu.guardado[i] == 3:
                    self.personajesJugables.append(z + menu.guardado[i])

            eleccion = Propiedades(self.personajesJugables)
            nivel1 = Nivel1(personajesJugables=eleccion.personajesJugables)
            nivel1.run()  # Ejecutar el nivel

if __name__ == "__main__":
    controlaClase().main()