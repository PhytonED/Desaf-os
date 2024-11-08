"""Objetivo: 
Desafío 1: Saludo Personalizado
Escriba un programa que pida al usuario su nombre y su ciudad de origen, luego imprima un saludo personalizado con esa información.

Autor: Eliana Dalfolo
Se solicita al usuario que ingrese su nombre y ciudad de origen.
- La función input() permite que el usuario ingrese los valores solicitados desde la consola.
- \n permite hacer salto de línea.
- Los valores ingresados por el usuario se almacenan en las variables:
  * nombre: Almacena el primer valor ingresado por el usuario.
  * ciudad_o: Almacena el segundo valor ingresado por el usuario.
- Se imprimirán los resultados en la consola utilizando la función print() y función f-string (f"").
  - {} 
  -- si usamos la función f-strings, sirven para colocar en su interior la variable."""

# Explica de qué trata el programa.
print("***** SALUDO PERSONALIZADO *****\n")
print("Este programa solicita al usuario que ingrese su nombre y ciudad de origen para realizar un saludo personalizado.\n")

# Solicito al usuario que ingrese su nombre
nombre = input("\nIngrese su nombre: ")

# Solicito al usuario que ingrese su ciudad de origen
ciudad_o = input("\nIngrese su ciudad de origen: ")

# Se imprime en pantalla el saludo.
print("\n********************************************************")  
print(f"\nHola {nombre},\nes un placer contar con un usuario de {ciudad_o}.\nGracias por registrarte.")
print("\n********************************************************")