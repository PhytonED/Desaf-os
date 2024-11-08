# Tema 2 - Desafío 1: Clasificar Números
# Objetivo: Dado tres números distintos, clasificarlos en orden ascendente utilizando comparaciones encadenadas.
# #Autor: Eliana Dalfolo

# Solicitar el primer número y asegurarse de que sea válido
while True:
    entrada1 = input("Ingresa el primer número: ")
    try:
        num1 = float(entrada1)
        break
    except ValueError:
        print("Por favor, ingresa un número válido.")

# Solicitar el segundo número y asegurarse de que sea válido
while True:
    entrada2 = input("Ingresa el segundo número: ")
    try:
        num2 = float(entrada2)
        break
    except ValueError:
        print("Por favor, ingresa un número válido.")

# Solicitar el tercer número y asegurarse de que sea válido
while True:
    entrada3 = input("Ingresa el tercer número: ")
    try:
        num3 = float(entrada3)
        break
    except ValueError:
        print("Por favor, ingresa un número válido.")

# Comparaciones encadenadas para ordenar en forma ascendente
if num1 <= num2 <= num3:
    orden = (num1, num2, num3)
elif num1 <= num3 <= num2:
    orden = (num1, num3, num2)
elif num2 <= num1 <= num3:
    orden = (num2, num1, num3)
elif num2 <= num3 <= num1:
    orden = (num2, num3, num1)
elif num3 <= num1 <= num2:
    orden = (num3, num1, num2)
else:
    orden = (num3, num2, num1)

# Mostrar el resultado
print("Los números en orden ascendente son:", orden)


















