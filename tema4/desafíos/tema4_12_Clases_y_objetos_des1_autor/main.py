# 4_12_Clases_y_objetos
### Desafío 1: Amplía la clase `Autor` para incluir una lista de libros escritos por el autor. 
# Implementa métodos para agregar y eliminar libros de esta lista.
# Autor: Eliana Dalfolo

# Clase Autor: Define un autor con su nombre, nacionalidad y una lista de libros escritos.
class Autor:
    def __init__(self, nombre, nacionalidad):
        """
        Inicializa un objeto Autor con nombre, nacionalidad y una lista vacía de libros.
        :param nombre: El nombre del autor.
        :param nacionalidad: La nacionalidad del autor.
        """
        self.nombre = nombre  # Almacenamos el nombre del autor.
        self.nacionalidad = nacionalidad  # Almacenamos la nacionalidad del autor.
        self.libros = []  # Lista vacía para almacenar los libros escritos por el autor.

    def agregar_libro(self, libro):
        """
        Agrega un libro a la lista de libros del autor.
        :param libro: El nombre del libro que se va a agregar.
        """
        self.libros.append(libro)  # Añadimos el libro a la lista de libros del autor.
        print(f"\nEl libro '{libro}' ha sido agregado a la lista de {self.nombre}.")  # Confirmación de que el libro fue agregado.

    def eliminar_libro(self, libro):
        """
        Elimina un libro de la lista de libros del autor si está presente.
        :param libro: El nombre del libro que se desea eliminar.
        """
        if libro in self.libros:  # Comprobamos si el libro está en la lista.
            self.libros.remove(libro)  # Eliminamos el libro de la lista.
            print(f"\nEl libro '{libro}' ha sido eliminado de la lista de {self.nombre}.")  # Confirmación de que el libro fue eliminado.
        else:
            print(f"\nEl libro '{libro}' no se encuentra en la lista de {self.nombre}.")  # Mensaje si el libro no se encuentra.

    def mostrar_libros(self):
        """
        Muestra todos los libros escritos por el autor.
        """
        if self.libros:  # Si la lista de libros no está vacía.
            print(f"\nLibros escritos por {self.nombre}:")  # Título que indica los libros del autor.
            for libro in self.libros:  # Recorremos todos los libros.
                print(f"- {libro}")  # Imprimimos el nombre de cada libro.
        else:
            print(f"{self.nombre} no ha escrito ningún libro aún.")  # Mensaje si no hay libros.

# Solicitar datos del autor
print("\nIngresar autor")
nombre_autor = input("\nIngrese el nombre del autor: ")  # Pedimos el nombre del autor.
nacionalidad_autor = input("Ingrese la nacionalidad del autor: ")  # Pedimos la nacionalidad del autor.

# Creamos un objeto Autor con los datos ingresados por el usuario
autor = Autor(nombre_autor, nacionalidad_autor)

# Agregar libros al autor
while True:
    libro = input(f"\nIngrese un libro escrito por {nombre_autor} (o 's' para salir): ")  # Solicitar al usuario un libro.
    if libro.lower() == 's':  # Si el usuario escribe 'salir', se termina el bucle.
        break  # Salimos del bucle si el usuario decide no agregar más libros.
    autor.agregar_libro(libro)  # Agregamos el libro a la lista del autor.

# Mostrar todos los libros del autor
autor.mostrar_libros()

# Eliminar un libro
libro_a_eliminar = input(f"\nIngrese el nombre de un libro de {nombre_autor} que desea eliminar: ")  # Pedimos el libro a eliminar.
autor.eliminar_libro(libro_a_eliminar)  # Llamamos al método de eliminar para borrar el libro.

# Mostrar los libros restantes
autor.mostrar_libros()  # Mostramos la lista actualizada de libros.
























































