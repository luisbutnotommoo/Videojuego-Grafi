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
from PersonajeLuis2.claseMainLuis import PersonajeLuis
from PersonajeEmma.claseEmma import PersonajeEmmanuel
from PersonajeLin.blue_multiverso.machote.main import PersonajeLin

from Acciones.propiedadesPersonajes import Propiedades
from nivel2 import Nivel2
from nivel import Nivel1
from nivel3 import Nivel3
from menuPrincipal import MenuPrincipal
from menuNivel import MenuNivel
import Sonidos.controla_mp3 as cmp3
import subprocess

instanciaLuis = PersonajeLuis()
directorio_script = os.path.dirname(os.path.abspath(__file__))

class GameState:
    def __init__(self):
        self.mp3 = cmp3.MP3()
        self.personajesJugables = []
        self.banderaSeleccion = True
        self.banderaNivel = True
        self.personajeCorrer = None
        pygame.init()  
        
       

    def enter(self):
        pass

    def exit(self):
        pass

    def update(self):
        pass

    def render(self):
        pass

class MainMenuState(GameState):
    def enter(self):
        print("Entrando al menu principal")
        self.menuPrincipal = MenuPrincipal()
        self.menuPrincipal.main()

    def update(self):
        if self.menuPrincipal.exit_game:
            pygame.quit()
            sys.exit()

        if self.menuPrincipal.play_game:
            game.change_state(MenuNiveles())

        

    def render(self):
        pass

class MenuNiveles(GameState):
    def enter(self):
        self.menuNivel=MenuNivel()
        self.menuNivel.main()
    
    def update(self):
        if self.menuNivel.jugar==False:
            game.change_state(SelectCharacterState(self.menuNivel.nivel))
        

class SelectCharacterState(GameState):
    def __init__(self,  nivel):
        super().__init__()
        self.nivel = nivel

    def enter(self):
        print("Entrando a la selección de personajes")
        self.personajesJugables = []
        self.menu = SeleccionPersonaje()
        self.menu.run()

    def update(self):
        if self.menu.bandera == 1:  
            game.change_state(MainMenuState())

        z = 0
        for i in range(2):
            if i == 1:
                z = 4

            if self.menu.guardado[i] == 0:
                self.personajesJugables.append(z + self.menu.guardado[i])
               # self.personajeCorrer = PersonajeEmmanuel()
            elif self.menu.guardado[i] == 1:
                self.personajesJugables.append(z + self.menu.guardado[i])
               # self.personajeCorrer = instanciaLuis
            elif self.menu.guardado[i] == 2:
                self.personajesJugables.append(z + self.menu.guardado[i])
                #self.personajeCorrer = PersonajeLin()
            elif self.menu.guardado[i] == 3:
                #self.personajeCorrer = PersonajeStarenka()
                self.personajesJugables.append(z + self.menu.guardado[i])

            #self.personajeCorrer.run()

        eleccion = Propiedades(self.personajesJugables)
        game.change_state(LevelState(eleccion.personajesJugables, self.nivel))

    

class LevelState(GameState):
    def __init__(self, personajesJugables, nivel):
        super().__init__()
        self.personajesJugables = personajesJugables
        self.nivel = nivel

    def enter(self):
        print(f"Entrando al nivel {self.nivel}")
        if self.nivel == 1:
            self.nivel1 = Nivel1(personajesJugables=self.personajesJugables)
            self.nivel1.run()

        elif self.nivel == 2:
            self.nivel2 = Nivel2(personajesJugables=self.personajesJugables)
            self.nivel2.run()

        elif self.nivel == 3:
            self.nivel3 = Nivel3(personajesJugables=self.personajesJugables)
            self.nivel3.run()

    def update(self):
        if self.nivel == 1:
            if self.nivel1.banderaSiguienteNivel == False:
                self.nivel = 2

            if self.nivel1.banderaMenuNivel == False:
                game.change_state(MainMenuState())

        elif self.nivel == 2:
            if self.nivel2.banderaSiguienteNivel == False:
                self.nivel = 3

            if self.nivel2.banderaMenuNivel == False:
                game.change_state(MainMenuState())

        elif self.nivel == 3:
            if self.nivel3.banderaSiguienteNivel == False:
                self.nivel = 3

            if self.nivel3.banderaMenuNivel == False:
                game.change_state(MainMenuState())

    def render(self):
        pass

class Game:
    def __init__(self):
        self.state = None
        self.change_state(MainMenuState())

    def change_state(self, state):
        if self.state:
            self.state.exit()
        self.state = state
        self.state.enter()

    def update(self):
        self.state.update()

    def render(self):
        self.state.render()

if __name__ == "__main__":
    game = Game()
    while True:
        game.update()
        game.render()
