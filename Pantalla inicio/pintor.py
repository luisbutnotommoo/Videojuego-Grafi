#Pintor se encargará de manejar las formas

matriz_base1 = [ [2.0,1.5], [2.5,1], [3.5,0.5], [5.5,0.5], [6.5,1.0],  [7.0,1.5]]
matriz_base2 = [ [7.0,1.5], [6.0,9.0], [5.0,8.5],  [4.0,8.5], [3.0,9.0], [2.0,1.5]]

matriz_tapa6 = [  [4.5, 11], [4, 10], [3, 9.5], [4, 9], [5, 9], [6, 9.5],[5,10]]

matriz_tapa1=[[4.5,11],[4,10],[5,10]]

matriz_tapa2=[[3,9.5],[4,9],[5,9],[6,9.5],[4,10],[5,10],[6,9.5]]

matriz_tapa3=[
    [3,9.5],
    [3,9],
    [4,8.5],
    [4,9],
    [3,9.5]
]

matriz_tapa4=[
    [4,8.5],
    [4,9],
    [5,9],
    [5,8.5]
]

matriz_tapa5=[
    [5,9],
    [5,8.5],
    [6,9],
    [6,9.5],
    [5,9]
]


matriz_boquilla1=[
    [6.6,4],
    [7.5,4],
    [8.3,3],
    [6.7,3]
]
matriz_boquilla2=[
    [7.5,4],
    [8.5,6],
    [9,5.5],
    [8.3,3],
    [7.5,4]   
]

matriz_boquilla3=[
    [8.5,6],
    [9,5.5],
    [9.5,5.5],
    [9.5,6]
]



matriz_asa1=[
    [2,9],
    [2,8],
    [2.8,6.8],
    [2.8,7.5],
    [2,9]
]    
matriz_asa2=[
    [1,8],
    [1.5,7.5],
    [2,8],
    [2,9],
    [1,8]
]

matriz_asa3=[
    [1,8],
    [1,5],
    [1.5,5],
    [1.5,7.5],
    [1,8]
]
matriz_asa4=[
    [1,5],
    [2.3,3],
    [2.3,4],
    [1.5,5]
]

mesa=[
    [7.8,1.16],
    [6.36,0.3],
    [1,0.3],
    [2.7,1.16],
    [7.8,1.16],
]

mesa_grosor_sombra=[[7.8,1.16],[7.8,0.96],[6.36,0],[6.36,0.3],[7.8,1.16]]
mesa_grosor_ilum=[[1,0],[1,0.3],[6.36,0.3],[6.36,0],[1,0]]
mesa_pata=[[7.8,1.16],[7.8,0],[7.59,0],[7.59,1],[7.8,1.16]]
mesa_pata_sombra=[[7.59,0.82],[7.5,0.76],[7.5,0],[7.59,0],[7.59,0.82]]

matriz_base=[matriz_base1,matriz_base2]

matriz_taza=[[5.44,1],[5.44,0.8],[5.54,0.6],[5.84,0.6],[5.94,0.8],[5.94,1]]
matriz_taza_asa=[(594,310),(604,310),(614,320),(599,330),(580,330)]


tupla_azucarera=[(269,288)]
matriz_azucarera=[[299,285],[299,334],[270,310]]
matriz_azucarera2=[[324,285],[324,334],[350,310]]

montaña=[[3.44,1.74], [4.48,2.8],[5.44,3.26],[5.84,2.42],[7.72,1.74],[3.44,1.74]]

matriz_pared_atras=[[800,0],[270,0],[270,264],[800,264],[800,0]]
matriz_pared_sombra=[[270,264],[270,0],[0,0],[0,400],[270,264]]




def convierte_coordenadas(matriz):
    resultado = []
    for coords in matriz:
        coords_ajustadas = [coords[0] * 100, 400 - coords[1] * 100]
        resultado.append(coords_ajustadas)
    return resultado

        
def convierte_coordenadas_dobles(matriz_de_matrices):
    resultado=[]
    for submatriz in matriz_de_matrices:
        resultado.extend(convierte_coordenadas(submatriz))
    
    return resultado

def escala_matriz_matrices(matriz_matrices):
    matriz_escalada = []
    for matriz in matriz_matrices:        
        matriz_escalada.append(escala_matriz(matriz))
    return matriz_escalada

def escala_matriz(matriz):
    factor=0.19
    matriz_escalada = []
    for fila in matriz:
        nueva_fila = [elemento * factor for elemento in fila]
        matriz_escalada.append(nueva_fila)
    traslada_matriz(matriz_escalada)
    return matriz_escalada

def traslada_matriz(matriz):
  for fila in matriz:
    fila[0] += 3.2
    fila[1] += 0.5

