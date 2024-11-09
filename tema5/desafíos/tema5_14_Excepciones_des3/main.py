# 5_14_Excepciones
# Número de desafío: 3
# Consigna: Escribe una función que calcule el factorial de un número entero positivo. 
# Maneja las excepciones si el número ingresado es negativo, no es entero, o es demasiado grande para ser procesado.
# Autora: Eliana D

import math

def calcular_factorial():
    """Solicita al usuario un número entero y calcula su factorial."""
    try:
        # Solicitar un número entero al usuario
        numero = int(input("Ingresa un número entero positivo: "))
        
        # Validar que el número sea no negativo
        if numero < 0:
            raise ValueError("Error: El número no puede ser negativo.")
        
        # Calcular el factorial usando math.factorial
        resultado = math.factorial(numero)
        print(f"El factorial de {numero} es: {resultado}")
    
    except ValueError as ve:
        print(ve)
    except OverflowError:
        print("Error: El número es demasiado grande para calcular su factorial.")
    except Exception as e:
        print(f"Error inesperado: {e}")
    finally:
        print("Programa finalizado.")

# Ejecutar la función
calcular_factorial()











