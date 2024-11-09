# tema5_16_Algoritmos_fundamentales
# Número de desafío: 2
# Consigna:
'''
Tienes una tabla de calificaciones representada como una matriz,
donde cada fila contiene las calificaciones de un estudiante en distintas materias. 
Implementa una función que busque una calificación específica en toda la matriz y 
devuelva el estudiante y la materia en la que se encuentra.
'''
# Autora: Eliana D

def buscar_calificacion(matriz, calificacion_buscada):
    """Busca una calificación específica en la matriz de calificaciones y devuelve el estudiante y la materia donde se encuentra."""
    for i, fila in enumerate(matriz):
        for j, calificacion in enumerate(fila):
            if calificacion == calificacion_buscada:
                return i, j  # Retorna el índice del estudiante (i) y el índice de la materia (j)
    return None  # Si no se encuentra la calificación

def main():
    # Ejemplo de matriz de calificaciones (estudiantes x materias)
    # Cada fila representa las calificaciones de un estudiante en distintas materias
    calificaciones = [
        [85, 90, 78],  # Estudiante 1: Matemáticas, Física, Química
        [92, 88, 95],  # Estudiante 2: Matemáticas, Física, Química
        [76, 84, 89],  # Estudiante 3: Matemáticas, Física, Química
    ]
    
    # Calificación a buscar
    calificacion_buscada = 95
    
    # Llamar a la función de búsqueda
    resultado = buscar_calificacion(calificaciones, calificacion_buscada)
    
    if resultado:
        estudiante, materia = resultado
        print(f"La calificación {calificacion_buscada} se encuentra en el estudiante {estudiante + 1} en la materia {materia + 1}.")
    else:
        print(f"La calificación {calificacion_buscada} no se encuentra en la matriz de calificaciones.")

# Ejecutar el programa
main()
