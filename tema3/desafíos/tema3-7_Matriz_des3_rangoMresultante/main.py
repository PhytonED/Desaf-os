# Desafío 3
# Dada la matriz A = [1  2  3 
#                     4  5  6 
#                     7  8  9]
#encuentra el rango de la matriz resultante de (A + A^T).
# Autor: Eliana Dalfolo
'''
Solicito que el usuario
- indique dimensiones de la matriz
- ingrese los valores 
de esta forma se puede usar de forma genérica y no solamnete para los valores planteados.
'''
import numpy as np  # Importamos la biblioteca numpy para operaciones con matrices.

# Solicitamos al usuario las dimensiones de la matriz.
filas = int(input("Ingrese el número de filas de la matriz A: "))
columnas = int(input("Ingrese el número de columnas de la matriz A: "))

# Inicializamos una lista vacía para almacenar los valores de la matriz.
valores = []

# Pedimos al usuario que ingrese cada valor de la matriz A.
print("Ingrese los valores de la matriz A, fila por fila:")
for i in range(filas):
    fila = []
    for j in range(columnas):
        valor = int(input(f"Ingrese el valor para A[{i+1}][{j+1}]: "))
        fila.append(valor)  # Añadimos el valor a la fila actual.
    valores.append(fila)  # Añadimos la fila completa a la matriz.

# Convertimos la lista de listas en un arreglo de numpy para facilitar operaciones matriciales.
A = np.array(valores)

# Mostramos la matriz A ingresada por el usuario.
print("\nLa matriz A ingresada es:")
print(A)

# Calculamos la transpuesta de A, denotada como A^T.
# Matemáticamente, la transposición intercambia filas por columnas.
A_T = np.transpose(A)

# Sumamos A y su transpuesta A^T para obtener la matriz resultante.
# Matemáticamente, (A + A^T) es una matriz simétrica cuando A es cuadrada.
resultante = A + A_T

# Calculamos el rango de la matriz resultante usando la función np.linalg.matrix_rank.
# El rango representa el número de filas o columnas linealmente independientes.
rango = np.linalg.matrix_rank(resultante)

# Mostramos la matriz resultante y su rango en pantalla.
print("\nLa matriz resultante de (A + A^T) es:")
print(resultante)
print("\nEl rango de la matriz resultante es:", rango)
