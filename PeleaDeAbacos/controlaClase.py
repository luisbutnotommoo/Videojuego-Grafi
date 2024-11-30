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
import subprocess
directorio_script = os.path.dirname(os.path.abspath(__file__))
def main():
    
 while True:  
    menu = SeleccionPersonaje()
    menu.run()
    
    if menu.bandera==1:  
        break  

    
    """ for i in range(2):
            if menu.guardado[i] == 0:
                personajeCorrer = PersonajeEmma()
            elif menu.guardado[i] == 1:
                personajeCorrer = PersonajeLuis()
            elif menu.guardado[i] == 2:
                personajeCorrer = MainLin()
            elif menu.guardado[i] == 3:
                personajeCorrer = PersonajeStarenka()
            

            personajeCorrer.run()  # Ejecutamos el personaje"""


if __name__ == "__main__":
    main()