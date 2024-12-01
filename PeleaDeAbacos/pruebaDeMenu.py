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
from menuPrincipal2 import Menu
from menuNivel import MenuNivel
import subprocess
directorio_script = os.path.dirname(os.path.abspath(__file__))

class ControlaClase:
    def __init__(self):
        self.personajesJugables = []
        self.banderaSeleccion = True
        self.banderaNivel = True

    def main(self):
        while True:
            self.banderaNivel = True
            menu_principal = Menu()
            menu_principal.main()
            

            # Menú Principal
            

            # Bucle para manejar los niveles
            while self.banderaNivel:
                self.banderaSeleccion = True
                menu_nivel = MenuNivel()
                menu_nivel.main()
                # Menú de Niveles
                
                banderaNivel=False

                menu = SeleccionPersonaje()
                menu.run()
                self.banderaSeleccion=False
              


                            
if __name__ == "__main__":
    ControlaClase().main()
