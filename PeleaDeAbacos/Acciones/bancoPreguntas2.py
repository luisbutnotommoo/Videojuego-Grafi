import random
import operator

class NodoOperacion:
    def __init__(self, valor=None, izquierda=None, derecha=None):
        self.valor = valor
        self.izquierda = izquierda
        self.derecha = derecha

class ArbolOperaciones:
    OPERADORES = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }

    def __init__(self, profundidad_max=3, rango_numeros=(-20, 20)):
        self.profundidad_max = profundidad_max
        self.rango_numeros = rango_numeros

    def generar_arbol_operaciones(self, profundidad_actual=0):
        # Condición de parada
        if profundidad_actual >= self.profundidad_max:
            return NodoOperacion(random.randint(*self.rango_numeros))

        # Decidir si es un nodo hoja (número) o un nodo de operación
        if random.random() < 0.5 and profundidad_actual > 0:
            return NodoOperacion(random.randint(*self.rango_numeros))

        # Generar nodo de operación
        operador = random.choice(list(self.OPERADORES.keys()))
        nodo = NodoOperacion(operador)
        
        # Generar subárboles izquierdo y derecho
        nodo.izquierda = self.generar_arbol_operaciones(profundidad_actual + 1)
        nodo.derecha = self.generar_arbol_operaciones(profundidad_actual + 1)

        return nodo

    def evaluar_arbol(self, nodo):
        # Evalúa recursivamente el árbol de operaciones
        if not isinstance(nodo.valor, str):
            return nodo.valor
        
        # Obtener valores de los subárboles
        izq = self.evaluar_arbol(nodo.izquierda)
        der = self.evaluar_arbol(nodo.derecha)
        
        # Aplicar operación
        try:
            return self.OPERADORES[nodo.valor](izq, der)
        except (ZeroDivisionError, OverflowError):
            return None

    def representacion_arbol(self, nodo):
        # Genera representación en cadena del árbol
        if not isinstance(nodo.valor, str):
            return str(nodo.valor)
        
        return f"({self.representacion_arbol(nodo.izquierda)} {nodo.valor} {self.representacion_arbol(nodo.derecha)})"

class BancoPreguntas:
    def __init__(self, dificultad=1):
        """
        Inicializa el banco de preguntas con generación dinámica
        
        :param dificultad: Profundidad máxima del árbol de operaciones
        """
        self.generador_arboles = ArbolOperaciones(profundidad_max=dificultad)
        self.preguntas_usadas = set()

    def generar_pregunta(self):
        """
        Genera una pregunta única en tiempo real
        
        :return: Diccionario con la pregunta generada
        """
        while True:
            # Generar árbol de operaciones
            arbol = self.generador_arboles.generar_arbol_operaciones()
            
            # Evaluar resultado
            resultado = self.generador_arboles.evaluar_arbol(arbol)
            
            # Omitir si no se puede evaluar o ya se ha usado
            if (resultado is None or 
                not isinstance(resultado, (int, float)) or 
                resultado in self.preguntas_usadas):
                continue
            
            # Redondear y convertir a entero
            resultado = int(round(resultado))
            
            # Generar opciones de respuesta
            opciones = [resultado]
            while len(opciones) < 3:
                opcion = resultado + random.randint(-20, 20)
                if opcion not in opciones:
                    opciones.append(opcion)
            
            random.shuffle(opciones)
            
            # Crear pregunta
            pregunta = {
                'texto': f"¿Cuánto es {self.generador_arboles.representacion_arbol(arbol)}?\n" + 
                         "\n".join([f"{chr(97+i)}) {opcion}" for i, opcion in enumerate(opciones)]),
                'respuesta_correcta': chr(97 + opciones.index(resultado)),
                'resultado': resultado
            }
            
            # Marcar resultado como usado para evitar repeticiones
            self.preguntas_usadas.add(resultado)
            
            return pregunta

    def reiniciar_preguntas(self):
        """
        Reinicia el conjunto de preguntas usadas
        """
        self.preguntas_usadas.clear()

'''def main():
    # Crear banco de preguntas con generación dinámica
    banco = BancoPreguntas(dificultad=3)
    
    # Generar y mostrar 10 preguntas diferentes
    for i in range(20):
        pregunta = banco.generar_pregunta()
        print(f"Pregunta {i+1}:")
        print(pregunta['texto'])
        print(f"Respuesta correcta: {pregunta['respuesta_correcta']}")
        print(f"Resultado: {pregunta['resultado']}\n")

if __name__ == "__main__":
    main()'''