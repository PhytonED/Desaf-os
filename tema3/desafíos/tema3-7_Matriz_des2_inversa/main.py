# Desafío 2
# Dada la matriz $ A = \begin{bmatrix} 1 & 0 & 1 \\ 4 & -1 & 4 \\ 5 & 6 & 7 \end{bmatrix} $, encuentra la traza de la matriz inversa de $ A $.
# Autor: Eliana Dalfolo

'''
Usaré el submódulo linalg unciones para realizar operaciones de álgebra lineal como cálculo de determinantes, inversión de matrices, descomposiciones y resolución de sistemas de ecuaciones.
- Determinante (np.linalg.det(A)): 
El determinante de una matriz cuadrada A debe ser distinto de cero para que la matriz sea invertible. 
Si el determinante es cero, la matriz no tiene inversa.
- Inversa (np.linalg.inv(A)): 
La matriz inversa Aˆ-1 es la que al multiplicarse por la matriz original 
A, produce la matriz identidad. 
Esta propiedad solo es posible cuando el determinante de A es distinto de cero.
- Traza (np.trace(A_inv)): 
Es la suma de los elementos en la diagonal principal de la matriz y en este caso, se calcula sobre la inversa de A
'''

import numpy as np  # Importamos la biblioteca numpy para manejar operaciones de matrices

# Solicitar el número de filas de la matriz (debe ser igual al número de columnas para ser cuadrada)
filas = int(input("Ingrese el número de filas de la matriz (debe ser igual al número de columnas para ser cuadrada): "))
# Solicitar el número de columnas de la matriz
columnas = int(input("Ingrese el número de columnas de la matriz: "))

# Verificar si la matriz es cuadrada
if filas != columnas:
    # Si no es cuadrada, mostramos un mensaje de error porque no tiene inversa
    print("Error: La matriz debe ser cuadrada para poder calcular su inversa y su traza.")
else:
    # Si la matriz es cuadrada, continuamos con la creación de la matriz

    matriz = []  # Inicializar una lista vacía para almacenar la matriz

    # Iniciar un bucle para pedir los elementos de cada fila
    print("Ingrese los elementos de la matriz, fila por fila:")
    for i in range(filas):
        fila = []  # Inicializa una lista para la fila actual
        # Iniciar un bucle para pedir cada elemento de la fila
        for j in range(columnas):
            # Solicitar al usuario el valor de cada elemento de la matriz en la posición específica (i, j)
            valor = float(input(f"Ingrese el valor del elemento en la posición ({i+1}, {j+1}): "))
            fila.append(valor)  # Agregar el valor a la fila actual
        matriz.append(fila)  # Agregar la fila completa a la matriz

    # Convertimos la matriz ingresada (lista de listas) a un arreglo de numpy para realizar cálculos
    A = np.array(matriz)

    # Calcular el determinante de la matriz para verificar si es invertible
    determinante_A = np.linalg.det(A)
    # Matemáticamente, una matriz solo es invertible si su determinante no es cero

    # Verificar si el determinante es cero
    if determinante_A == 0:
        # Si el determinante es cero, no se puede calcular la inversa, entonces mostramos un mensaje
        print("La matriz no es invertible, por lo tanto no se puede calcular la traza de su inversa.")
    else:
        # Si el determinante no es cero, podemos calcular la inversa de la matriz

        A_inv = np.linalg.inv(A)  # Calcular la matriz inversa de A usando numpy
        # Matemáticamente, la inversa de una matriz A es otra matriz A⁻¹ tal que A * A⁻¹ = I (matriz identidad)

        traza_A_inv = np.trace(A_inv)  # Calcular la traza de la matriz inversa (suma de la diagonal principal)
        # Matemáticamente, la traza de una matriz es la suma de los elementos en su diagonal principal

        # Mostrar los resultados
        print("\nLa matriz A ingresada es:")
        print(A)  # Mostrar la matriz original A

        print("\nLa matriz inversa de A es:")
        print(A_inv)  # Mostrar la matriz inversa de A

        print("\nLa traza de la matriz inversa de A es:")
        print(traza_A_inv)  # Mostrar la traza de la matriz inversa de A
