from OpenGL.GL import GL_QUADS,GL_TRIANGLES


import os

ruta_actual = os.path.dirname(__file__)

#Colores
negro= (0.01,0.01,0.01,1.0)
blanco=(1.0,1.0,1.0,1.0)
gris=(0.5,0.5,0.5,1.0)
marron=(0.7, 0.5, 0.3,1.0)
marron_oscuro = (0.49, 0.35, 0.21,1.0)
plata=(0.9, 0.9, 0.8,1.0)
azul=(0.5, 0.8, 1.0,1.0)

#Heisenpurr
prisma_caras = [
    0, 1, 2, 3,  
    4, 5, 6, 7,  
    0, 1, 5, 4,  
    3, 2, 6, 7,  
    0, 3, 7, 4, 
    1, 2, 6, 5 
]

piramide_triangulo_caras = [
    3,0,2,
    3,2,1,
    3,1,0
]

piramide_cuadrado_caras = [
    4,0,1,
    4,0,2,
    4,2,3,
    4,3,1,
    4,0,2
]

heisenpurr_cuerpo = [
    [1, 1.11, -1],      
    [1, 1.11, 1],       
    [-1, 1.11, 1],     
    [-1, 1.11, -1],     
    [1, 3.11, -1],      
    [1, 3.11, 1],      
    [-1, 3.11, 1],      
    [-1, 3.11, -1]      
]

heisenpurr_cola = [
    [-0.11, 1.8, -1],      # [0.11, 1.8, 1]
    [0.11, 1.8, -1],       # [-0.11, 1.8, 1]
    [0.19, 1.43, -1],      # [-0.19, 1.43, 1]
    [0, 1.43, -1],         # [0, 1.43, 1]
    [-0.11, 1.8, -2.2],    # [0.11, 1.8, 2.2]
    [0.11, 1.8, -2.2],     # [-0.11, 1.8, 2.2]
    [0.19, 1.43, -2.2],    # [-0.19, 1.43, 2.2]
    [0, 1.43, -2.2]        # [0, 1.43, 2.2]
]

heisenpurr_brazo = [
    [-0.9, 2.69, 0.46],   
    [-0.9, 2.69, -0.52],   
    [-0.9, 1.85, 0.46],   
    [-0.9, 1.85, -0.52],   
    [-2, 1.19, -0.02]      #apice
]

heisenpurr_brazo_apice=heisenpurr_brazo[4]

heisenpurr_brazo2 = [
    [0.9, 2.69, 0.46],     
    [0.9, 2.69, -0.52],    
    [0.9, 1.85, 0.46],     
    [0.9, 1.85, -0.52],    
    [2, 1.19, -0.02]       # apice
]

heisenpurr_oreja = [
    [0.04, 4.43, 0.3],     
    [0.41, 4.36, 0.09],    
    [0.14, 4.44, -0.23],   
    [0.28, 5.21, 0.03]     # apice
]

heisenpurr_oreja2 = [
    [-0.04, 4.43, 0.3],    
    [-0.41, 4.36, 0.09],   
    [-0.14, 4.44, -0.23],  
    [-0.28, 5.21, 0.03]    
]

heisenpurr_pata = [
    [0.63, 1.41, 0.29],    
    [0.63, 1.41, -0.29],  
    [0.13, 1.41, -0.29],   
    [0.13, 1.41, 0.29],   
    [0.63, 0.11, 0.29],   
    [0.63, 0.11, -0.29],  
    [0.13, 0.11, -0.29],   
    [0.13, 0.11, 0.29]    
]

heisenpurr_pata2 = [
    [-0.63, 1.41, 0.29],   
    [-0.63, 1.41, -0.29],  
    [-0.13, 1.41, -0.29],  
    [-0.13, 1.41, 0.29],   
    [-0.63, 0.11, 0.29],   
    [-0.63, 0.11, -0.29],  
    [-0.13, 0.11, -0.29],  
    [-0.13, 0.11, 0.29]    
]

heisenpurr_cabeza=[[0,3.74,0],0.75]

heisenpurr_geometries = {
    'Cuerpo': {
        'vertices': heisenpurr_cuerpo,
        'faces': prisma_caras,
        'primitive': GL_QUADS,
        'colors': marron
    },
    'Cola': {
        'vertices': heisenpurr_cola,
        'faces': prisma_caras,
        'primitive': GL_QUADS,

    },
    'Pata': {
        'vertices': heisenpurr_pata,
        'faces': prisma_caras,
        'primitive': GL_QUADS,

    },
    'Pata2': {
        'vertices': heisenpurr_pata2,
        'faces': prisma_caras,
        'primitive': GL_QUADS,

    },
    'Brazo': {
        'vertices': heisenpurr_brazo,
        'faces': piramide_cuadrado_caras,
        'primitive': GL_TRIANGLES,                   
    },
    'Brazo2': {
        'vertices': heisenpurr_brazo2,
        'faces': piramide_cuadrado_caras,
        'primitive': GL_TRIANGLES,
    },
    'Oreja': {
        'vertices': heisenpurr_oreja,
        'faces': piramide_triangulo_caras,
        'primitive': GL_TRIANGLES,
    },                                                      
    'Oreja2': {
        'vertices': heisenpurr_oreja2,
        'faces': piramide_triangulo_caras,
        'primitive': GL_TRIANGLES,
        'colors': negro
    },
    'Esfera':{
        'centro': heisenpurr_cabeza[0],
        'radio': heisenpurr_cabeza[1],
        'textura': os.path.join(ruta_actual, ('mi_mapa_uv.png'))
    }                       
}

heisenpurr_diccionario=["Heisenpurr",heisenpurr_geometries]









