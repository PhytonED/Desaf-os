# 5_15_Arboles
# Número de desafío: 4
# Consigna: Dado un conjunto de números enteros únicos, construye un árbol de búsqueda binaria (ABB) que inserte los valores de manera que el subárbol izquierdo de cada nodo contenga solo nodos con valores menores, y el subárbol derecho solo nodos con valores mayores. Una vez construido el árbol, implementa una función para buscar un número dado y devuelva si ese número existe en el árbol o no.
# Autora: Eliana D

# Definición de la clase Nodo para el árbol de búsqueda binaria
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

# Función para insertar un valor en el ABB
def insertar(nodo, valor):
    if nodo is None:
        return Nodo(valor)
    
    # Insertar en el subárbol izquierdo si el valor es menor
    if valor < nodo.valor:
        nodo.izquierdo = insertar(nodo.izquierdo, valor)
    # Insertar en el subárbol derecho si el valor es mayor
    elif valor > nodo.valor:
        nodo.derecho = insertar(nodo.derecho, valor)
    
    return nodo

# Función para buscar un valor en el ABB
def buscar(nodo, valor):
    # Si el nodo es None, el valor no está en el árbol
    if nodo is None:
        return False
    
    # Si el valor se encuentra en el nodo actual
    if nodo.valor == valor:
        return True
    # Buscar en el subárbol izquierdo si el valor es menor
    elif valor < nodo.valor:
        return buscar(nodo.izquierdo, valor)
    # Buscar en el subárbol derecho si el valor es mayor
    else:
        return buscar(nodo.derecho, valor)

# Función para construir un ABB a partir de una lista de números
def construir_arbol(lista):
    raiz = None
    for valor in lista:
        raiz = insertar(raiz, valor)
    return raiz

# Lista de números enteros únicos
numeros = [15, 10, 20, 8, 12, 17, 25]

# Construcción del árbol de búsqueda binaria
arbol = construir_arbol(numeros)

# Búsqueda de un número en el ABB
numero_a_buscar = 17
encontrado = buscar(arbol, numero_a_buscar)

# Mostrar si el número fue encontrado
if encontrado:
    print(f"El número {numero_a_buscar} está en el árbol.")
else:
    print(f"El número {numero_a_buscar} no está en el árbol.")

