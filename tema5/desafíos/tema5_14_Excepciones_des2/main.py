# 5_14_Excepciones
# Número de desafío: 2
# Consigna: Crea un programa que tome una lista de valores y realice operaciones matemáticas sobre ellos. 
# Implementa el manejo de varias excepciones comunes como ZeroDivisionError, TypeError, y ValueError.
# Autora: Eliana D

def obtener_lista():
    """Solicita al usuario una lista de números separados por comas."""
    try:
        entrada = input("Ingresa una lista de números separados por comas: ")
        # Convertir la entrada en una lista de números
        lista = [float(valor.strip()) for valor in entrada.split(",")]
        return lista
    except ValueError:
        raise ValueError("Error: Uno o más valores no son números válidos.")

def elegir_operacion():
    """Solicita al usuario que elija una operación matemática."""
    print("\nOperaciones disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    try:
        opcion = int(input("Elige una operación (1-4): "))
        if opcion not in [1, 2, 3, 4]:
            raise ValueError("Error: Opción no válida.")
        return opcion
    except ValueError:
        raise ValueError("Error: Debes ingresar un número entero entre 1 y 4.")

def realizar_operacion(lista, operacion):
    """Realiza la operación seleccionada en la lista de números."""
    try:
        if operacion == 1:  # Suma
            return sum(lista)
        elif operacion == 2:  # Resta (restar todos los elementos del primero)
            resultado = lista[0]
            for num in lista[1:]:
                resultado -= num
            return resultado
        elif operacion == 3:  # Multiplicación
            resultado = 1
            for num in lista:
                resultado *= num
            return resultado
        elif operacion == 4:  # División (dividir el primer elemento por todos los demás)
            resultado = lista[0]
            for num in lista[1:]:
                if num == 0:
                    raise ZeroDivisionError("Error: División por cero.")
                resultado /= num
            return resultado
    except TypeError:
        raise TypeError("Error: La lista contiene elementos no numéricos.")
    except ZeroDivisionError as e:
        raise e

def main():
    """Función principal que ejecuta el programa."""
    try:
        lista = obtener_lista()
        operacion = elegir_operacion()
        resultado = realizar_operacion(lista, operacion)
        print(f"\nEl resultado de la operación es: {resultado}")
    except ValueError as ve:
        print(ve)
    except TypeError as te:
        print(te)
    except ZeroDivisionError as zde:
        print(zde)
    finally:
        print("\nPrograma finalizado.")

# Ejecutar el programa
main()









