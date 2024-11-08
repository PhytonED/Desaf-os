# Tema 3 - Desafío 3: Caracteres ASCII
# Objetivo: Mostrar los caracteres ASCII correspondientes a una lista de números.
# Autor: Eliana Dalfolo
    
"""
Se pide al usuario que ingrese los números que desea convertir
Rango ASCII: Se verifica si el número está entre 0 y 127 antes de hacer la conversión.
Mensaje de error: Si el número está fuera de este rango, se muestra mensaje diciendo que el número no tiene un carácter ASCII válido.

"""

# Importamos la biblioteca array para crear el arreglo de números
from array import array

# Creamos el arreglo vacío para almacenar los números ingresados
numeros = array('i')

# Solicitamos al usuario que ingrese la cantidad de números que desea convertir
cantidad = int(input("\n¿Cuántos números deseas ingresar para convertir a caracteres ASCII? "))

# Pedimos al usuario que ingrese cada número y lo añadimos al arreglo
for i in range(cantidad):
    numero = int(input(f"\nIngrese el número {i+1}: "))
    numeros.append(numero)  # Agregamos el número al arreglo

# Recorremos el arreglo y convertimos cada número a su correspondiente carácter ASCII si es válido
print("\nConversión de números a caracteres ASCII:")
for numero in numeros:
    if 0 <= numero <= 127:  # Verificamos si el número está en el rango ASCII estándar
        print(f"\nEl número {numero} corresponde al carácter ASCII: {chr(numero)}")
    else:
        print(f"\nEl número {numero} no tiene un carácter ASCII válido.")













