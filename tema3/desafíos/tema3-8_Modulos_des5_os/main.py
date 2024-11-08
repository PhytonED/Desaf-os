# Tema 3-8 MÓDULOS
# **Desafio 5:**
# Utiliza el módulo `os` para interactuar con el sistema operativo y añade características como guardar un archivo o leer un archivo existente en nuestro procesador de texto.
# Autor: Eliana Dalfolo

'''
Aspectos a destacar
- except Exception as e: Captura cualquier error que ocurra durante el proceso de guardar el archivo, como problemas de permisos.
- os.path.exists(nombre_archivo): Verifica si el archivo existe en la ubicación especificada.
'''
# Importar el módulo os para interactuar con el sistema operativo
import os  # Usamos os para realizar operaciones como verificar la existencia de archivos y gestionar rutas.

# Función para guardar texto en un archivo
def guardar_archivo(nombre_archivo, contenido):
    """
    Guarda el texto proporcionado en un archivo con el nombre especificado.
    Si el archivo no existe, lo crea. Si ya existe, sobrescribe su contenido.
    """
    try:
        with open(nombre_archivo, 'w') as archivo:  # 'w' abre el archivo para escritura (sobrescribe el contenido si ya existe).
            archivo.write(contenido)  # Escribe el contenido en el archivo.
        print(f"\nEl archivo '{nombre_archivo}' se ha guardado correctamente.")  # Confirmación de guardado.
    except Exception as e:  # Si ocurre un error, como un problema de permisos, se captura la excepción.
        print(f"\nError al guardar el archivo: {e}")  # Imprimir el mensaje de error.

# Función para leer el contenido de un archivo
def leer_archivo(nombre_archivo):
    """
    Lee el contenido de un archivo y lo devuelve como un string.
    Si el archivo no existe, muestra un mensaje de error.
    """
    if os.path.exists(nombre_archivo):  # Verificamos si el archivo existe en el sistema.
        try:
            with open(nombre_archivo, 'r') as archivo:  # 'r' abre el archivo para lectura.
                contenido = archivo.read()  # Lee todo el contenido del archivo y lo guarda en la variable 'contenido'.
            return contenido  # Retorna el contenido del archivo.
        except Exception as e:  # Si ocurre un error durante la lectura, lo capturamos.
            print(f"\nError al leer el archivo: {e}")  # Imprimir el mensaje de error.
    else:
        print(f"\nEl archivo '{nombre_archivo}' no existe.")  # Si el archivo no se encuentra, se notifica al usuario.
        return None  # Retorna None si el archivo no existe.

# Función principal que permite al usuario elegir entre guardar o leer un archivo
def menu():
    """
    Muestra un menú donde el usuario puede elegir entre guardar un archivo o leer uno existente.
    """
    while True:
        print("\n--- OPCIONES ---")
        print("1. Guardar archivo")
        print("2. Leer archivo")
        print("3. Salir")
        
        opcion = input("\nIngresa una opción: ")  # Solicita al usuario que elija una opción.

        if opcion == '1':  # Si elige la opción 1, el programa guarda un archivo.
            nombre_archivo = input("\nIngresa el nombre del archivo a guardar: ")  # Pide el nombre del archivo.
            contenido = input("\nIngresa el contenido del archivo: ")  # Pide el contenido del archivo.
            guardar_archivo(nombre_archivo, contenido)  # Llama a la función para guardar el archivo.
        
        elif opcion == '2':  # Si elige la opción 2, el programa lee un archivo.
            nombre_archivo = input("\nIngresa el nombre del archivo a leer: ")  # Pide el nombre del archivo.
            contenido = leer_archivo(nombre_archivo)  # Llama a la función para leer el archivo.
            if contenido:  # Si el archivo existe y fue leído con éxito, muestra su contenido.
                print("\nContenido del archivo:")
                print(contenido)  # Muestra el contenido leído.
        
        elif opcion == '3':  # Si elige la opción 3, el programa termina.
            print("Saliendo")  # Mensaje de despedida.
            break  # Sale del bucle, terminando el programa.
        
        else:
            print("\nOpción inválida, por favor elige una opción válida.")  # Si elige una opción no válida, muestra un mensaje de error.
            

# Llamamos a la función menu() para iniciar el programa
menu()






