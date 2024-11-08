# 4_12_Clases_y_objetos
### Crea una clase `Libro` con atributos como título, género e ISBN. 
# ¿Cómo podrías relacionar esta clase con la clase `Autor`?
# Autor: Eliana Dalfolo

'''
Respuesta
Relación entre Autor y Libro: La clase Autor tiene una lista libros que contiene objetos de la clase Libro. 
Cada autor puede tener múltiples libros asociados, permitiendo establecer una relación de uno a muchos entre autor y libros.
'''

# Clase Libro: Define un libro con atributos como título, género e ISBN.
class Libro:
    def __init__(self, titulo, genero, isbn):
        """
        Inicializa un libro con su título, género e ISBN.
        :param titulo: El título del libro.
        :param genero: El género del libro.
        :param isbn: El número ISBN del libro.
        """
        self.titulo = titulo  # Atributo para almacenar el título del libro.
        self.genero = genero  # Atributo para almacenar el género del libro.
        self.isbn = isbn  # Atributo para almacenar el ISBN del libro.

    def mostrar_info(self):
        """
        Muestra la información completa del libro.
        """
        print(f"Título: {self.titulo}")  # Muestra el título del libro.
        print(f"Género: {self.genero}")  # Muestra el género del libro.
        print(f"ISBN: {self.isbn}")  # Muestra el ISBN del libro.

# Clase Autor: Relacionada con la clase Libro, cada autor puede tener múltiples libros.
class Autor:
    def __init__(self, nombre, nacionalidad):
        """
        Inicializa un autor con nombre, nacionalidad y una lista vacía de libros.
        :param nombre: El nombre del autor.
        :param nacionalidad: La nacionalidad del autor.
        """
        self.nombre = nombre  # Atributo para almacenar el nombre del autor.
        self.nacionalidad = nacionalidad  # Atributo para almacenar la nacionalidad del autor.
        self.libros = []  # Lista vacía para almacenar los libros escritos por el autor.

    def agregar_libro(self, libro):
        """
        Agrega un libro a la lista de libros del autor.
        :param libro: Un objeto de la clase Libro que representa el libro a agregar.
        """
        self.libros.append(libro)  # Añadimos el libro a la lista de libros.

    def mostrar_libros(self):
        """
        Muestra la lista de libros escritos por el autor.
        """
        for libro in self.libros:  # Recorremos todos los libros de la lista.
            libro.mostrar_info()  # Llamamos al método mostrar_info del objeto Libro para mostrar su información.

# Solicitar al usuario los datos del autor
print("\n === Ingresar autor ===")
nombre_autor = input("\nIngrese el nombre del autor: ")  # Pedimos el nombre del autor.
nacionalidad_autor = input("Ingrese la nacionalidad del autor: ")  # Pedimos la nacionalidad del autor.

# Crear el autor e instanciar libros
autor = Autor(nombre_autor, nacionalidad_autor)

# Solicitar los libros del autor
while True:
    titulo = input(f"\nIngrese un título de libro escrito por {nombre_autor} (o 's' para salir): ")  # Pedimos el título del libro.
    if titulo.lower() == 's':  # Si el usuario escribe 'salir', se termina el bucle.
        break  # Salimos del bucle si no queremos ingresar más libros.
    genero = input(f"Ingrese el género del libro '{titulo}': ")  # Pedimos el género del libro.
    isbn = input(f"Ingrese el ISBN del libro '{titulo}': ")  # Pedimos el ISBN del libro.
    
    # Creamos el libro y lo agregamos al autor
    libro = Libro(titulo, genero, isbn)
    autor.agregar_libro(libro)  # Agregamos el libro al autor.

# Mostrar todos los libros del autor
autor.mostrar_libros()





























































