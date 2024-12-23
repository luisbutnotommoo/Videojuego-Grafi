import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
from Acciones import boceto2 as b
from Acciones.boceto2 import PersonajesDeTodos
import os
from Acciones.textos import textos as tx
from Imagenes.controla_img import ruta_carpeta_imagenes as ruta_img
from Sonidos.controla_mp3 import ruta_carpeta_audios as ruta_audio
from PersonajeStarenka.claseEscenarioStar import PersonajeStarenka
from PersonajeLuis2.claseMainLuis import PersonajeLuis
from PersonajeEmma.claseEmma import PersonajeEmmanuel
from PersonajeLin.blue_multiverso.machote.main import PersonajeLin

instanciaLuis = PersonajeLuis()

class SeleccionPersonaje:
    def __init__(self, display_size=(800, 600)):
        self.bandera=0
        self.display = display_size
        self.init_pygame()
        self.init_opengl()
        self.guardado=[]
        self.nom1=" "
        self.nom2=" "
        self.menuBan=False
        self.banderaAcomula=False
        self.running=True
        # Estados de selección de personajes
        self.selected_character = -1
        self.personaje = [
            PersonajesDeTodos("Dr. Newt", b.figuraEmma(0),rotacion=190, escala=(0.22, 0.22, 0.22)),
            PersonajesDeTodos("Heinsenpurr", b.figuraLuis(0), escala=(1.4, 1.4, 1.4)),
            PersonajesDeTodos("Blue",b.figuraLin(0), rotacion=0, escala=(0.4, 0.4, 0.4)),
            PersonajesDeTodos("Amargando",  b.figuraStar(0),rotacion=190, escala=(0.25, 0.25, 0.25))
        ]
        self.bandera_control_instrucciones = True
        self.bandera_instrucciones = True
        self.fuente_instrucciones = pygame.font.SysFont(None, 30)
        self.texto_instrucciones = [
            "                                   M E N U   P E R S O N A J E S      ",
            "               _____________________________________________", "",
            "                     Para visualizar más de cerca un personaje ",
            "                       Presiona un número(1, 2, 3, 4) y después M ",
            "                     Para salir del modo visualizar, presiona ESC",
            "              Cuando quieras elegir un personaje, presiona ENTER",
            "                Recuerda, se haran DOS elecciones de personajes",
            "                                     Jugador 1 y Jugador 2",
            "               _____________________________________________", "",
            "                                - Presiona P para continuar -"
        ]

        self.contador=0
        
        # Posiciones
        self.asignar_posiciones_personajes()

        # Cargar texturas
        floor=os.path.join(ruta_img,'pisoCast.jpg')
        wall=os.path.join(ruta_img,'castillo4.jpg')
        self.floor_texture = self.load_texture(floor)
        self.wall_texture = self.load_texture(wall)

        self.jump_height = 0.0  # Altura del salto
        self.jump_speed = 0.1    # Velocidad del salto
        self.jumping = False      # Estado de salto
        
        self.font_titulo = pygame.font.SysFont('Algerian', 60)
        self.font_menu = pygame.font.SysFont('Imprint MT Shadow', 65)
        self.font_personajes = pygame.font.SysFont('Imprint MT Shadow', 35)
        self.font_personajes2 = pygame.font.SysFont('Imprint MT Shadow', 30)
        self.font_instrucciones = pygame.font.SysFont('Imprint MT Shadow', 25)
        
        self.sonido_seleccion = pygame.mixer.Sound(os.path.join(ruta_audio,"seleccion_personaje_espada.mp3"))
        pygame.mixer.music.load(os.path.join(ruta_audio,"menu_medieval.mp3"))
        pygame.mixer.music.play(loops=-1) 

    def resetMenu(self):
        pygame.init()
        self.init_pygame()
        self.init_opengl()
        floor=os.path.join(ruta_img,'pisoCast.jpg')
        wall=os.path.join(ruta_img,'castillo4.jpg')
        self.floor_texture = self.load_texture(floor)
        self.wall_texture = self.load_texture(wall)
        self.sonido_seleccion = pygame.mixer.Sound(os.path.join(ruta_audio,"seleccion_personaje_espada.mp3"))
        pygame.mixer.music.load(os.path.join(ruta_audio,"menu_medieval.mp3"))
        pygame.mixer.music.play(loops=-1) 
    def asignar_posiciones_personajes(self):
        posiciones = [
            (-4.5, -1.5, 0),  # Posición para personaje 1
            (-1.5, -1.5, 0),  # Posición para personaje 2
            (5.6, -1.5, -1),   # Posición para personaje 3
            (4.5, -1.5, 0)    # Posición para personaje 4
        ]
        for personaje, (x, y, z) in zip(self.personaje, posiciones):
            personaje.set_position(x, y, z)

    def init_pygame(self):
        #pygame.init()
        #pygame.mixer.init()
        self.screen = pygame.display.set_mode(self.display, DOUBLEBUF | OPENGL)
        pygame.event.set_grab(True)

    def init_opengl(self):


        # Fondo oscuro
        glClearColor(0.1, 0.1, 0.1, 1.0)
        self.set_perspective()


    def set_perspective(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(60, (self.display[0] / self.display[1]), 0.5, 100.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -20.0)

    def configurar_luz_personaje(self, is_selected):
        if is_selected:
            # Luz neutral para el personaje seleccionado
            glEnable(GL_LIGHT2)
            glLightfv(GL_LIGHT2, GL_POSITION, [0.0, 5.0, 0.0, 1.0])
            glLightfv(GL_LIGHT2, GL_AMBIENT, [0.2, 0.2, 0.2, 1.0])  # Luz ambiente baja y neutral
            glLightfv(GL_LIGHT2, GL_DIFFUSE, [0.5, 0.5, 0.5, 1.0])  # Luz difusa neutral
            glLightfv(GL_LIGHT2, GL_SPECULAR, [0.3, 0.3, 0.3, 1.0])
            
            # Ajustar material para resaltar sin tonos amarillos
            glMaterialfv(GL_FRONT, GL_SPECULAR, [0.6, 0.6, 0.6, 1.0])
            glMaterialf(GL_FRONT, GL_SHININESS, 32.0)
        else:
            glDisable(GL_LIGHT2)
            glMaterialfv(GL_FRONT, GL_SPECULAR, [0.2, 0.2, 0.2, 1.0])
            glMaterialf(GL_FRONT, GL_SHININESS, 20.0)


    def dibujar_personaje(self, personaje, is_selected):
        glPushMatrix()
        x, y, z = personaje.posicion
        glTranslatef(x, y, z)

        # Configurar iluminación específica para el personaje
        self.configurar_luz_personaje(is_selected)
        
        if is_selected:
            # Actualizar posición de la luz del personaje seleccionado
            glLightfv(GL_LIGHT2, GL_POSITION, [x, 5.0, z, 1.0])
            
            # Aumentar brillo manteniendo el color
            glColor3f(1.0, 1.0, 1.0)
        else:
            # Color normal para personajes no seleccionados
            glColor3f(0.9, 0.9, 0.9)
            
        personaje.render()
        glPopMatrix()

    def dibuja_textos(self):
        glColor4f(2, 2, 2, 1)
        self.render_text_2d(self.display,"Duelo de Abacos",135,590,self.font_titulo)
        self.render_text_2d(self.display,"Menú de selección",195,520,self.font_menu)
        self.render_text_2d(self.display,"Dr. Newt",70,200,self.font_personajes)
        self.render_text_2d(self.display,"Heisenpurr",250,200,self.font_personajes)
        self.render_text_2d(self.display,"Blue",460,198,self.font_personajes)
        self.render_text_2d(self.display,"Amargando",580,200,self.font_personajes)
        self.render_text_2d(self.display,"Teclas |1||2||3||4| - Selección de personaje\n|Enter| - Confirma selección\n|M| - Visualizar personaje",10,70,self.font_instrucciones)
        self.render_text_2d(self.display,"Teclas de modo visualizar personaje:\n|ESC| - Salir De Visualizar",460,70,self.font_instrucciones)
        if(self.selected_character!=-1) and self.contador==0:
            self.render_text_2d(self.display, f"Personaje jugador 1:{self.personaje[self.selected_character].nombre}", 60, 460, self.font_personajes2)
            self.nom1=self.personaje[self.selected_character].nombre
            self.render_text_2d(self.display, "Personaje jugador 2:", 450, 460, self.font_personajes2)
        elif(self.selected_character!=-1) and self.contador==1:
            self.render_text_2d(self.display, f"Personaje jugador 1:{self.nom1}", 60, 460, self.font_personajes2)
            self.render_text_2d(self.display, f"Personaje jugador 2:{self.personaje[self.selected_character].nombre}", 450, 460, self.font_personajes2)
            self.nom2=self.personaje[self.selected_character].nombre
        elif(self.selected_character!=-1) and self.contador==2:
            self.render_text_2d(self.display, f"Personaje jugador 1:{self.nom1}", 60, 460, self.font_personajes2)
            self.render_text_2d(self.display, f"Personaje jugador 2:{self.nom2}", 450, 460, self.font_personajes2)
        elif self.selected_character==-1:
            self.render_text_2d(self.display,"Personaje jugador 1: "+self.nom1,60 ,460,self.font_personajes2)
            self.render_text_2d(self.display, "Personaje jugador 2:", 450, 460, self.font_personajes2)

    def dibujar_piso_pared(self):
       
        glEnable(GL_TEXTURE_2D)
        
        # Configurar material para las texturas con un filtro neutral
        glMaterialfv(GL_FRONT, GL_SPECULAR, [0.2, 0.2, 0.2, 1.0])
        glMaterialf(GL_FRONT, GL_SHININESS, 16.0)

        # Suelo
        glBindTexture(GL_TEXTURE_2D, self.floor_texture)
        glColor3f(0.6, 0.6, 0.6)  # Filtro gris
        glBegin(GL_QUADS)
        glNormal3f(0.0, 1.0, 0.0)
        glTexCoord2f(0, 0); glVertex3f(-20.0, -2.0, -20.0)
        glTexCoord2f(1, 0); glVertex3f(20.0, -2.0, -20.0)
        glTexCoord2f(1, 1); glVertex3f(20.0, -2.0, 20.0)
        glTexCoord2f(0, 1); glVertex3f(-20.0, -2.0, 20.0)
        glEnd()

        # Techo
        glBindTexture(GL_TEXTURE_2D, self.wall_texture)
        glColor3f(0.6, 0.6, 0.6)
        glBegin(GL_QUADS)
        glNormal3f(0.0, -1.0, 0.0)
        glTexCoord2f(0, 0); glVertex3f(-20.0, 25.0, -20.0)
        glTexCoord2f(1, 0); glVertex3f(20.0, 25.0, -20.0)
        glTexCoord2f(1, 1); glVertex3f(20.0, 25.0, 20.0)
        glTexCoord2f(0, 1); glVertex3f(-20.0, 25.0, 20.0)
        glEnd()

        # Pared trasera
        glBindTexture(GL_TEXTURE_2D, self.wall_texture)
        glColor3f(0.6, 0.6, 0.6)
        glBegin(GL_QUADS)
        glNormal3f(0.0, 0.0, 1.0)
        glTexCoord2f(0, 0); glVertex3f(-20.0, -2.0, -20.0)
        glTexCoord2f(1, 0); glVertex3f(20.0, -2.0, -20.0)
        glTexCoord2f(1, 1); glVertex3f(20.0, 25.0, -20.0)
        glTexCoord2f(0, 1); glVertex3f(-20.0, 25.0, -20.0)
        glEnd()

        # Pared delantera
        glBindTexture(GL_TEXTURE_2D, self.wall_texture)
        glColor3f(0.6, 0.6, 0.6)
        glBegin(GL_QUADS)
        glNormal3f(0.0, 0.0, -1.0)
        glTexCoord2f(0, 0); glVertex3f(-20.0, -2.0, 20.0)
        glTexCoord2f(1, 0); glVertex3f(20.0, -2.0, 20.0)
        glTexCoord2f(1, 1); glVertex3f(20.0, 25.0, 20.0)
        glTexCoord2f(0, 1); glVertex3f(-20.0, 25.0, 20.0)
        glEnd()

        # Pared izquierda
        glBindTexture(GL_TEXTURE_2D, self.wall_texture)
        glColor3f(0.6, 0.6, 0.6)
        glBegin(GL_QUADS)
        glNormal3f(1.0, 0.0, 0.0)
        glTexCoord2f(0, 0); glVertex3f(-20.0, -2.0, -20.0)
        glTexCoord2f(1, 0); glVertex3f(-20.0, -2.0, 20.0)
        glTexCoord2f(1, 1); glVertex3f(-20.0, 25.0, 20.0)
        glTexCoord2f(0, 1); glVertex3f(-20.0, 25.0, -20.0)
        glEnd()

        # Pared derecha
        glBindTexture(GL_TEXTURE_2D, self.wall_texture)
        glColor3f(0.6, 0.6, 0.6)
        glBegin(GL_QUADS)
        glNormal3f(-1.0, 0.0, 0.0)
        glTexCoord2f(0, 0); glVertex3f(20.0, -2.0, -20.0)
        glTexCoord2f(1, 0); glVertex3f(20.0, -2.0, 20.0)
        glTexCoord2f(1, 1); glVertex3f(20.0, 25.0, 20.0)
        glTexCoord2f(0, 1); glVertex3f(20.0, 25.0, -20.0)
        glEnd()

        glDisable(GL_TEXTURE_2D)


    def render_text_2d(self, display, text, x, y, font, line_height=18):
        # Caché para texturas
        if not hasattr(self, '_text_texture_cache'):
            self._text_texture_cache = {}

        # Verificar si el texto ya tiene textura generada
        if text not in self._text_texture_cache:
            lines = text.split('\n')  # Dividir texto en líneas
            textures = []

            for line in lines:
                text_surface = font.render(line, True, (255, 255, 255))  # Fondo transparente
                text_data = pygame.image.tostring(text_surface, "RGBA", True)
                text_width, text_height = text_surface.get_size()

                texture_id = glGenTextures(1)
                glBindTexture(GL_TEXTURE_2D, texture_id)
                glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, text_width, text_height, 0, GL_RGBA, GL_UNSIGNED_BYTE, text_data)
                glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
                glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

                textures.append((texture_id, text_width, text_height))

            # Guardar en la caché
            self._text_texture_cache[text] = textures

        # Recuperar texturas de la caché
        textures = self._text_texture_cache[text]

        # Configuración de OpenGL
        glEnable(GL_TEXTURE_2D)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        # Configuración de proyección
        glMatrixMode(GL_PROJECTION)
        glPushMatrix()
        glLoadIdentity()
        glOrtho(0, display[0], 0, display[1], -1, 1)

        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glLoadIdentity()

        # Dibujar las texturas
        for i, (texture_id, text_width, text_height) in enumerate(textures):
            glBindTexture(GL_TEXTURE_2D, texture_id)
            glBegin(GL_QUADS)
            # Asegúrate de que las coordenadas de la textura estén correctamente alineadas
            glTexCoord2f(0, 1); glVertex2f(x, y - i * line_height)  # Esquina inferior izquierda
            glTexCoord2f(1, 1); glVertex2f(x + text_width, y - i * line_height)  # Esquina inferior derecha
            glTexCoord2f(1, 0); glVertex2f(x + text_width, y - i * line_height - text_height)  # Esquina superior derecha
            glTexCoord2f(0, 0); glVertex2f(x, y - i * line_height - text_height)  # Esquina superior izquierda
            glEnd()

        # Restaurar matrices
        glPopMatrix()
        glMatrixMode(GL_PROJECTION)
        glPopMatrix()
        glMatrixMode(GL_MODELVIEW)

        # Deshabilitar modos
        glDisable(GL_BLEND)
        glDisable(GL_TEXTURE_2D)

        # Limpieza opcional de texturas si cambian dinámicamente
        # for texture_id, _, _ in textures:
        #     glDeleteTextures(1, [texture_id])




    def draw_scene(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # Dibujar escenario
        self.dibujar_piso_pared()
        self.update_jump()
        # Dibujar personajes
        for idx, character in enumerate(self.personaje):
            is_selected = idx == self.selected_character
            if is_selected:
                character.set_position(character.posicion[0], -1.0+self.jump_height, character.posicion[2])
            else:
                character.set_position(character.posicion[0], -1.5, character.posicion[2])
            self.dibujar_personaje(character, is_selected)

        self.dibuja_textos()
        if self.bandera_control_instrucciones:
            tx.draw_text2(self.texto_instrucciones,self.fuente_instrucciones,200,50,50)
        pygame.display.flip()

    def handle_input(self):
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.KEYDOWN:
                    """if event.key == pygame.K_ESCAPE:
                        self.bandera=1
                        return False"""
                    if event.key == pygame.K_p:
                        if self.bandera_control_instrucciones:
                            self.bandera_instrucciones =  not self.bandera_instrucciones
                            self.bandera_control_instrucciones = not self.bandera_control_instrucciones       
                    elif event.key in (pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4):
                        self.selected_character = event.key - pygame.K_1
                        self.sonido_seleccion.play()
                    elif event.key==pygame.K_m and self.selected_character!=-1:
                        self.menuBan=True
                        self.running=False
                    elif event.key == pygame.K_RETURN:
                        if self.selected_character >= 0:
                            if(self.contador<2):
                                print(f"Personaje seleccionado: {self.selected_character + 1}")
                                self.personaje[self.selected_character].start_jump()  # Iniciar el salto
                                self.saltar()
                                self.contador=self.contador+1
                                self.guardado.append(self.selected_character)
                        else:
                            print("No se ha seleccionado ningún personaje.")
            return True
        except pygame.error as e:
         print(f"Error al manejar eventos: {e}")



    def saltar(self):
        # Iniciar el salto
        self.jumping = True

    def update_jump(self):
        if self.jumping:
            # Actualizar la altura del salto
            if self.jump_height < 2.0:  # Altura máxima del salto
                self.jump_height += self.jump_speed
            else:
                self.jumping = False  # Terminar el salto al alcanzar la altura máxima
        else:
            # Bajar el personaje
            if self.jump_height > 0:
                self.jump_height -= self.jump_speed

    def run(self):

        while self.running:
            self.handle_input()
            self.draw_scene()
            pygame.time.wait(10)
            if (self.contador==2):
                self.cleanup()
                self.running=False

        pygame.display.quit()
                
     

    def cleanup(self):
        try:
        # Limpiar texturas
            if hasattr(self, 'floor_texture'):
                glDeleteTextures([self.floor_texture, self.wall_texture])
            
                # Deshabilitar luces
                glDisable(GL_LIGHT0)
                glDisable(GL_LIGHT1)
                glDisable(GL_LIGHT2)
                
                # Limpiar contexto de OpenGL
                glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
               
                pygame.mixer.music.stop()
                pygame.mixer.music.unload()
                #pygame.mixer.quit()
                # Reiniciar estado de Pygame
                pygame.display.quit()
                #pygame.display.init()
        except Exception as e:
            print(f"Error en cleanup: {e}")
    
 
    def load_texture(self, path):
        texture_surface = pygame.image.load(path)
        texture_data = pygame.image.tostring(texture_surface, "RGB", 1)
        width, height = texture_surface.get_rect().size

        texture_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, texture_id)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, texture_data)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        return texture_id

if __name__ == "__main__":
    sP=SeleccionPersonaje()
    sP.run()