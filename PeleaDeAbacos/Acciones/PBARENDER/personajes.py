import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image 
import mapasUV

class Personajes:
    def __init__(self):
        self.personajes = {}
        self.texturas = {}  # Diccionario para almacenar texturas
               
    def cargar_textura(self, ruta_textura):
        """
        Carga una textura y retorna su ID
        """
        if ruta_textura in self.texturas:
            return self.texturas[ruta_textura]
            
        # Cargar imagen con PIL
        imagen = Image.open(ruta_textura)
        datos_imagen = imagen.convert("RGBA").tobytes()
        
        # Generar textura en OpenGL
        id_textura = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, id_textura)
        
        # Configurar parámetros de la textura
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        
        # Cargar datos de la imagen
        glTexImage2D(
            GL_TEXTURE_2D, 0, GL_RGBA, imagen.width, imagen.height, 0,
            GL_RGBA, GL_UNSIGNED_BYTE, datos_imagen
        )
        glGenerateMipmap(GL_TEXTURE_2D)
        
        self.texturas[ruta_textura] = id_textura
        return id_textura


    def agregar_personaje(self, nombre_personaje, extremidades):
        self.personajes[nombre_personaje] = {}
        
        for nombre_extremidad, geometria in extremidades.items():
            
            if "Esfera" in nombre_extremidad:
                centro = geometria['centro']
                radio = geometria['radio']
                color = geometria.get('colors', [1.0, 1.0, 1.0, 1.0])
                colores = np.array([color], dtype=np.float32)
                
                # Agregar soporte para textura en esferas
                textura = None
                if 'textura' in geometria:
                    textura = self.cargar_textura(geometria['textura'])
                
                self.personajes[nombre_personaje][nombre_extremidad] = {            
                    'centro': centro,
                    'radio': radio,
                    'colores': colores,
                    'coords_textura': mapasUV.uv_esfera,
                    'id_textura': textura
                }
                
            else:
                vertices = np.array(geometria['vertices'], dtype=np.float32)
                faces = np.array(geometria.get('faces', []), dtype=np.uint32)
                primitive = geometria.get('primitive', GL_TRIANGLES)
                
                # Crear array de colores para cada vértice
                color = geometria.get('colors', [1.0, 1.0, 1.0, 1.0])
                colores = np.tile(color, (len(vertices), 1)).astype(np.float32)
                
                coords_textura = np.array(geometria.get('texcoords', []), dtype=np.float32)
                textura_path = geometria.get('texture_path', None)
                
                # Crear VAO y VBOs
                vao = glGenVertexArrays(1)
                vbo_vertices = glGenBuffers(1)
                vbo_colores = glGenBuffers(1)
                vbo_texcoords = glGenBuffers(1) if len(coords_textura) > 0 else None
                
                glBindVertexArray(vao)
                
                # Buffer de vértices
                glBindBuffer(GL_ARRAY_BUFFER, vbo_vertices)
                glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)
                glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)
                glEnableVertexAttribArray(0)
                
                # Buffer de colores
                glBindBuffer(GL_ARRAY_BUFFER, vbo_colores)
                glBufferData(GL_ARRAY_BUFFER, colores.nbytes, colores, GL_STATIC_DRAW)
                glVertexAttribPointer(1, 4, GL_FLOAT, GL_FALSE, 0, None)
                glEnableVertexAttribArray(1)
                
                if vbo_texcoords:
                    glBindBuffer(GL_ARRAY_BUFFER, vbo_texcoords)
                    glBufferData(GL_ARRAY_BUFFER, coords_textura.nbytes, coords_textura, GL_STATIC_DRAW)
                    glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, 0, None)
                    glEnableVertexAttribArray(2)
                
                # EBO si hay faces
                if len(faces) > 0:
                    ebo = glGenBuffers(1)
                    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ebo)
                    glBufferData(GL_ELEMENT_ARRAY_BUFFER, faces.nbytes, faces, GL_STATIC_DRAW)
                else:
                    ebo = None
                
                # Cargar textura si existe
                id_textura = None
                if textura_path:
                    id_textura = self.cargar_textura(textura_path)
                
                self.personajes[nombre_personaje][nombre_extremidad] = {
                    'vao': vao,
                    'vbo_vertices': vbo_vertices,
                    'vbo_colores': vbo_colores,
                    'vbo_texcoords': vbo_texcoords,
                    'ebo': ebo,
                    'vertices': vertices,
                    'colores': colores,
                    'coords_textura': coords_textura,
                    'faces': faces,
                    'primitive': primitive,
                    'id_textura': id_textura
                }
                
                glBindVertexArray(0)
                glBindBuffer(GL_ARRAY_BUFFER, 0)
                if ebo:
                    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0)

    
    def render_personaje(self, nombre_personaje):       
        if nombre_personaje not in self.personajes:
            print(f"Personaje {nombre_personaje} no encontrado!")
            return        
            
        glEnable(GL_COLOR_MATERIAL)
        
        for extremidad, buffers in self.personajes[nombre_personaje].items():
            if "Esfera" in extremidad:
                radio = buffers['radio']
                slices = 16  
                stacks = 8  
                
                glPushMatrix()
                color = buffers['colores'][0] if len(buffers['colores']) > 0 else [1.0, 1.0, 1.0, 1.0]
                glColor4fv(color)
                
                # Configuración de textura para la esfera
                if buffers['id_textura'] is not None:
                    glEnable(GL_TEXTURE_2D)
                    glBindTexture(GL_TEXTURE_2D, buffers['id_textura'])
                    quadric = gluNewQuadric()
                    gluQuadricTexture(quadric, GL_TRUE)  # Habilitar coordenadas de textura
                    gluQuadricNormals(quadric, GLU_SMOOTH)
                else:
                    quadric = gluNewQuadric()
                
                glTranslatef(*buffers['centro'])
                glRotatef(-90.0, 1.0, 0.0, 0.0)

                gluSphere(quadric, radio, slices, stacks)
                
                if buffers['id_textura'] is not None:
                    glDisable(GL_TEXTURE_2D)
                    
                gluDeleteQuadric(quadric)
                glPopMatrix()
                continue
            
            glBindVertexArray(buffers['vao'])
            
            # Si hay textura, configurarla
            if buffers['id_textura']:
                glEnable(GL_TEXTURE_2D)
                glBindTexture(GL_TEXTURE_2D, buffers['id_textura'])
            
            # Configuración explícita de color para otras geometrías
            if len(buffers['colores']) > 0:
                glEnableClientState(GL_COLOR_ARRAY)
                glBindBuffer(GL_ARRAY_BUFFER, buffers['vbo_colores'])
                glColorPointer(4, GL_FLOAT, 0, None)
            
            # Dibujar
            if buffers['ebo'] is not None:
                glDrawElements(
                    buffers['primitive'],
                    len(buffers['faces']),
                    GL_UNSIGNED_INT,
                    None
                )
            else:
                glDrawArrays(
                    buffers['primitive'],
                    0,
                    len(buffers['vertices'])
                )
            
            # Limpieza
            if len(buffers['colores']) > 0:
                glDisableClientState(GL_COLOR_ARRAY)
            
            if buffers['id_textura']:
                glDisable(GL_TEXTURE_2D)
            
            glBindVertexArray(0)
        
        glDisable(GL_COLOR_MATERIAL)

    
    def limpiar_buffers(self):
        # Limpiar buffers de geometría
        for personaje in self.personajes.values():
            for buffers in personaje.values():
                if 'centro' in buffers and 'radio' in buffers:
                    continue
                    
                if buffers['vao']:
                    glDeleteVertexArrays(1, [buffers['vao']])
                if buffers['vbo_vertices']:
                    glDeleteBuffers(1, [buffers['vbo_vertices']])
                if buffers['vbo_colores']:
                    glDeleteBuffers(1, [buffers['vbo_colores']])
                if buffers['vbo_texcoords']:
                    glDeleteBuffers(1, [buffers['vbo_texcoords']])
                if buffers['ebo']:
                    glDeleteBuffers(1, [buffers['ebo']])
                    
        # Limpiar texturas
        for id_textura in self.texturas.values():
            glDeleteTextures(1, [id_textura])