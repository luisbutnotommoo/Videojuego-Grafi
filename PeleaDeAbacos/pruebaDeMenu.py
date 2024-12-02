import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
import sys
import os
from Acciones.boceto import PersonajesDeTodos
from menuPersonajesPruebas import SeleccionPersonaje
from PersonajeStarenka.claseEscenarioStar import PersonajeStarenka
from PersonajeEmma.claseEmma import PersonajeEmmanuel
from Acciones.propiedadesPersonajes import Propiedades
from nivel2 import Nivel2
from nivel import Nivel1
from menuPrincipal import MenuPrincipal
from menuNivel import MenuNivel

class ControlaClase:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("Sonidos/menu_principal.mp3")
        pygame.mixer.music.play(loops=-1)
        self.personajesJugables = []
    
    def main(self):
        while True:
            self.menu_principal()
    
    def menu_principal(self):
        """Muestra el menú principal."""
        menuPrincipal = MenuPrincipal()
        menuPrincipal.main()
        
        # Lógica para pasar al siguiente menú
        if menuPrincipal.ir_a_niveles:
            self.menu_niveles()
    
    def menu_niveles(self):
        """Muestra el menú de niveles."""
        menuNivel = MenuNivel()
        menuNivel.main()
        
        if menuNivel.jugar:
            self.seleccion_personaje(menuNivel.nivel)
        elif menuNivel.volver_menu_principal:
            self.menu_principal()
    
    def seleccion_personaje(self, nivel_actual):
        """Muestra la selección de personajes."""
        menu = SeleccionPersonaje()
        menu.run()
        
        if menu.bandera == 1:  # Si seleccionó los personajes
            self.personajesJugables = self._procesar_seleccion(menu.guardado)
            if nivel_actual == 1:
                self.ejecutar_nivel_1()
            elif nivel_actual == 2:
                self.ejecutar_nivel_2()
    
    def ejecutar_nivel_1(self):
        """Ejecuta el Nivel 1."""
        nivel1 = Nivel1(personajesJugables=self.personajesJugables)
        nivel1.run()
        
        if nivel1.banderaSiguienteNivel:
            self.ejecutar_nivel_2()
        elif nivel1.banderaMenuPrincipal:
            self.menu_principal()
    
    def ejecutar_nivel_2(self):
        """Ejecuta el Nivel 2."""
        nivel2 = Nivel2(personajesJugables=self.personajesJugables)
        nivel2.run()
        
        if nivel2.banderaMenuPrincipal:
            self.menu_principal()
    
    def _procesar_seleccion(self, seleccion):
        """Procesa la selección de personajes."""
        personajes = []
        z = 0
        for i in range(len(seleccion)):
            if i == 1:
                z = 4
            personajes.append(z + seleccion[i])
        return personajes

if __name__ == "__main__":
    ControlaClase().main()
