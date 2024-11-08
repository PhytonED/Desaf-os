#4_13_Encapsulamiento
### Desafío 5: Desarrolla una función que reciba una lista de objetos Autor y 
# devuelva el autor que ha escrito el mayor número de libros. 
# Utiliza el encapsulamiento para acceder a la información necesaria de cada objeto Autor.
# Eliana D

'''
Método obtener_numero_de_libros: Devuelve el número de libros que el autor ha escrito utilizando el encapsulamiento de la lista __libros.
Función autor_con_mas_libros: Toma una lista de objetos Autor y utiliza la función max para encontrar el autor con el mayor número de libros, usando el atributo privado __libros.
Ingreso de Datos: El usuario ingresa la cantidad de autores y sus libros, de forma interactiva.
'''
class Autor:
    def __init__(self, nombre, nacionalidad):
        """Inicializa un objeto Autor con nombre, nacionalidad y lista de libros escritos."""
        self.__nombre = nombre
        self.__nacionalidad = nacionalidad
        self.__libros = []  # Lista privada de libros escritos por el autor
    
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
    
    def obtener_numero_de_libros(self):
        """Devuelve el número de libros escritos por el autor."""
        return len(self.__libros)
    
    def __str__(self):
        """Devuelve la representación del autor."""
        return f"Autor: {self.__nombre}, Nacionalidad: {self.__nacionalidad}"

def autor_con_mas_libros(autores):
    """Función que recibe una lista de autores y devuelve el que tiene más libros escritos."""
    if not autores:
        return None
    
    # Se encuentra al autor con el máximo número de libros
    autor_max = max(autores, key=lambda autor: autor.obtener_numero_de_libros())
    return autor_max

# Solicitar datos de los autores
num_autores = int(input("¿Cuántos autores quieres ingresar? "))
autores = []

for _ in range(num_autores):
    nombre = input("Ingresa el nombre del autor: ")
    nacionalidad = input("Ingresa la nacionalidad del autor: ")
    
    autor = Autor(nombre, nacionalidad)
    
    # Solicitar los libros del autor
    num_libros = int(input(f"¿Cuántos libros tiene {nombre}? "))
    for _ in range(num_libros):
        titulo = input("Ingresa el título del libro: ")
        autor.agregar_libro(titulo)
    
    autores.append(autor)

# Encontrar al autor con más libros escritos
autor_mas_libros = autor_con_mas_libros(autores)

if autor_mas_libros:
    print(f"El autor que ha escrito más libros es: {autor_mas_libros.nombre}")
else:
    print("No se encontraron autores.")







































