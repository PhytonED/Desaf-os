# 5_14_Excepciones
# Número de desafío: 1
# Consigna: Solicita al usuario dos números enteros e implementa un try-except que maneje la división por cero y los valores no numéricos. Muestra mensajes de error apropiados en cada caso.
# Autora: Eliana D

def dividir_numeros():
    try:
        # Solicitar al usuario que ingrese dos números
        numerador = int(input("Ingresa el numerador (número entero): "))
        denominador = int(input("Ingresa el denominador (número entero): "))
        
        # Intentar realizar la división
        resultado = numerador / denominador
    except ValueError:
        print("Error: Debes ingresar un número entero válido.")
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
    else:
        # Si no hubo excepciones, mostrar el resultado
        print(f"El resultado de {numerador} / {denominador} es: {resultado}")
    finally:
        print("Programa finalizado.")

# Ejecutar la función
dividir_numeros()
















