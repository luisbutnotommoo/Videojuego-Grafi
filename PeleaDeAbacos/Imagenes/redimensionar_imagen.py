from PIL import Image
import os

ruta_actual = os.path.dirname(__file__)

def resize_image(image_path, output_path, size=(256, 256)):
    try:
        # Abre la imagen
        im = Image.open(image_path)

        # Redimensionar la imagen usando el filtro LANCZOS
        im = im.resize(size, Image.LANCZOS)

        # Guardar la nueva imagen
        im.save(output_path)
        print(f"Imagen redimensionada y guardada en: {output_path}")
    except Exception as e:
        print(f"Error al redimensionar la imagen: {e}")

if __name__ == "__main__":
    # Ruta de la imagen original
    original_image_path = os.path.join(ruta_actual,"moradoPocima.jpg")
    
    # Ruta donde se guardará la imagen redimensionada
    resized_image_path = os.path.join(ruta_actual,"moradoPocimaOrg.jpg")

    # Llamar a la función de redimensionar
    resize_image(original_image_path, resized_image_path)
