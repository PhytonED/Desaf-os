# tema5_16_Algoritmos_fundamentales
# Número de desafío: 4
# Consigna:
'''
Tienes una lista de estudiantes y su promedio de calificaciones. 
Implementa un algoritmo que ordene a los estudiantes de acuerdo con su
promedio utilizando el algoritmo de ordenamiento por selección. 
Al final, el estudiante con el promedio más alto debe estar en primer lugar.
'''
# Autora: Eliana D

def ordenamiento_por_seleccion(estudiantes):
    """Ordena a los estudiantes por su promedio de calificaciones en orden descendente utilizando el algoritmo de ordenamiento por selección."""
    n = len(estudiantes)
    
    # Recorremos la lista de estudiantes
    for i in range(n):
        # Encontrar el índice del estudiante con el promedio más alto en el subarreglo no ordenado
        max_indice = i
        for j in range(i + 1, n):
            if estudiantes[j][1] > estudiantes[max_indice][1]:  # Comparar los promedios
                max_indice = j
        
        # Intercambiar el estudiante con el promedio más alto con el estudiante en la posición i
        estudiantes[i], estudiantes[max_indice] = estudiantes[max_indice], estudiantes[i]
    
    return estudiantes

def main():
    # Lista de estudiantes con su nombre y su promedio de calificaciones
    estudiantes = [
        ("Ana", 85.4),
        ("Carlos", 90.2),
        ("Elena", 88.0),
        ("Jorge", 76.5),
        ("Luis", 92.1),
        ("Marta", 95.3)
    ]
    
    # Ordenar los estudiantes por su promedio utilizando el algoritmo de selección
    estudiantes_ordenados = ordenamiento_por_seleccion(estudiantes)
    
    # Imprimir los estudiantes ordenados por promedio
    print("Estudiantes ordenados por promedio (de mayor a menor):")
    for estudiante, promedio in estudiantes_ordenados:
        print(f"{estudiante}: {promedio}")

# Ejecutar el programa
main()
