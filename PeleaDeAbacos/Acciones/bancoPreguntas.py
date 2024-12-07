import random
import operator
import math

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
        '/': operator.truediv,
    }

    def __init__(self, profundidad_max=4, rango_numeros=(-11, 11)):
        self.profundidad_max = profundidad_max
        self.rango_numeros = rango_numeros

    def generar_arbol_operaciones(self, profundidad_actual=0):
        
        if profundidad_actual >= self.profundidad_max:
            return NodoOperacion(random.randint(*self.rango_numeros))

        if profundidad_actual == 0 or profundidad_actual < self.profundidad_max - 1:
            # Generar nodo de operación
            operador = random.choice(list(self.OPERADORES.keys()))
            nodo = NodoOperacion(operador)
            
            # Generar subárboles izquierdo y derecho
            nodo.izquierda = self.generar_arbol_operaciones(profundidad_actual + 1)
            nodo.derecha = self.generar_arbol_operaciones(profundidad_actual + 1)

            return nodo
        
        # En los últimos niveles, generar solo números
        return NodoOperacion(random.randint(*self.rango_numeros))

    def evaluar_arbol(self, nodo):
        if not isinstance(nodo.valor, str):
            return nodo.valor
        
        # Obtener valores de los subárboles
        izq = self.evaluar_arbol(nodo.izquierda)
        der = self.evaluar_arbol(nodo.derecha)
        
        # Aplicar operación
        try:
            resultado = self.OPERADORES[nodo.valor](izq, der)
            
            # Manejo especial para división
            if nodo.valor == '/' and isinstance(resultado, float):
                # Redondear a 2 decimales si es necesario
                return round(resultado, 2)
            
            return resultado
        except (ZeroDivisionError, OverflowError, ValueError):
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
        self.generador_arboles = ArbolOperaciones(profundidad_max=dificultad + 1)
        self.preguntas_usadas = set()

    def generar_pregunta(self):
        """
        Genera una pregunta única en tiempo real
        
        :return: Diccionario con la pregunta generada
        """
        intentos_max = 20  # Límite de intentos para evitar bucle infinito
        intentos = 0

        while intentos < intentos_max:
            # Generar árbol de operaciones
            arbol = self.generador_arboles.generar_arbol_operaciones()
            
            # Evaluar resultado
            resultado = self.generador_arboles.evaluar_arbol(arbol)
            
            # Omitir si no se puede evaluar o ya se ha usado
            if (resultado is None or 
                resultado in self.preguntas_usadas or
                math.isnan(resultado) or 
                math.isinf(resultado)):
                intentos += 1
                continue
            
            # Formatear el resultado
            if isinstance(resultado, float):
                # Redondear a 2 decimales si es un flotante
                resultado = round(resultado, 2)
            
            # Convertir a entero si es posible
            if isinstance(resultado, float) and resultado.is_integer():
                resultado = int(resultado)
            
            # Generar opciones de respuesta
            opciones = [resultado]
            while len(opciones) < 3:
                # Generar variaciones de la respuesta
                if isinstance(resultado, int):
                    variacion = resultado + random.randint(-10, 10)
                else:
                    variacion = round(resultado + random.uniform(-2, 2), 2)
                
                if variacion not in opciones:
                    opciones.append(variacion)
            
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

        # Si no se puede generar una pregunta válida
        raise ValueError("No se pudo generar una pregunta válida después de múltiples intentos")

    def reiniciar_preguntas(self):
        """
        Reinicia el conjunto de preguntas usadas
        """
        self.preguntas_usadas.clear()