#4_13_Encapsulamiento
### Desafío 2: 
# Modifica la clase Autor para que pueda tener una lista de libros escritos por el autor. 
# Proporciona un método para agregar libros a esta lista.
# Autor: Eliana Dalfolo

# Desafío 2: Modificación de la Clase Autor
# Autor: Eliana D.
# Esta clase representa un autor, con un atributo privado para almacenar la lista de libros que ha escrito.
# Se proporciona un método para agregar libros a esta lista.

'''
Clase Autor: Representa un autor con atributos privados para nombre, nacionalidad y una lista de libros escritos.
Métodos Getter y Setter: Controlan el acceso a los atributos privados de nombre y nacionalidad.
Método agregar_libro: Permite agregar un libro a la lista de libros del autor.
Método obtener_libros: Devuelve la lista de libros escritos por el autor.
Ingreso de Datos: El usuario ingresa el nombre y la nacionalidad del autor.
Agregar Libros: El usuario puede agregar una cantidad de libros al autor y ver la lista de libros escritos.
'''

class Autor:
    def __init__(self, nombre, nacionalidad):
        """Inicializa un objeto Autor con nombre y nacionalidad, y una lista vacía de libros."""
        self.__nombre = nombre            # Atributo privado: Nombre del autor
        self.__nacionalidad = nacionalidad  # Atributo privado: Nacionalidad del autor
        self.__libros = []               # Atributo privado: Lista de libros escritos por el autor
    
    @property
    def nombre(self):
        """Getter para el atributo nombre."""
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        """Setter para el atributo nombre."""
        self.__nombre = nombre
    
    @property
    def nacionalidad(self):
        """Getter para el atributo nacionalidad."""
        return self.__nacionalidad
    
    @nacionalidad.setter
    def nacionalidad(self, nacionalidad):
        """Setter para el atributo nacionalidad."""
        self.__nacionalidad = nacionalidad
    
    def agregar_libro(self, libro):
        """Método para agregar un libro a la lista de libros del autor."""
        self.__libros.append(libro)
    
    def obtener_libros(self):
        """Método para obtener la lista de libros escritos por el autor."""
        return self.__libros
    
    def __str__(self):
        """Devuelve una representación del autor."""
        return f"Autor: {self.__nombre}, Nacionalidad: {self.__nacionalidad}"

# Solicitar datos del autor
nombre = input("Ingresa el nombre del autor: ")
nacionalidad = input("Ingresa la nacionalidad del autor: ")

# Crear un objeto Autor con los datos ingresados
autor = Autor(nombre, nacionalidad)

# Crear y agregar libros
num_libros = int(input("¿Cuántos libros quieres agregar al autor? "))
for _ in range(num_libros):
    titulo = input("Ingresa el título del libro: ")
    autor.agregar_libro(titulo)

# Mostrar la información del autor y los libros
print(autor)
print("Libros escritos por el autor:")
for libro in autor.obtener_libros():
    print(libro)










































































































