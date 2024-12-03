import pygame
from pruebaMenus import Menus
from menuPersonajesPruebas import SeleccionPersonaje
from nivel import Nivel1
from Acciones.propiedadesPersonajes import Propiedades

from PersonajeStarenka.claseEscenarioStar import PersonajeStarenka
from PersonajeLuis2.claseMainLuis import PersonajeLuis
from PersonajeEmma.claseEmma import PersonajeEmmanuel
from PersonajeLin.blue_multiverso.machote.main import PersonajeLin

instanciaLuis = PersonajeLuis()

class Main:
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock() 

        self.estado_general = "nivel1" #menus, personajes, nivel1, nivel2, nivel3, salir
        self.personajesJugables=[]


    def run(self):
        """Bucle PRINCIPAL"""
        if self.estado_general == "menus":
            ventana_actual = Menus()
        if self.estado_general == "nivel1" or self.estado_general == "nivel2" or self.estado_general == "nivel3":
            self.personajesJugables=[]
            ventana_actual = SeleccionPersonaje()
        ventana_actual.run()

        
        if self.estado_general == "nivel1" or self.estado_general == "nivel2" or self.estado_general == "nivel3": 
            z = 0
            for i in range(2):
                if (i == 1):
                    z = 4
                    
                    
                if ventana_actual.guardado[i] == 0:
                    self.personajesJugables.append(z + ventana_actual.guardado[i])
                    self.personajeCorrer = PersonajeEmmanuel()
                elif ventana_actual.guardado[i] == 1:
                    self.personajesJugables.append(z + ventana_actual.guardado[i])
                    self.personajeCorrer = instanciaLuis
                elif ventana_actual.guardado[i] == 2:
                    self.personajesJugables.append(z + ventana_actual.guardado[i])
                    self.personajeCorrer=PersonajeLin()
                elif ventana_actual.guardado[i] == 3:
                    self.personajeCorrer=PersonajeStarenka()
                    self.personajesJugables.append(z + ventana_actual.guardado[i])
                
                self.personajeCorrer.run()
            
            eleccion = Propiedades(self.personajesJugables)


        print(self.estado_general)
        self.clock.tick(60)

        if self.estado_general == "salir":
            self.running = False



if __name__ == "__main__":
    game = Main()
    game.run() 
        