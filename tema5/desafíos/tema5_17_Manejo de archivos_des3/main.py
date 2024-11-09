# tema5_17_Manejo de archivos
# Número de desafío: 3
# Consigna:
'''
Tienes un archivo inventario.csv que contiene una lista de libros y el número de copias disponibles. 
Escribe un programa que permita actualizar la cantidad de copias de un libro específico. 
El programa debe leer el archivo, modificar el número de copias y volver a escribir el archivo.
'''
# Autora: Eliana D

import csv

def actualizar_copias():
    # Solicitar el título del libro y la nueva cantidad de copias
    titulo_libro = input("Ingrese el título del libro a actualizar: ")
    try:
        nuevas_copias = int(input("Ingrese la nueva cantidad de copias: "))
    except ValueError:
        print("La cantidad de copias debe ser un número entero.")
        return

    # Leer el archivo CSV
    try:
        with open('inventario.csv', 'r', newline='', encoding='utf-8') as archivo:
            lector = csv.reader(archivo)
            libros = list(lector)  # Leer todo el contenido del archivo

        # Buscar el libro y actualizar la cantidad de copias
        libro_encontrado = False
        for fila in libros:
            if fila[0].strip().lower() == titulo_libro.strip().lower():  # Comparación insensible a mayúsculas
                fila[1] = str(nuevas_copias)  # Actualizar la cantidad de copias
                libro_encontrado = True
                print(f"Cantidad de copias de '{titulo_libro}' actualizada a {nuevas_copias}.")
                break

        if not libro_encontrado:
            print(f"No se encontró el libro '{titulo_libro}' en el inventario.")

        # Escribir los datos actualizados de vuelta al archivo
        with open('inventario.csv', 'w', newline='', encoding='utf-8') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerows(libros)
    
    except FileNotFoundError:
        print("El archivo 'inventario.csv' no se encuentra.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Ejecutar la función
actualizar_copias()
