#4_13_Encapsulamiento
### Desafío 4: Crea una función que tome un objeto Autor y devuelva una lista de todos los títulos de libros escritos por el autor. 
# Asegúrate de que la lista de libros sea accesible solo a través de métodos de la clase Autor.
# Eliana D


class Autor:
    def __init__(self, nombre, nacionalidad):
        """Inicializa un objeto Autor con nombre y nacionalidad."""
        self.__nombre = nombre
        self.__nacionalidad = nacionalidad
        self.__libros = []  # Lista de libros escritos por el autor
    
    @property
    def nombre(self):
        """Getter para el atributo nombre del autor."""
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        """Setter para el atributo nombre del autor."""
        self.__nombre = nombre
    
    def agregar_libro(self, libro):
        """Agrega un libro a la lista de libros escritos por el autor."""
        self.__libros.append(libro)
    
    def obtener_libros(self):
        """Devuelve la lista de libros escritos por el autor."""
        return self.__libros
    
def obtener_titulos_libros(autor):
    """Función externa que devuelve los títulos de todos los libros escritos por un autor."""
    return autor.obtener_libros()

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

# Obtener y mostrar los títulos de los libros
titulos = obtener_titulos_libros(autor)
print("Libros escritos por el autor:")
for titulo in titulos:
    print(titulo)
































