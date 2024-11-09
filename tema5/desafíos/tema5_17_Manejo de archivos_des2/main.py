# tema5_17_Manejo de archivos
# Número de desafío: 2
# Consigna:
'''
Dado un archivo libros.txt que contiene una lista de libros y sus autores, 
implementa una función que busque todos los libros escritos por un autor 
específico y los muestre. Si el autor no tiene libros en la lista, 
debe mostrar un mensaje indicando que no hay coincidencias.
'''
# Autora: Eliana D

def buscar_libros_por_autor(autor):
    try:
        # Abrir el archivo en modo lectura
        with open('libros.txt', 'r') as archivo:
            libros = archivo.readlines()
            
            # Filtrar los libros escritos por el autor especificado
            libros_autor = [linea.strip() for linea in libros if autor.lower() in linea.lower()]
            
            # Comprobar si se encontraron libros del autor
            if libros_autor:
                print(f"\nLibros escritos por {autor}:")
                for libro in libros_autor:
                    print(libro)
            else:
                print(f"No se encontraron libros de {autor}.")
    except FileNotFoundError:
        print("El archivo 'libros.txt' no existe.")

# Buscar el archivo
autor_buscar = input("Ingrese el nombre del autor a buscar: ")
buscar_libros_por_autor(autor_buscar)
