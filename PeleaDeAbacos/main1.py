from pruebaMenus import Menus
from menuPersonajesPruebas import SeleccionPersonaje
from nivel import Nivel1
import pygame

class Main:
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock() 
        self.estado_general = "menus" #menus, personajes, nivel1, nivel2, nivel3, salir


    def run(self):
        """Bucle PRINCIPAL"""
        if self.estado_general == "menus":
            ventana_actual = Menus()
        if self.estado_general == "nivel1":
            ventana_actual = Nivel1()
        self.estado_general = ventana_actual.run()
        print(self.estado_general)
        self.clock.tick(60)
        

        if self.estado_general == "salir":
            self.running = False



if __name__ == "__main__":
    game = Main()
    game.run() 
        