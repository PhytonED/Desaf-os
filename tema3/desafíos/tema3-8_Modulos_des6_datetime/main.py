# Tema 3-8 MÓDULOS
# **Desafio 6:**Calculadora de Fechas
# Objetivo: Escribir un programa en Python que permita calcular la diferencia entre dos fechas, utilizando el módulo `datetime.`
# Autor: Eliana Dalfolo

'''
Aspectos a destacar
- datetime.datetime.strptime(fecha_str, "%Y-%m-%d"): Este método convierte una cadena de texto que representa una fecha en un objeto datetime según el formato especificado ("%Y-%m-%d" en este caso, es decir, año-mes-día).
- .date(): Después de convertir la cadena a datetime, usamos .date() para obtener solo la parte de la fecha (sin la hora).
- función abs() asegura que el resultado sea siempre un valor positivo, independientemente del orden de las fechas ingresadas.
'''

# Importamos el módulo datetime para trabajar con fechas y horas
import datetime  # Este módulo proporciona clases para manipular fechas y horas en Python.

# Función que solicita al usuario dos fechas y calcula la diferencia entre ellas
def calcular_diferencia_fechas():
    """
    Esta función solicita al usuario dos fechas en formato 'YYYY-MM-DD' y calcula la diferencia entre ellas.
    """
    # Solicitar la primera fecha al usuario
    fecha1_str = input("Ingresa la primera fecha (formato YYYY-MM-DD): ")  # Pide al usuario que ingrese la primera fecha.
    
    # Solicitar la segunda fecha al usuario
    fecha2_str = input("Ingresa la segunda fecha (formato YYYY-MM-DD): ")  # Pide al usuario que ingrese la segunda fecha.
    
    try:
        # Convertir las cadenas de texto a objetos de fecha utilizando strptime
        fecha1 = datetime.datetime.strptime(fecha1_str, "%Y-%m-%d").date()  # Convierte la fecha1_str a un objeto de fecha.
        fecha2 = datetime.datetime.strptime(fecha2_str, "%Y-%m-%d").date()  # Convierte la fecha2_str a un objeto de fecha.
        
        # Calculamos la diferencia entre las fechas
        diferencia = abs(fecha2 - fecha1)  # La función abs() se usa para obtener la diferencia absoluta (sin importar el orden de las fechas).
        
        # Mostrar la diferencia en días
        print(f"La diferencia entre las fechas es de {diferencia.days} días.")  # Muestra la diferencia en días.

    except ValueError:
        # Si ocurre un error al convertir las fechas (por formato incorrecto), se maneja con un mensaje de error
        print("Error: El formato de las fechas no es válido. Asegúrate de seguir el formato YYYY-MM-DD.")  # Mensaje de error si el formato es incorrecto.

# Llamamos a la función para ejecutar el programa
calcular_diferencia_fechas()  # Ejecuta la función para calcular la diferencia entre las fechas.
