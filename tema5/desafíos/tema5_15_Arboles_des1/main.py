# 5_15_Arboles
# Número de desafío: 1
# Consigna: 
# Construye un árbol binario simple con al menos 3 niveles de profundidad. Cada nodo debe contener un número entero como valor. Una vez construido el árbol, implementa una función que imprima los valores de los nodos siguiendo un recorrido en preorden.
# Autora: Eliana D

# Definición de la clase Nodo para el árbol binario
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

# Función para realizar un recorrido en preorden
def preorden(nodo):
    if nodo:
        # Imprimir el valor del nodo actual
        print(nodo.valor, end=' ')
        # Recorrer el subárbol izquierdo
        preorden(nodo.izquierdo)
        # Recorrer el subárbol derecho
        preorden(nodo.derecho)

# Construcción de un árbol binario con al menos 3 niveles
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

# Nivel 4 (agregando nodos adicionales para mayor profundidad)
raiz.izquierdo.izquierdo.izquierdo = Nodo(8)
raiz.izquierdo.izquierdo.derecho = Nodo(9)
raiz.derecho.derecho.izquierdo = Nodo(10)

# Imprimir el recorrido en preorden
print("Recorrido en preorden:")
preorden(raiz)





































