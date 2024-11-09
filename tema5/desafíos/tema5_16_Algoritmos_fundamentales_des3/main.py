# tema5_16_Algoritmos_fundamentales
# Número de desafío: 3
# Consigna:
'''
Tienes una lista ordenada alfabéticamente con los nombres de los estudiantes de una clase. 
Implementa una función que realice una búsqueda binaria para encontrar un estudiante específico
en la lista. Si el estudiante no está, la función debe mostrar un mensaje adecuado.
'''
# Autora: Eliana D

def busqueda_binaria(lista, estudiante_buscado):
    """Realiza una búsqueda binaria para encontrar un estudiante en la lista ordenada alfabéticamente."""
    bajo = 0
    alto = len(lista) - 1
    
    while bajo <= alto:
        medio = (bajo + alto) // 2  # Calcula el índice medio
        if lista[medio] == estudiante_buscado:
            return medio  # Estudiante encontrado, devolver el índice
        elif lista[medio] < estudiante_buscado:
            bajo = medio + 1  # Buscar en la mitad superior
        else:
            alto = medio - 1  # Buscar en la mitad inferior
    
    return -1  # Si no se encuentra el estudiante

def main():
    # Lista ordenada alfabéticamente con los nombres de los estudiantes
    estudiantes = ["Ana", "Carlos", "Elena", "Jorge", "Luis", "Marta", "Patricia", "Raúl"]
    
    # Estudiante que queremos buscar
    estudiante_buscado = "Marta"
    
    # Llamar a la función de búsqueda binaria
    resultado = busqueda_binaria(estudiantes, estudiante_buscado)
    
    if resultado != -1:
        print(f"El estudiante '{estudiante_buscado}' se encuentra en el índice {resultado}.")
    else:
        print(f"El estudiante '{estudiante_buscado}' no se encuentra en la lista.")

# Ejecutar el programa
main()

