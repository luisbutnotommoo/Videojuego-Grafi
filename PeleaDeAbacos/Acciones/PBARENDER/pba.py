import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

from personajes import Personajes
from coordenadas import heisenpurr_diccionario

def main():
    # Inicializar GLFW
    if not glfw.init():
        return
    
    # Crear ventana
    window = glfw.create_window(900, 900, "Demo MeshManager", None, None)
    if not window:
        glfw.terminate()
        return
        
    # Hacer el contexto OpenGL actual
    glfw.make_context_current(window)
    
    # Configuración inicial de OpenGL
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.2, 0.2, 0.2, 1.0)
    
    # Crear instancia del MeshManager
    mesh_manager = Personajes()
    
    # Agregar el personaje al mesh manager
    mesh_manager.agregar_personaje(heisenpurr_diccionario[0], heisenpurr_diccionario[1])
    
    # Configurar proyección
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, 1, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    
    # Loop principal
    while not glfw.window_should_close(window):
        # Limpiar buffers
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        # Configurar vista
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -19.0)
        
        # Renderizar personaje
        mesh_manager.render_personaje("Heisenpurr")
        
        # Intercambiar buffers y procesar eventos
        glfw.swap_buffers(window)
        glfw.poll_events()
    
    # Limpieza
    mesh_manager.limpiar_buffers()
    glfw.terminate()

if __name__ == "__main__":
    main()