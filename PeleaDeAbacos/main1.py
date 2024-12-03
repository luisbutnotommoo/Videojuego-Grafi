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
        pygame.init()
        pygame.mixer.init()
        self.running = True
        self.clock = pygame.time.Clock() 

        self.estado_general = "menuPrincipal" #menuPrincipal, menuNiveles, personajes1, personajes2, personajes3 (seleccion de personajes que guarda el nivel),
                                        #nivel1, nivel2, nivel3, salir
        self.personajesJugables=[]
        self.index = 0


    def run(self):
        """Bucle PRINCIPAL"""
        while self.running:
            print(f"Iteracion {self.index} del bucle principal")
            if self.estado_general == "menuPrincipal":
                print("Entro a menus")
                ventana_actual = Menus()
            if self.estado_general == "personaje1" or self.estado_general == "personaje2" or self.estado_general == "personaje3":
                print ("Entro a seleccion de personaje")
                self.personajesJugables=[]
                ventana_actual = SeleccionPersonaje()
                ventana_actual.run()

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

                for i in range(1,4):
                    if self.estado_general == f"personaje{i}":
                        self.estado_general = f"nivel{i}"
            else: 
                self.estado_general = ventana_actual.run()
                print(f"Terminó de ejecutar {self.estado_general}")

            if self.estado_general == "nivel1":
                print("Entro a nivel 1")
                ventana_actual = Nivel1(personajesJugables = eleccion.personajesJugables)

            self.clock.tick(60)

            if self.estado_general == "salir":
                print("Entro a salir")
                self.running = False
                
            self.index += 1
        print("Salio del programa")

if __name__ == "__main__":
    game = Main()
    game.run() 
        