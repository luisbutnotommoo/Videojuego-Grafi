import PersonajeLuis.AccionesLuis.escultor as escultor


radio=3.03
centro=[2, 3.13, 7]


ceja1=[
    [2.19, 4.46, 6.3],
    [2.79, 4.01, 7-0.66]
]

ceja2=[
    [4.61, 4.52, 7-0.48],
    [4.0, 3.97, 7-0.19]
]

ojo1=[
    [2.28, 3.47, 7-0.53],
    [2.37, 2.56, 7-0.51]
]

ojo2=[
    [4.59, 3.25, 7-0.03],
    [4.63, 2.32, 7-0.15]
]

cara=[ojo1,ojo2,ceja1,ceja2]
cuerpo=[centro,radio,(0,0,1),cara]

#intento de enemigo (sale mal)


class Enemigo():
    def render_enemigo(self):
        global cara, cuerpo
        escultor.render_esfera(*cuerpo)

        
    def __init__(self):
        global centro
        self.width = 6.16  
        self.posicion = centro
    
        

		
        