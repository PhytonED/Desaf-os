# 5_15_Arboles
# Número de desafío: 2
# Consigna: Dado un árbol binario con números enteros en cada nodo, implementa una función que recorra el árbol en orden y calcule la suma de todos los valores almacenados en los nodos. El programa debe devolver el resultado final de la suma.
# Autora: Eliana D

# Definición de la clase Nodo para el árbol binario
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

# Función para recorrer el árbol en orden y calcular la suma de todos los nodos
def sumar_valores_inorden(nodo):
    if nodo is None:
        return 0

    # Calcular la suma de los nodos usando recorrido inorden
    suma_izquierda = sumar_valores_inorden(nodo.izquierdo)
    suma_derecha = sumar_valores_inorden(nodo.derecho)
    suma_total = suma_izquierda + nodo.valor + suma_derecha

    return suma_total

# Construcción de un árbol binario con algunos nodos
# Nivel 1 (raíz)
raiz = Nodo(1)

# Nivel 2
raiz.izquierdo = Nodo(2)
raiz.derecho = Nodo(3)

# Nivel 3
raiz.izquierdo.izquierdo = Nodo(4)
raiz.izquierdo.derecho = Nodo(5)
raiz.derecho.izquierdo = Nodo(6)
raiz.derecho.derecho = Nodo(7)

# Nivel 4 (agregando nodos adicionales)
raiz.izquierdo.izquierdo.izquierdo = Nodo(8)
raiz.izquierdo.izquierdo.derecho = Nodo(9)
raiz.derecho.derecho.izquierdo = Nodo(10)

# Calcular la suma de todos los valores en el árbol
suma_total = sumar_valores_inorden(raiz)
print("La suma de todos los valores en el árbol es:", suma_total)





































