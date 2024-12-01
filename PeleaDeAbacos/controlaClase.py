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
from nivel2_Prueba import Nivel2Prueba
import subprocess
directorio_script = os.path.dirname(os.path.abspath(__file__))

class controlaClase:
    def __init__(self):
        self.personajesJugables=[]

    def main(self):

      
            menu = SeleccionPersonaje()
            menu.run()
            
            

            z=0
            for i in range(2):
                    if (i==1):
                         z=4
                    if menu.guardado[i] == 0:
                        self.personajesJugables.append(z+ menu.guardado[i])

                        #personajeCorrer = PersonajeEmma()
                    elif menu.guardado[i] == 1:
                        self.personajesJugables.append(z+ menu.guardado[i])
                        #personajeCorrer = PersonajeLuis()
                    elif menu.guardado[i] == 2:
                       self.personajesJugables.append(z+ menu.guardado[i])
                        #personajeCorrer = MainLin()
                    elif menu.guardado[i] == 3:
                        self.personajesJugables.append(z+ menu.guardado[i])
                        #personajeCorrer = PersonajeStarenka()
                    
            
                    #personajeCorrer.run()  # Ejecutamos el personaje"""

           
            eleccion=Propiedades(self.personajesJugables)
            nivel2=Nivel2Prueba(personajesJugables=eleccion.personajesJugables)
            nivel2.run()




if __name__ == "__main__":
    controlaClase().main()