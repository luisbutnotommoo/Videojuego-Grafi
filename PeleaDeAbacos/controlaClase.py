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
from PersonajeEmma.claseEmma import PersonajeEmmanuel
#from PersonajeLin.machote.main_sincolision import MainLin
from Acciones.propiedadesPersonajes import Propiedades
from nivel2 import Nivel2
from nivel import Nivel1
from nivel3 import Nivel3
from menuPrincipal import MenuPrincipal
from menuNivel import MenuNivel
import Sonidos.controla_mp3 as cmp3
import subprocess

directorio_script = os.path.dirname(os.path.abspath(__file__))

class controlaClase:
    def __init__(self):
        self.mp3=cmp3.MP3()
        self.personajesJugables = []
        self.banderaSeleccion=True
        self.banderaNivel=True
        pygame.init()  
        self.mp3.reproducir_sonido_fondo("menu_principal.mp3")

        
    def main(self):
        while True:
            print("Esta aqui")
            self.banderaSeleccion=True
            self.banderaNivel=True
            
            menuPrincipal=MenuPrincipal()
            menuPrincipal.main()

            
            while(self.banderaNivel):
                print("Si regreso aqui, solo que no quiso")
                self.banderaSeleccion=True
                menuNivel=MenuNivel()
                menuNivel.main()

                if(menuNivel.nivel==4):
                    self.banderaSeleccion=False
                    self.banderaNivel=False
                    menuPrincipal.reset()
                    
                

                if(menuNivel.jugar==False):
                    while(self.banderaSeleccion):
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
                                    personajeCorrer = PersonajeEmmanuel()
                                elif menu.guardado[i] == 1:
                                    self.personajesJugables.append(z + menu.guardado[i])
                                elif menu.guardado[i] == 2:
                                    self.personajesJugables.append(z + menu.guardado[i])
                                elif menu.guardado[i] == 3:
                                    personajeCorrer=PersonajeStarenka()
                                    self.personajesJugables.append(z + menu.guardado[i])

                                personajeCorrer.run()
                            
                            eleccion = Propiedades(self.personajesJugables)

                        
                            
                            if(menuNivel.nivel==1):
                                nivel1 = Nivel1(personajesJugables=eleccion.personajesJugables)
                                nivel1.run()
                                if nivel1.banderaSiguienteNivel==False:
                                    menuNivel.nivel=2

                                if nivel1.banderaMenuNivel==False:
                                    self.banderaSeleccion=False
                                    menuNivel.reset()
                                if nivel1.banderaMenuPrincipal==False:
                                    self.banderaSeleccion=False
                                    self.banderaNivel=False
                                    menuNivel.reset()
                                    menuPrincipal.reset()
                                    
                                

                            if(menuNivel.nivel==2):
                                nivel2 = Nivel2(personajesJugables=eleccion.personajesJugables)
                                nivel2.run()
                                if nivel2.banderaSiguienteNivel==False:
                                    menuNivel.nivel=3

                                if nivel2.banderaMenuNivel==False:
                                    self.banderaSeleccion=False
                                    menuNivel.reset()
                                if nivel2.banderaMenuPrincipal==False:
                                    self.banderaSeleccion=False
                                    self.banderaNivel=False
                                    menuNivel.reset()
                                    menuPrincipal.reset()

                            if(menuNivel.nivel==3):
                                nivel3 = Nivel3(personajesJugables=eleccion.personajesJugables)
                                nivel3.run()
                                if nivel2.banderaSiguienteNivel==False:
                                    menuNivel.nivel=3

                                if nivel2.banderaMenuNivel==False:
                                    self.banderaSeleccion=False
                                    menuNivel.reset()
                                if nivel2.banderaMenuPrincipal==False:
                                    self.banderaSeleccion=False
                                    self.banderaNivel=False
                                    menuNivel.reset()
                                    menuPrincipal.reset()
                            



                    
                    # Ejecutar el nivel

if __name__ == "__main__":
    controlaClase().main()