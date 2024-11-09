# 5_14_Excepciones
# Número de desafío: 4
# Consigna: Crea una excepción personalizada llamada NegativeNumberError que se dispare si el usuario intenta ingresar un número negativo en un programa de cálculo de raíces cuadradas. Implementa el manejo de esta excepción en el programa.
# Autora: Eliana D

import math

class NegativeNumberError(Exception):
    """Excepción personalizada para números negativos."""
    def __init__(self, mensaje="Error: No se puede calcular la raíz cuadrada de un número negativo."):
        super().__init__(mensaje)

def calcular_raiz_cuadrada():
    try:
        # Solicitar al usuario un número
        numero = float(input("Ingresa un número para calcular su raíz cuadrada: "))
        
        # Verificar si el número es negativo y lanzar la excepción personalizada
        if numero < 0:
            raise NegativeNumberError()
        
        # Calcular la raíz cuadrada si el número es válido
        resultado = math.sqrt(numero)
        print(f"La raíz cuadrada de {numero} es: {resultado}")
    
    except ValueError:
        print("Error: Debes ingresar un número válido.")
    except NegativeNumberError as nne:
        print(nne)
    except Exception as e:
        print(f"Error inesperado: {e}")
    finally:
        print("Programa finalizado.")

# Ejecutar la función
calcular_raiz_cuadrada()









