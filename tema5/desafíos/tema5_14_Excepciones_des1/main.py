# 5_14_Excepciones
# Número de desafío: 1
# Consigna: Solicita al usuario dos números enteros e implementa un try-except que maneje la división por cero y los valores no numéricos. Muestra mensajes de error apropiados en cada caso.
# Autora: Eliana D
'''
El bloque try intenta realizar la operación de división, y si ocurre algún error, el bloque except maneja las excepciones específicas (como valores no numéricos o división por cero).
Se usa ValueError para manejar entradas no numéricas y ZeroDivisionError para manejar la división por cero.
'''

def dividir_numeros():
    try:
        # Solicitar al usuario que ingrese dos números
        """
    Este programa solicita al usuario dos números enteros e intenta realizar una 
    división. Maneja las excepciones de entrada no numérica, división por cero y 
    otros errores generales.
    """
    try:
        # Solicita el primer número y lo convierte a entero
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        
        # Intenta realizar la división
        resultado = num1 / num2
        print(f"El resultado de la división es: {resultado}")
    
    except ValueError:
        # Captura el error cuando el usuario no ingresa un valor numérico
        print("Error: Por favor ingrese valores numéricos enteros.")
    
    except ZeroDivisionError:
        # Captura el error cuando el divisor es cero
        print("Error: No se puede dividir por cero.")
    
    except Exception as e:
        # Captura cualquier otro tipo de error no previsto
        print(f"Se ha producido un error inesperado: {e}")

# Llamada a la función para ejecutar el desafío
dividir_numeros()
















