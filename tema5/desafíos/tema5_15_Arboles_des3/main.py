# 5_15_Arboles
# Número de desafío: 3
# Consigna: Construye un árbol binario en el que cada nodo contiene un número entero. Implementa una función que recorra el árbol en postorden y devuelva el valor máximo encontrado entre todos los nodos del árbol.
# Autora: Eliana D

# Definición de la clase Nodo para el árbol binario
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

# Función para recorrer el árbol en postorden y encontrar el valor máximo
def maximo_postorden(nodo):
    if nodo is None:
        return float('-inf')  # Retornamos un valor muy bajo si el nodo es None

    # Recorrer en postorden: subárbol izquierdo, subárbol derecho, nodo actual
    max_izquierdo = maximo_postorden(nodo.izquierdo)
    max_derecho = maximo_postorden(nodo.derecho)

    # Retornar el valor máximo entre el nodo actual y los máximos de sus hijos
    return max(nodo.valor, max_izquierdo, max_derecho)

# Construcción de un árbol binario con algunos nodos
# Nivel 1 (raíz)
raiz = Nodo(1)

# Nivel 2
raiz.izquierdo = Nodo(12)
raiz.derecho = Nodo(7)

# Nivel 3
raiz.izquierdo.izquierdo = Nodo(4)
raiz.izquierdo.derecho = Nodo(5)
raiz.derecho.izquierdo = Nodo(6)
raiz.derecho.derecho = Nodo(17)

# Nivel 4 (agregando nodos adicionales)
raiz.izquierdo.izquierdo.izquierdo = Nodo(9)
raiz.izquierdo.izquierdo.derecho = Nodo(3)
raiz.derecho.derecho.izquierdo = Nodo(20)

# Encontrar el valor máximo en el árbol usando un recorrido en postorden
valor_maximo = maximo_postorden(raiz)
print("El valor máximo en el árbol es:", valor_maximo)





















































