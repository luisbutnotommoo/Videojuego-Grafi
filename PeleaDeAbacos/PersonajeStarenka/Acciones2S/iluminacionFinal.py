from OpenGL.GL import *
from OpenGL.GLU import *

class iluminacion:
    def __init__(self):
        # Posición de la luz
        self.light_position = [150, 0, -250.0, 1.0]

        # Configuración para iluminación interpolada
        self.interpolated_light = {
            'ambient': [0.3, 0.3, 0.3, 1.0],
            'diffuse': [0.7, 0.7, 0.7, 1.0],
            'specular': [0.2, 0.2, 0.2, 1.0]
        }

        # Configuración para Gouraud
        self.gouraud_light = {
            'ambient': [0.2, 0.2, 0.2, 1.0],
            'diffuse': [1.0, 1.0, 1.0, 1.0],
            'specular': [0.6, 0.6, 0.6, 1.0]
        }

        # Configuración para Phong
        self.phong_light = {
            'ambient': [0.1, 0.1, 0.1, 1.0],
            'diffuse': [1.0, 1.0, 1.0, 1.0],
            'specular': [1.0, 1.0, 1.0, 1.0]
        }

        # Material especular y brillo (común para todos los modos)
        self.material_specular = [1.0, 1.0, 1.0, 1.0]

    def iluminacionInterpolada(self):
        """Implementación básica de iluminación interpolada"""
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glShadeModel(GL_FLAT)  # Sombreado plano para interpolación básica
        
        # Habilitar materiales de color
        glEnable(GL_COLOR_MATERIAL)
        glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)
        
        # Configurar luz con valores más suaves
        glLightfv(GL_LIGHT0, GL_POSITION, self.light_position)
        glLightfv(GL_LIGHT0, GL_AMBIENT, self.interpolated_light['ambient'])
        glLightfv(GL_LIGHT0, GL_DIFFUSE, self.interpolated_light['diffuse'])
        glLightfv(GL_LIGHT0, GL_SPECULAR, self.interpolated_light['specular'])
        
        # Sin atenuación para mantener la iluminación simple
        glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 1.0)
        glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.0)
        glLightf(GL_LIGHT0, GL_QUADRATIC_ATTENUATION, 0.0)
        
        # Brillo bajo para superficies más mate
        glMaterialfv(GL_FRONT, GL_SPECULAR, [0.2, 0.2, 0.2, 1.0])
        glMaterialf(GL_FRONT, GL_SHININESS, 8.0)

    def iluminacionGourad(self):
        """Implementación de iluminación Gouraud"""
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glShadeModel(GL_SMOOTH)  # Sombreado suave característico de Gouraud
        
        # Habilitar materiales de color
        glEnable(GL_COLOR_MATERIAL)
        glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)
        
        # Configurar luz con valores intermedios
        glLightfv(GL_LIGHT0, GL_POSITION, self.light_position)
        glLightfv(GL_LIGHT0, GL_AMBIENT, self.gouraud_light['ambient'])
        glLightfv(GL_LIGHT0, GL_DIFFUSE, self.gouraud_light['diffuse'])
        glLightfv(GL_LIGHT0, GL_SPECULAR, self.gouraud_light['specular'])
        
        # Atenuación moderada
        glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 1.0)
        glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
        glLightf(GL_LIGHT0, GL_QUADRATIC_ATTENUATION, 0.0)
        
        # Brillo moderado
        glMaterialfv(GL_FRONT, GL_SPECULAR, self.material_specular)
        glMaterialf(GL_FRONT, GL_SHININESS, 32.0)

    def iluminacionPhong(self):
        """Implementación de iluminación Phong"""
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glShadeModel(GL_SMOOTH)  # Sombreado suave necesario para Phong
        
        # Habilitar materiales de color
        glEnable(GL_COLOR_MATERIAL)
        glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)
        
        # Configurar luz con valores más intensos
        glLightfv(GL_LIGHT0, GL_POSITION, self.light_position)
        glLightfv(GL_LIGHT0, GL_AMBIENT, self.phong_light['ambient'])
        glLightfv(GL_LIGHT0, GL_DIFFUSE, self.phong_light['diffuse'])
        glLightfv(GL_LIGHT0, GL_SPECULAR, self.phong_light['specular'])
        
        # Atenuación más pronunciada
        glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 1.0)
        glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
        glLightf(GL_LIGHT0, GL_QUADRATIC_ATTENUATION, 0.02)
        
        # Brillo alto para reflejos más definidos
        glMaterialfv(GL_FRONT, GL_SPECULAR, self.material_specular)
        glMaterialf(GL_FRONT, GL_SHININESS, 128.0)
        
        glEnable(GL_NORMALIZE)

    def desactivarLuz(self):
        glDisable(GL_LIGHTING)
        glDisable(GL_LIGHT0)
        glDisable(GL_COLOR_MATERIAL)