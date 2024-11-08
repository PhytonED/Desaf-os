'''
Desafío 6: Verificación y Cálculo de Números Primos
Crea dos funciones y un main que te permita trabajar con números primos, un concepto matemático fundamental. 
En este desafío, deberás:
1. Crear una función que verifique si un número es primo.
2. Crear otra función que cuente la cantidad de números primos dentro de una lista dada.
3. Implementar un main que integre estas funciones y muestre los resultados.
Asegúrate de que tu código esté bien documentado y que las funciones sean reutilizables.

#Autor: Eliana Dalfolo
'''
'''
Anexo1:
abs(round(a)) asegura que:

- El número sea un entero: La función round(a) convierte cualquier número decimal en su entero más cercano, eliminando la parte fraccionaria. Se asegura el ingreso de números enteros positivos.

- El número sea positivo: La función abs(...) convierte cualquier número negativo en su equivalente positivo. Los primos solamente son números positivos pero por si ocurriera que se ingrese algún valor negarivo.
'''
'''
Anexo2
a/2: 
Calculo la mitad porque es el divisor más grande que puedo llegar a tener (sin el mismo número). Cualquiér número más grande me daría un valor menor a 2 (sin ser el 1 que ya son divisibles) o sea fraccionario.
'''
'''
Anexo3
if es_primo(un_numero) else 'no es primo': 
Condición en la cual si es_primo(un_numero) devuelve True, se usa 'es primo'; si devuelve False, se usa 'no es primo'. Esta parte del código elige entre dos cadenas de texto basándose en el resultado de la función es_primo.
'''

# Limpia la pantalla
from os import system
system("clear")  # Linux - OSX

# Función que verifica si un número es primo
def es_primo(a): 
    # Nos aseguramos de tener un número natural
    a = abs(round(a)) # Redondeamos a entero y positivos. Anexo1
    divisor = round(a/2) # Anexo2
    # Calculamos los divisores de a/2 hasta 2 porque todos los números son divisibles entre 1 y a es divisible entre sí.
    while divisor > 1: # Mientras el divisor sea mayor que 1
        if a % divisor == 0: # Si el resto de la división es 0
            return False
        divisor -= 1 # Restar 1 al divisor
    return True

# Cuenta los primos de una lista
def cuenta_primos(lista): # Recibe una lista
    cuenta = 0 # Inicializamos la cuenta en 0
    for num in lista: # Recorremos la lista
        if es_primo(num):
            cuenta += 1 # Si es primo, sumamos 1 a la cuenta
    return cuenta

# Función principal
def main():
    while True:  # Cuando se introduce una entrada válida, se sigue hasta que se ingresen datos válidos.
        try: 
            print("\n ------------- ¿ES O NO PRIMO? --------------\n")
            un_numero = int(input("Introduce un número entero: "))
            print(f"\nEl número {un_numero} {'es primo' if es_primo(un_numero) else 'no es primo'}.")
            break  # Salir del bucle si la entrada es válida

        except ValueError:
            print("\nNo has introducido un número entero válido. Vuelve a intentarlo.")

    while True:
        try:
            print("\n ------------- ¿CUÁNTOS SON O NO PRIMOS? --------------\n")
            entrada = input("\nIntroduce una lista de números naturales separados por espacios: ")
            numeros = [int(numero) for numero in entrada.split()]
            print(f"\nHay {cuenta_primos(numeros)} números primos en la lista.")
            break  # Salir del bucle si la entrada es válida

        except ValueError:
            print("\n Has introducido valores incorrectos o no separados por espacios. Vuelve a intentarlo.")

# Ejecutar la función principal
main()
