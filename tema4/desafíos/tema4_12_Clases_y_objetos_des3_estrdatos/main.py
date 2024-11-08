# 4_12_Clases_y_objetos
### Desafío 3: Considera cómo podrías implementar una biblioteca que almacene múltiples autores y libros. 
#¿Qué estructuras de datos usarías?
# Autor: Eliana Dalfolo

'''
Aspectos a destacar

Para almacenar los autores y libros, uso un diccionario. 
La clave es el nombre del autor y el valor es un objeto de la clase Autor, que contiene una lista de libros. 
Accedo rápido a los autores por su nombre y visualizo la lista de libros de cada autor.

Clase Libro:
Representa un libro con un título, género e ISBN.
La función __str__ se usa para mostrar el libro en un formato legible.
Clase Biblioteca:

Gestiona una lista de autores usando un diccionario, donde la clave es el nombre del autor y el valor es el objeto Autor.
Los métodos agregar_autor, buscar_libro y mostrar_biblioteca permiten agregar autores, buscar libros por título y mostrar todos los libros de la biblioteca.

El usuario puede agregar autores y libros, buscar un libro por su título e imprimir toda la biblioteca.
Los libros son buscados y mostrados según el título ingresado por el usuario.

'''

print("\n === MENÚ === ")
print("1. Crear una biblioteca con múltiples autores y libros")
print("2. Salir")

# Solicitar la opción del usuario
opcion = int(input("\nSeleccione una opción: "))

if opcion == 1:
    # Clase Autor para representar autores con una lista de libros
    class Autor:
        def __init__(self, nombre, nacionalidad):
            self.nombre = nombre  # Nombre del autor
            self.nacionalidad = nacionalidad  # Nacionalidad del autor
            self.libros = []  # Lista para almacenar los libros escritos por el autor

        def agregar_libro(self, libro):
            """Agrega un libro a la lista de libros del autor"""
            self.libros.append(libro)  # Añadir libro a la lista de libros

        def mostrar_libros(self):
            """Muestra todos los libros escritos por el autor"""
            print(f"Libros escritos por {self.nombre}:")
            for libro in self.libros:
                print(f"- {libro}")  # Mostrar cada libro en la lista

    # Clase Libro para representar libros con título, autor y género
    class Libro:
        def __init__(self, titulo, genero, isbn):
            self.titulo = titulo  # Título del libro
            self.genero = genero  # Género del libro
            self.isbn = isbn  # ISBN del libro

        def __str__(self):
            return f"{self.titulo} ({self.genero}, ISBN: {self.isbn})"  # Formato para mostrar el libro

    # Clase Biblioteca para gestionar autores y libros
    class Biblioteca:
        def __init__(self):
            """
            Inicializa la biblioteca con un diccionario vacío de autores.
            El diccionario tiene como clave el nombre del autor y como valor un objeto Autor.
            """
            self.autores = {}  # Diccionario vacío para almacenar los autores.

        def agregar_autor(self, autor):
            """
            Agrega un autor a la biblioteca.
            :param autor: Un objeto de la clase Autor.
            """
            self.autores[autor.nombre] = autor  # Agrega el autor al diccionario usando su nombre como clave.

        def buscar_libro(self, titulo):
            """
            Busca un libro en la biblioteca por su título.
            :param titulo: El título del libro que se desea buscar.
            :return: El libro si se encuentra, None si no se encuentra.
            """
            for autor in self.autores.values():  # Recorremos todos los autores de la biblioteca.
                for libro in autor.libros:  # Recorremos los libros de cada autor.
                    if libro.titulo == titulo:  # Si encontramos el libro con el título buscado.
                        return libro  # Retornamos el libro encontrado.
            return None  # Si no se encuentra el libro, retornamos None.

        def mostrar_biblioteca(self):
            """
            Muestra todos los libros de todos los autores en la biblioteca.
            """
            print("\nBiblioteca completa:")
            for autor in self.autores.values():  # Recorremos todos los autores.
                autor.mostrar_libros()  # Mostramos los libros de cada autor

    # Crear la biblioteca
    biblioteca = Biblioteca()

    # Solicitar al usuario agregar autores y libros
    num_autores = int(input("\n¿Cantidad de autores a agregar a la biblioteca? "))
    
    for _ in range(num_autores):
        # Solicitar los datos del autor
        nombre_autor = input("\nIngrese el nombre del autor: ")
        nacionalidad_autor = input("Ingrese la nacionalidad del autor: ")

        # Crear objeto Autor
        autor = Autor(nombre_autor, nacionalidad_autor)

        # Solicitar los libros del autor
        num_libros = int(input(f"\n¿Cuántos libros tiene {nombre_autor}? "))
        
        for _ in range(num_libros):
            titulo_libro = input("\nIngrese el título del libro: ")
            genero_libro = input("Ingrese el género del libro: ")
            isbn_libro = input("Ingrese el ISBN del libro: ")

            # Crear objeto Libro
            libro = Libro(titulo_libro, genero_libro, isbn_libro)
            autor.agregar_libro(libro)  # Agregar el libro al autor

        # Agregar el autor a la biblioteca
        biblioteca.agregar_autor(autor)

    # Mostrar todos los libros de la biblioteca
    biblioteca.mostrar_biblioteca()

    # Buscar un libro por título
    titulo_buscar = input("\nIngrese el título del libro que desea buscar: ")  # Solicitar al usuario un título de libro.
    libro_encontrado = biblioteca.buscar_libro(titulo_buscar)  # Buscar el libro en la biblioteca.
    if libro_encontrado:  # Si el libro es encontrado, lo mostramos.
        print(f"\nLibro encontrado: {libro_encontrado}")  # Mostramos la información del libro.
    else:
        print(f"\nEl libro '{titulo_buscar}' no se encuentra en la biblioteca.")  # Si no se encuentra, mostramos un mensaje.

else:
    print("\nOpción no válida.")









