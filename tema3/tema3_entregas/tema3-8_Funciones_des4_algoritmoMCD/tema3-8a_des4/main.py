'''
Desafío 4: Algoritmo MCD
El Máximo Común Divisor (MCD) es un concepto matemático que ha sido estudiado desde tiempos antiguos. Atribuido a Euclides, el algoritmo para determinarlo es elegante y eficiente. Tu tarea es implementar una función que calcule el MCD de dos números utilizando el algoritmo de Euclides.

#Autor: Eliana Dalfolo
'''
# Limpia la pantalla
from os import system
system("clear")  # Linux - OSX


# Función que calcula el MCD de dos números
def mcd_euclides_resta(a, b): # a > b
  # Asegura que a y b sean positivos
  a, b = abs(a), abs(b)

  # Usa el algoritmo de resta
  while a != b: # Mientras a y b sean diferentes
    if a > b:
      a -= b # a = a - b
    else:
      b -= a # b = b - a
  return a

# Función principal
def main():
    while True: 
        try:
            print("\n ------------- CALCULAR EL MCD --------------\n")
            numero1 = int(input("Introduce el primer número entero: "))
            print(f"\nEl número introducido es {numero1}.")
            break  # Salir del bucle si la entrada es válida
        except ValueError:
            print("\nNo has introducido un número entero válido. Vuelve a intentarlo.")

    while True:
        try:
            numero2 = int(input("\nIntroduce el segundo número entero: "))
            print(f"\nEl número introducido es {numero2}.")
            break  # Salir del bucle si la entrada es válida
        except ValueError:
            print("\nNo has introducido un número entero válido. Vuelve a intentarlo.")

    # Calcular el MCD
    # Asigna el resultado de la función a la variable resultado
    resultado = mcd_euclides_resta(numero1, numero2) 
    print("\n ------------- RESULTADO --------------")
    print(f"\nEl MCD de {numero1} y {numero2} es {resultado}.") 

main()
