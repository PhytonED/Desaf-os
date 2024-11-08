# Desafío 1
# Considere las matrices $ A $ y $ B $ definidas como:
# La matriz resultante de la operación (2A + B^T) es:
# Autor: Eliana Dalfolo

'''
A = [ 1 2]  
    [ 3 4]
B = [ 5 6]
    [ 7 8]
Tu tarea es calcular la matriz resultante de la operación (2A + B^T) 
Recuerda que B^T denota la transposición de la matriz B.
'''
import numpy as np  # Importamos la librería numpy para trabajar con matrices

# Solicitar las dimensiones de las matrices A y B
'''
Le pedimos al usuario que ingrese el número de filas (m) y columnas (n) de las matrices A y B.
Para la transposición el número de columnas de A y debe ser coincida con el número de filas de B, 
ya que B.T convierte las filas en columnas.
'''
fila = int(input("¿Cuántas filas tendrá la matriz? "))  # Definir el número de filas
columna = int(input("¿Cuántas columnas tendrá la matriz? "))  # Definir el número de columnas

# Inicializar las matrices A y B con ceros
A = np.zeros((fila, columna), dtype=int)  # Matriz A de tamaño (filas, columnas), llena de ceros
B = np.zeros((fila, columna), dtype=int)  # Matriz B de tamaño (filas, columnas), llena de ceros

# Llenar la matriz A con valores proporcionados por el usuario
print("Introduce los valores para la matriz A:")
for i in range(fila):  # Recorremos las filas de la matriz A
    for j in range(columna):  # Recorremos las columnas de la matriz A
        A[i][j] = int(input(f"Ingrese el valor para A[{i+1},{j+1}]: "))  # Solicitar los valores de la matriz A

# Llenar la matriz B con valores proporcionados por el usuario
print("Introduce los valores para la matriz B:")
for i in range(fila):  # Recorremos las filas de la matriz B
    for j in range(columna):  # Recorremos las columnas de la matriz B
        B[i][j] = int(input(f"Ingrese el valor para B[{i+1},{j+1}]: "))  # Solicitar los valores de la matriz B

# Transponer la matriz B
'''
Realizamos la transposición de la matriz B. 
Las filas de B se convierten en columnas en la nueva matriz B_T.
'''
B_T = B.T  # B.T es la transposición de B, es decir, cambiamos filas por columnas

# Multiplicar la matriz A por 2
'''
Multiplicamos cada elemento de la matriz A por 2. 
'''
dos_A = 2 * A  # Esto genera una nueva matriz donde cada valor de A es multiplicado por 2

# Calcular la matriz resultante de la operación 2A + B^T
'''
Suma de las matrices 2A y B_T elemento por elemento. 
Podemos hacerlo porque ambas matrices tienen las mismas dimensiones.
'''
resultante = dos_A + B_T  # Realizamos la suma de 2A y B_T

# Mostrar el resultado
print("\nLa matriz A es:")
print(A)  # Imprimir la matriz A

print("\nLa matriz B es:")
print(B)  # Imprimir la matriz B

print("\nLa transposición de B (B^T) es:")
print(B_T)  # Imprimir la transposición de la matriz B

print("\nEl resultado de la operación 2A + B^T es:")
print(resultante)  # Mostrar el resultado final











