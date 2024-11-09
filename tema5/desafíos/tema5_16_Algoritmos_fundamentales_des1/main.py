# tema5_16_Algoritmos_fundamentales
# Número de desafío: 1
# Consigna:
'''
Dado un árbol que representa los grupos de estudiantes en una escuela, 
implementa un recorrido por niveles para mostrar los estudiantes de cada grupo, 
comenzando por el nivel más alto (ej. grado 12) y 
descendiendo hasta el nivel más bajo (ej. grado 1). 
Cada nodo del árbol representa un grado y sus estudiantes.
'''
# Autora: Eliana D

from collections import deque

class NodoGrado:
    def __init__(self, grado, estudiantes):
        self.grado = grado
        self.estudiantes = estudiantes
        self.hijos = []

    def agregar_hijo(self, nodo_hijo):
        self.hijos.append(nodo_hijo)

def recorrido_por_niveles(raiz):
    """Recorrido por niveles para mostrar los estudiantes de cada grado."""
    if not raiz:
        return
    
    # Utilizar una cola para el recorrido por niveles
    cola = deque([raiz])
    
    while cola:
        # Extraer el nodo actual de la cola
        nodo_actual = cola.popleft()
        
        # Mostrar el grado y sus estudiantes
        print(f"Grado {nodo_actual.grado}: {nodo_actual.estudiantes}")
        
        # Agregar los hijos del nodo actual a la cola
        for hijo in nodo_actual.hijos:
            cola.append(hijo)

# Crear el árbol de grados y estudiantes
grado12 = NodoGrado(12, ["Ana", "Luis", "María"])
grado11 = NodoGrado(11, ["Carlos", "Elena"])
grado10 = NodoGrado(10, ["Jorge", "Patricia", "Marta"])
grado9 = NodoGrado(9, ["Raúl", "Fernanda"])

# Construir la jerarquía del árbol
grado12.agregar_hijo(grado11)
grado11.agregar_hijo(grado10)
grado10.agregar_hijo(grado9)

# Realizar el recorrido por niveles
print("Recorrido por niveles:")
recorrido_por_niveles(grado12)

