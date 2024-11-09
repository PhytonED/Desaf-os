# 5_15_Arboles
# Número de desafío: 5
# Consigna: 
'''
Los árboles de expresiones son una herramienta poderosa en ciencias de la computación y se utilizan comúnmente para evaluar expresiones matemáticas. En este desafío, te propongo construir y evaluar un árbol de expresiones para una expresión matemática dada.
**Tu tarea es escribir un programa en Python que haga lo siguiente:**
* Construir el Árbol de Expresiones: Dada una expresión matemática en forma de cadena, construir el árbol de expresiones correspondiente. Puedes asumir que la expresión está bien formada y solo contiene números enteros, y los operadores +, -, *, /.
* Evaluar el Árbol de Expresiones: Una vez construido el árbol, evaluarlo y devolver el resultado de la expresión.
* Prueba tu Programa: Utiliza la expresión "5 + 3 * 4" para probar tu programa. El resultado debería ser 17.
## Consejos
Puedes crear una clase Nodo para representar los nodos en tu árbol de expresiones. Cada nodo debería tener un valor y dos hijos (izquierdo y derecho).
Puedes crear funciones auxiliares para ayudarte a construir y evaluar el árbol de expresiones.
Recuerda seguir las reglas de precedencia de operadores al construir el árbol.
'''
# Autora: Eliana D

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

def es_operador(c):
    """ Verificar si un carácter es un operador """
    return c in {'+', '-', '*', '/'}

def construir_arbol(expresion):
    """ Construir un árbol de expresiones a partir de una expresión dada """
    pila_nodos = []
    pila_operadores = []
    
    i = 0
    while i < len(expresion):
        if expresion[i].isdigit():
            # Extraer números completos (podrían ser de más de un dígito)
            num = ""
            while i < len(expresion) and expresion[i].isdigit():
                num += expresion[i]
                i += 1
            # Crear un nodo para el número y apilarlo
            pila_nodos.append(Nodo(int(num)))
            continue
        elif es_operador(expresion[i]):
            # Manejo de operadores con precedencia
            while (pila_operadores and precedencia(pila_operadores[-1]) >= precedencia(expresion[i])):
                nodo_derecho = pila_nodos.pop()
                nodo_izquierdo = pila_nodos.pop()
                operador = pila_operadores.pop()
                nuevo_nodo = Nodo(operador)
                nuevo_nodo.izquierdo = nodo_izquierdo
                nuevo_nodo.derecho = nodo_derecho
                pila_nodos.append(nuevo_nodo)
            # Apilar el operador actual
            pila_operadores.append(expresion[i])
        i += 1
    
    # Procesar los operadores restantes en la pila
    while pila_operadores:
        nodo_derecho = pila_nodos.pop()
        nodo_izquierdo = pila_nodos.pop()
        operador = pila_operadores.pop()
        nuevo_nodo = Nodo(operador)
        nuevo_nodo.izquierdo = nodo_izquierdo
        nuevo_nodo.derecho = nodo_derecho
        pila_nodos.append(nuevo_nodo)
    
    # El último nodo en la pila es la raíz del árbol de expresiones
    return pila_nodos[-1]

def precedencia(operador):
    """ Devolver la precedencia del operador """
    if operador in {'+', '-'}:
        return 1
    elif operador in {'*', '/'}:
        return 2
    return 0

def evaluar_arbol(nodo):
    """ Evaluar el árbol de expresiones de forma recursiva """
    if nodo is None:
        return 0
    # Si el nodo es un número, devolver el valor
    if not es_operador(nodo.valor):
        return nodo.valor
    # Evaluar los subárboles izquierdo y derecho
    izquierda = evaluar_arbol(nodo.izquierdo)
    derecha = evaluar_arbol(nodo.derecho)
    
    # Aplicar el operador correspondiente
    if nodo.valor == '+':
        return izquierda + derecha
    elif nodo.valor == '-':
        return izquierda - derecha
    elif nodo.valor == '*':
        return izquierda * derecha
    elif nodo.valor == '/':
        return izquierda / derecha

# Prueba con la expresión "5 + 3 * 4"
expresion = "5+3*4"
arbol = construir_arbol(expresion)
resultado = evaluar_arbol(arbol)
print(f"El resultado de la expresión '{expresion}' es: {resultado}")

