import os

# segun la ruta del proyecto asigamos sonidos y texturas
ruta_actual = os.path.dirname(__file__)

sonido1 = os.path.join(ruta_actual, '..', 'SonidosLuis', 'sonido1.wav')
sonido2 = os.path.join(ruta_actual,'..', 'SonidosLuis', 'sonido2.wav')
sonido3 = os.path.join(ruta_actual,'..', 'SonidosLuis', 'sonido3.wav')
sonido4 = os.path.join(ruta_actual,'..', 'SonidosLuis', 'sonido4.wav')
sonido5 = os.path.join(ruta_actual,'..', 'SonidosLuis', 'sonido5.wav')
sonido6 = os.path.join(ruta_actual,'..', 'SonidosLuis', 'sonido6.wav')
sonido7 = os.path.join(ruta_actual,'..', 'SonidosLuis', 'sonido7.wav')

pared1=os.path.join(ruta_actual, '..','ImagenesLuis', ('pared1.jpg'))
piso1=os.path.join(ruta_actual, '..','ImagenesLuis', ('piso1.jpg'))

pared2=os.path.join(ruta_actual,'..', 'ImagenesLuis', ('pared2.jpg'))
piso2=os.path.join(ruta_actual,'..', 'ImagenesLuis', ('piso2.jpg'))

pared3=os.path.join(ruta_actual,'..', 'ImagenesLuis', ('pared3.jpg'))
piso3=os.path.join(ruta_actual,'..', 'ImagenesLuis', ('piso3.jpg'))

pared4=os.path.join(ruta_actual, '..','ImagenesLuis', ('pared4.jpg'))
piso4=os.path.join(ruta_actual, '..','ImagenesLuis', ('piso4.jpg'))

pared5=os.path.join(ruta_actual,'..', 'ImagenesLuis', ('pared5.jpg'))
piso5=os.path.join(ruta_actual,'..', 'ImagenesLuis', ('piso5.jpg'))

pared6=os.path.join(ruta_actual,'..', 'ImagenesLuis', ('pared6.jpg'))
piso6=os.path.join(ruta_actual,'..', 'ImagenesLuis', ('piso6.jpg'))

pared7=os.path.join(ruta_actual,'..', 'ImagenesLuis', ('pared7.jpg'))
piso7=os.path.join(ruta_actual,'..', 'ImagenesLuis', ('piso7.jpg'))

menu=os.path.join(ruta_actual,'..', 'ImagenesLuis', ('menu.png'))
creditos=os.path.join(ruta_actual,'..', 'ImagenesLuis', ('creditos.png'))


#agrupamos
e1=(pared1,piso1,sonido1)
e2=(pared2,piso2,sonido2)
e3=(pared3,piso3,sonido3)
e4=(pared4,piso4,sonido4)
e5=(pared5,piso5,sonido5)
e6=(pared6,piso6,sonido6)
e7=(pared7,piso7,sonido7)

ambiente=(e1,e2,e3,e4,e5,e6,e7)