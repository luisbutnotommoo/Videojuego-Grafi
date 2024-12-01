import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image 


class Personaje:
    def __init__(self, nombre,geometrias):
        self.nombre = nombre
        self.texturas = {}  
        self.extremidades={}

        for clave in geometrias: 
            valor=geometrias[clave]
            self.agregar_extremidad(clave,valor)
            
        
               
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
        

    def agregar_extremidad(self, nombre_extremidad, geometria):
        caseCorrecto=""+nombre_extremidad

        if "Esfera" in nombre_extremidad:
            caseCorrecto="Esfera"

        if "Cilindro" in nombre_extremidad:
            caseCorrecto="Cilindro"

        match caseCorrecto:
            case "Esfera":
                centro = geometria['centro']
                radio = geometria['radio']
                color = geometria.get('colors', [1.0, 1.0, 1.0, 1.0])
                colores = np.array([color], dtype=np.float32)
            
                # Agregar soporte para textura en esferas
                textura = None
                if 'textura' in geometria:
                    textura = self.cargar_textura(geometria['textura'])
                
            
                self.extremidades[nombre_extremidad] = {            
                    'centro': centro,
                    'radio': radio,
                    'colores': colores,
                    'id_textura': textura
                }
            

            case "Cilindro":
                centro = geometria['centro']
                radio = geometria.get('radio', 0.5)
                altura = geometria.get('altura', 1.0)
                color = geometria.get('colors', [1.0, 1.0, 1.0, 1.0])
                colores = np.array([color], dtype=np.float32)
                rotacion=[-90,1,0,0]
                if 'rotate' in geometria:
                    rotacion=geometria['rotate']
        
                # Agregar soporte para textura en cilindros
                textura = None
                if 'textura' in geometria:
                    textura = self.cargar_textura(geometria['textura'])
        
                self.extremidades[nombre_extremidad] = {            
                    'centro': centro,
                    'radio': radio,
                    'altura': altura,
                    'colores': colores,
                    'id_textura': textura,
                    'rotate':rotacion
                }
            
            case _:
                vertices = np.array(geometria['vertices'], dtype=np.float32)
                faces = np.array(geometria.get('faces', []), dtype=np.uint32)
                primitive = geometria.get('primitive', GL_TRIANGLES)
            
                # Crear array de colores para cada vértice
                color = geometria.get('colors', [1.0, 1.0, 1.0, 1.0])
                colores = np.tile(color, (len(vertices), 1)).astype(np.float32)
            
                # Crear VAO y VBOs
                vao = glGenVertexArrays(1)
                vbo_vertices = glGenBuffers(1)
                vbo_colores = glGenBuffers(1)
            
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
            
                # EBO si hay faces
                if len(faces) > 0:
                    ebo = glGenBuffers(1)
                    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ebo)
                    glBufferData(GL_ELEMENT_ARRAY_BUFFER, faces.nbytes, faces, GL_STATIC_DRAW)
                else:
                    ebo = None
            
                # Cargar textura si existe
                id_textura = None
                if 'textura' in geometria:
                    id_textura = self.cargar_textura(geometria['textura'])
            
                self.extremidades[nombre_extremidad] = {
                    'vao': vao,
                    'vbo_vertices': vbo_vertices,
                    'vbo_colores': vbo_colores,
                    'ebo': ebo,
                    'vertices': vertices,
                    'colores': colores,
                    'faces': faces,
                    'primitive': primitive,
                    'id_textura': id_textura
                }
            
                glBindVertexArray(0)
                glBindBuffer(GL_ARRAY_BUFFER, 0)
                if ebo: 
                    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0)
    

    def render(self):       
        glEnable(GL_COLOR_MATERIAL)
        
        for nombre_extremidad, buffers in self.extremidades.items():
            if "Esfera" in nombre_extremidad:
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

            elif "Cilindro" in nombre_extremidad:
                radio = buffers.get('radio', 0.5)
                altura = buffers.get('altura', 1.0)
                slices = 16
                stacks = 8

                glPushMatrix()
                color = buffers['colores'][0] if len(buffers['colores']) > 0 else [1.0, 1.0, 1.0, 1.0]
                glColor4fv(color)
            
            # Configuración de textura para el cilindro
                if buffers['id_textura'] is not None:
                    glEnable(GL_TEXTURE_2D)
                    glBindTexture(GL_TEXTURE_2D, buffers['id_textura'])
                    gluQuadricTexture(quadric, GL_TRUE)
                    gluQuadricNormals(quadric, GLU_SMOOTH)
                
                quadric = gluNewQuadric()
            
                glTranslatef(*buffers['centro'])
                glRotatef(*buffers['rotate'])

                # Renderizar cilindro
                gluCylinder(quadric, radio, radio, altura, slices, stacks)
            
                if buffers['id_textura'] is not None:
                    glDisable(GL_TEXTURE_2D)
                
                #gluDeleteQuadric(quadric)
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
        for buffers in self.extremidades.values():
            if 'centro' in buffers and 'radio' in buffers:
                continue
                
            if 'vao' in buffers and buffers['vao']:
                glDeleteVertexArrays(1, [buffers['vao']])
            if 'vbo_vertices' in buffers and buffers['vbo_vertices']:
                glDeleteBuffers(1, [buffers['vbo_vertices']])
            if 'vbo_colores' in buffers and buffers['vbo_colores']:
                glDeleteBuffers(1, [buffers['vbo_colores']])
            if 'ebo' in buffers and buffers['ebo']:
                glDeleteBuffers(1, [buffers['ebo']])
                
        # Limpiar texturas
        for id_textura in self.texturas.values():
            glDeleteTextures(1, [id_textura])


    def mover_extremidad(self, nombre_extremidad, desplazamiento):
        """
        Mueve una extremidad del personaje aplicando un desplazamiento a su posición.

        :param nombre_extremidad: Nombre de la extremidad a mover.
        :param desplazamiento: Lista o tupla de tres valores [dx, dy, dz] que indica el movimiento.
        """
        if nombre_extremidad not in self.extremidades:
            print(f"Extremidad '{nombre_extremidad}' no encontrada.")
            return
    
        buffers = self.extremidades[nombre_extremidad]
    
        if 'centro' in buffers:
        # Mover esferas o cilindros
            buffers['centro'] = [c + d for c, d in zip(buffers['centro'], desplazamiento)]
        elif 'vertices' in buffers:
        # Mover geometrías basadas en vértices
            vertices = buffers['vertices']
            desplazamiento_array = np.array(desplazamiento, dtype=np.float32)
            buffers['vertices'] = vertices + desplazamiento_array
        
        # Actualizar el VBO de vértices en OpenGL
            glBindBuffer(GL_ARRAY_BUFFER, buffers['vbo_vertices'])
            glBufferSubData(GL_ARRAY_BUFFER, 0, buffers['vertices'].nbytes, buffers['vertices'])
            glBindBuffer(GL_ARRAY_BUFFER, 0)
        else:
            print(f"La extremidad '{nombre_extremidad}' no se puede mover.")
          
    def mover_personaje(self,desplazamiento):
        for clave in self.extremidades:
            self.mover_extremidad(clave,desplazamiento)
