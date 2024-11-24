import random as ran
from random import choice

class bancoPreguntas:
    def __init__(self):
        self.numUno = 0
        self.numDos = 0
        self.numTres = 0
        self.respuesta = 0
        self.preguntaActual = None
        self.preguntas = []
        self.respuestaActual = None
        self.operacion1 = 0
        self.respuestaMala = 0
        self.respuestaMala2 = 0
        self.operacion2 = 0
        self.operacion3 = 0
        self.operacion4=0
        self.operacion5=0
        # Genera las preguntas al inicio
        ##self.elige_pregunta()
    
    def generar_numeros(self):
        self.numUno = ran.randint(-11, 11)
        self.numDos = ran.randint(-11, 11)
        self.numTres = ran.randint(-11, 11)

    def comprobarIgual(self):
        if(self.operacion1==self.respuestaMala):#
            self.respuestaMala=ran.randint(-51,50)
        if(self.operacion1==self.respuestaMala2):#
            self.respuestaMala2=ran.randint(-51,50)
        if(self.operacion2==self.respuestaMala):#
            self.respuestaMala=ran.randint(-51,50)
        if(self.operacion2==self.respuestaMala2):#
            self.respuestaMala2=ran.randint(-51,50)
        if(self.operacion3==self.respuestaMala):
            self.respuestaMala=ran.randint(-51,50)
        if(self.operacion3==self.respuestaMala2):
            self.respuestaMala2=ran.randint(-51,50)
        if(self.operacion4==self.respuestaMala):
            self.respuestaMala=ran.randint(-51,50)
        if(self.operacion4==self.respuestaMala2):
            self.respuestaMala2=ran.randint(-51,50)
        if(self.operacion5==self.respuestaMala):
            self.respuestaMala=ran.randint(-51,50)
        if(self.operacion5==self.respuestaMala2):
            self.respuestaMala2=ran.randint(-51,50)
        
        if(self.operacion1==self.respuestaMala or self.operacion1==self.respuestaMala2 or
            self.operacion2==self.respuestaMala or self.operacion2==self.respuestaMala2 or 
            self.operacion3==self.respuestaMala or self.operacion3==self.respuestaMala2 or
            self.operacion4==self.respuestaMala or self.operacion4==self.respuestaMala2 or
            self.operacion5==self.respuestaMala or self.operacion5==self.respuestaMala2 ):
                self.comprobarIgual()
            

    def generar_preguntasNivel1(self):
        # Genera nuevos números antes de cada pregunta
        self.comprobarIgual()
        self.operacion1 = self.numUno + self.numDos 
        self.respuestaMala = ran.randint(-51, 50)
        self.respuestaMala2 = ran.randint(-51, 50)
        self.operacion2 = self.numUno * self.numDos 
        self.operacion3 = self.numUno - self.numDos
        self.operacion4=self.numUno+self.numDos
        self.operacion5=self.numUno*self.numDos
        
        self.preguntas = [
            {"pregunta": f"¿Cuánto es ({self.numUno}) + ({self.numDos}) ?\n"
                         f"a) {self.operacion1}\n"
                         f"b) {self.respuestaMala}\n"
                         f"c) {self.respuestaMala2}", 
             "respuesta": "a"},

            {"pregunta": f"¿Cuánto es ({self.numUno}) * ({self.numDos})?\n"
                         f"a) {self.respuestaMala2}\n"
                         f"b) {self.operacion2}\n"
                         f"c) {self.respuestaMala}",
             "respuesta": "b"},

            {"pregunta": f"¿Cuánto es ({self.numUno}) - ({self.numDos})?\n"
                         f"a) {self.respuestaMala}\n"
                         f"b) {self.respuestaMala2}\n"
                         f"c) {self.operacion3}",
             "respuesta": "c"},

            {"pregunta": f"¿Cuánto es ({self.numUno}) + ({self.numDos}) ?\n"
                         f"a) {self.respuestaMala}\n"
                         f"b) {self.respuestaMala2}\n"
                         f"c) {self.operacion4}",
             "respuesta": "c"},
            
            {"pregunta": f"¿Cuánto es ({self.numUno}) * ({self.numDos}) ?\n"
                         f"a) {self.respuestaMala2}\n"
                         f"b) {self.operacion5}\n"
                         f"c) {self.respuestaMala}",
             "respuesta": "b"},

        ]
    
    def elige_pregunta(self):
        # Generar nuevas preguntas cada vez que se elige una pregunta
        self.generar_numeros()
        self.generar_preguntasNivel1()
        seleccionado = choice(self.preguntas)
        self.preguntaActual = seleccionado["pregunta"]
        self.respuestaActual = seleccionado["respuesta"]

    def generar_preguntasNivel2(self):
        # Genera nuevos números antes de cada pregunta
        self.comprobarIgual()
        self.operacion1 = self.numUno + self.numDos + self.numTres
        self.respuestaMala = ran.randint(-51, 50)
        self.respuestaMala2 = ran.randint(-51, 50)
        self.operacion2 = self.numUno * self.numDos -self.numTres
        self.operacion3 = self.numUno - self.numDos + self.numTres
        self.operacion4=self.numUno+self.numDos * self.numTres
        self.operacion5=self.numUno*self.numDos - self.numTres
        
        self.preguntas = [
            {"pregunta": f"¿Cuánto es ({self.numUno}) + ({self.numDos}) + ({self.numTres})?\n"
                         f"a) {self.operacion1}\n"
                         f"b) {self.respuestaMala}\n"
                         f"c) {self.respuestaMala2}", 
             "respuesta": "a"},

            {"pregunta": f"¿Cuánto es ({self.numUno}) * ({self.numDos}) - ({self.numTres})?\n"
                         f"a) {self.respuestaMala2}\n"
                         f"b) {self.operacion2}\n"
                         f"c) {self.respuestaMala}",
             "respuesta": "b"},

            {"pregunta": f"¿Cuánto es ({self.numUno}) - ({self.numDos}) + ({self.numTres})?\n"
                         f"a) {self.respuestaMala}\n"
                         f"b) {self.respuestaMala2}\n"
                         f"c) {self.operacion3}",
             "respuesta": "c"},

            {"pregunta": f"¿Cuánto es ({self.numUno}) + ({self.numDos}) * ({self.numTres})?\n"
                         f"a) {self.respuestaMala}\n"
                         f"b) {self.respuestaMala2}\n"
                         f"c) {self.operacion4}",
             "respuesta": "c"},
            
            {"pregunta": f"¿Cuánto es ({self.numUno}) * ({self.numDos}) - ({self.numTres})?\n"
                         f"a) {self.respuestaMala2}\n"
                         f"b) {self.operacion5}\n"
                         f"c) {self.respuestaMala}",
             "respuesta": "b"},

        ]
    def elige_pregunta2(self):
        # Generar nuevas preguntas cada vez que se elige una pregunta
            self.generar_numeros()
            self.generar_preguntasNivel2()
            seleccionado = choice(self.preguntas)
            self.preguntaActual = seleccionado["pregunta"]
            self.respuestaActual = seleccionado["respuesta"]
