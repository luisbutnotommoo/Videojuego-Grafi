from PIL import Image
from OpenGL.GL import*
import os

ruta_carpeta_imagenes = os.path.dirname(__file__)


def cargar_imagen(nombre_archivo):
    return os.path.join(ruta_carpeta_imagenes,nombre_archivo)

def redimenciona_img(image_path, output_path, size=(256, 256)):
    try:
        im = Image.open(image_path)
        im = im.resize(size, Image.LANCZOS)

        im.save(output_path)
        print(f"Imagen redimensionada y guardada en: {output_path}")
    except Exception as e:
        print(f"Error al redimensionar la imagen: {e}")


def cargar_textura(nombre_archivo):
        """
        Carga una textura y retorna su ID
        """            
        ruta_textura=cargar_imagen(nombre_archivo)
        imagen = Image.open(ruta_textura)
        datos_imagen = imagen.convert("RGBA").tobytes()
        
        id_textura = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, id_textura)
        
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        
        glTexImage2D(
            GL_TEXTURE_2D, 0, GL_RGBA, imagen.width, imagen.height, 0,
            GL_RGBA, GL_UNSIGNED_BYTE, datos_imagen
        )
        glGenerateMipmap(GL_TEXTURE_2D)
        
        return id_textura


