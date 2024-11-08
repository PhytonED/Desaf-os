"""Objetivo: 
Desafío 2: Calculadora Simple
Escriba un programa que pida al usuario que ingrese dos números y luego imprima la suma, la resta, la multiplicación y la división de esos números.

Autor: Eliana Dalfolo"""

"""Se solicita al usuario que ingrese dos valores numéricos.
- La función input() permite que el usuario ingrese los valores solicitados desde la consola.
- \n permite hacer salto de línea.
- Los valores ingresados por el usuario se almacenan en las variables:
  * valor1: Almacena el primer valor ingresado por el usuario.
  * valor2: Almacena el segundo valor ingresado por el usuario.
- Con los valores ingresados se realizarán operaciones matemáticas y sus resultados se almacenarán en las siguientes variables:
  * suma
  * resta
  * multiplicacion
  * division
- Se imprimirán los resultados en la consola utilizando la función print() y función f-string (f"").
  - {} 
  -- si usamos la función f-strings, sirven para colocar en su interior la variable."""

# Explica de qué trata el programa.
print("***** CALCULADORA SIMPLE *****\n")
print("Este programa solicita al usuario que ingrese dos valores numéricos para realizar la suma, resta, multiplicación y división de los mismos y mostrar los resultados obtenidos.\n")

# Solicito al usuario que ingrese el 1er. número
num1 = input("\nIngrese el primer número: ")
# Solicito al usuario que ingrese el 2do. número
num2 = input("\nIngrese el segundo número: ")

'''Los números introducidos son de tipo string, por lo que se debe convertir a tipo int o float. Dado que es una calculadora, uso float'''

# Realizo las operaciones matemáticas.
print("\n*******************************************")  
print("\nLas operaciones realizadas y sus resultados")
print("\n*******************************************")  
# Variables Operaciones:
# ---- SUMA ----
suma = float(num1) + float(num2)
print(f"\nSuma: {suma}")
# ---- RESTA ----
resta = float(num1) - float(num2)
print(f"\nResta: {resta}")
# ---- MULTIPLICACIÓN ----
multiplicacion = float(num1) * float(num2)
print(f"\nMultiplicación: {multiplicacion}")
# ---- DIVISIÓN ----
if num2 == "0":
  print("\nDivisión: No se puede dividir por cero.")
else: 
  division = float(num1) / float(num2)
  print(f"\nDivisión: {division}\n")
