#4_13_Encapsulamiento
### Desafío 1: 
# Crea una clase Libro que tenga atributos privados para el título, autor y ISBN. 
# Proporciona métodos getter y setter para cada atributo.
# Autor: Eliana Dalfolo

'''
Clase Libro: Define la clase que tiene atributos privados para almacenar el título, autor e ISBN.
Métodos Getter y Setter: Se usan para controlar el acceso y modificación de los atributos privados (__titulo, __autor, __isbn).
Método __str__: Proporciona una forma amigable de mostrar la información del libro.
Ingreso de Datos: El usuario ingresa el título, autor e ISBN del libro.
'''

# Desafío 1: Clase Libro con Encapsulamiento
# Autor: Eliana D.
# Esta clase representa un libro con atributos privados. 
# Se proporcionan métodos getter y setter para controlar el acceso a estos atributos.

class Libro:
    def __init__(self, titulo, autor, isbn):
        """Inicializa un objeto Libro con título, autor e ISBN."""
        self.__titulo = titulo  # Atributo privado: Título del libro
        self.__autor = autor    # Atributo privado: Autor del libro
        self.__isbn = isbn      # Atributo privado: ISBN del libro
    
    @property
    def titulo(self):
        """Getter para el atributo título."""
        return self.__titulo
    
    @titulo.setter
    def titulo(self, titulo):
        """Setter para el atributo título."""
        self.__titulo = titulo
    
    @property
    def autor(self):
        """Getter para el atributo autor."""
        return self.__autor
    
    @autor.setter
    def autor(self, autor):
        """Setter para el atributo autor."""
        self.__autor = autor
    
    @property
    def isbn(self):
        """Getter para el atributo ISBN."""
        return self.__isbn
    
    @isbn.setter
    def isbn(self, isbn):
        """Setter para el atributo ISBN."""
        self.__isbn = isbn
    
    def __str__(self):
        """Devuelve una representación del libro."""
        return f"Título: {self.__titulo}, Autor: {self.__autor}, ISBN: {self.__isbn}"

# Solicitar datos al usuario
titulo = input("Ingresa el título del libro: ")
autor = input("Ingresa el nombre del autor: ")
isbn = input("Ingresa el ISBN del libro: ")

# Crear un objeto Libro con los datos ingresados
libro = Libro(titulo, autor, isbn)

# Mostrar la información del libro
print(libro)








