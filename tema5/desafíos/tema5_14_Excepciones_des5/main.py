# 5_14_Excepciones
# Número de desafío: 5
# Consigna: Desarrolla un programa que abra un archivo de texto, lea su contenido y lo muestre. Implementa manejo de excepciones para archivos que no existan y usa finally para asegurarte de que el archivo se cierre adecuadamente en cualquier caso.
# Autora: Eliana D


def leer_archivo(nombre_archivo):
    """Lee y muestra el contenido de un archivo de texto."""
    archivo = None
    try:
        # Intentar abrir el archivo en modo lectura
        archivo = open(nombre_archivo, 'r')
        
        # Leer el contenido del archivo y mostrarlo
        contenido = archivo.read()
        print("Contenido del archivo:")
        print(contenido)
    
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no existe.")
    except Exception as e:
        print(f"Error inesperado: {e}")
    finally:
        # Asegurarse de cerrar el archivo si fue abierto
        if archivo:
            archivo.close()
            print("El archivo ha sido cerrado.")

# Solicitar al usuario el nombre del archivo
nombre_archivo = input("Ingresa el nombre del archivo que deseas leer: ")
leer_archivo(nombre_archivo)












