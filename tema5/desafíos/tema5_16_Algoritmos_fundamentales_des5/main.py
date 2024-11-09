# tema5_16_Algoritmos_fundamentales
# Número de desafío: 5
# Consigna:
'''
Dado un conjunto de estudiantes y sus promedios, implementa una función que cree un árbol binario de búsqueda en el que los nodos representan los promedios de los estudiantes.
Luego, implementa una función que recorra el árbol en orden para mostrar los estudiantes en orden ascendente de rendimiento académico.
'''
# Autora: Eliana D
class Nodo:
    def __init__(self, promedio, estudiante):
        self.promedio = promedio
        self.estudiante = estudiante
        self.izquierdo = None
        self.derecho = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, promedio, estudiante):
        """Inserta un nuevo nodo en el árbol binario de búsqueda."""
        if self.raiz is None:
            self.raiz = Nodo(promedio, estudiante)
        else:
            self._insertar_recursivo(self.raiz, promedio, estudiante)

    def _insertar_recursivo(self, nodo, promedio, estudiante):
        """Inserta recursivamente un nodo en el lugar adecuado del árbol."""
        if promedio < nodo.promedio:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(promedio, estudiante)
            else:
                self._insertar_recursivo(nodo.izquierdo, promedio, estudiante)
        else:
            if nodo.derecho is None:
                nodo.derecho = Nodo(promedio, estudiante)
            else:
                self._insertar_recursivo(nodo.derecho, promedio, estudiante)

    def recorrido_en_orden(self):
        """Realiza un recorrido en orden (in-order) y devuelve una lista de estudiantes ordenados."""
        estudiantes_ordenados = []
        self._recorrido_en_orden_recursivo(self.raiz, estudiantes_ordenados)
        return estudiantes_ordenados

    def _recorrido_en_orden_recursivo(self, nodo, estudiantes_ordenados):
        """Recorrido en orden recursivo."""
        if nodo:
            self._recorrido_en_orden_recursivo(nodo.izquierdo, estudiantes_ordenados)
            estudiantes_ordenados.append((nodo.estudiante, nodo.promedio))
            self._recorrido_en_orden_recursivo(nodo.derecho, estudiantes_ordenados)

def main():
    # Lista de estudiantes y sus promedios
    estudiantes = [
        ("Ana", 85.4),
        ("Carlos", 90.2),
        ("Elena", 88.0),
        ("Jorge", 76.5),
        ("Luis", 92.1),
        ("Marta", 95.3)
    ]

    # Crear el árbol binario de búsqueda
    arbol = ArbolBinarioBusqueda()

    # Insertar los estudiantes en el árbol
    for estudiante, promedio in estudiantes:
        arbol.insertar(promedio, estudiante)

    # Obtener el listado de estudiantes ordenados por su promedio
    estudiantes_ordenados = arbol.recorrido_en_orden()

    # Imprimir los estudiantes ordenados por promedio
    print("Estudiantes ordenados por rendimiento académico (de menor a mayor):")
    for estudiante, promedio in estudiantes_ordenados:
        print(f"{estudiante}: {promedio}")

# Ejecutar el programa
main()
