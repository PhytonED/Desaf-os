# 4_12_Clases_y_objetos
### Desafío 4: Piensa en otros atributos y métodos que podrías agregar a la clase `Autor` para hacerla más completa.
# Autor: Eliana Dalfolo

'''
Atributos adicionales:

    __fecha_nacimiento: Guarda la fecha de nacimiento del autor.
    __genero_literario: Representa el género literario del autor (ejemplo: ficción, no ficción).
    __libros: Lista privada de los libros escritos por el autor.
    __biografia: Contiene la biografía del autor.

Métodos adicionales:

    obtener_edad: Este método calcula la edad del autor tomando su fecha de nacimiento y comparándola con la fecha actual.
    set_biografia y obtener_biografia: Permiten establecer y obtener la biografía del autor.
    agregar_libro y obtener_libros: Métodos para agregar y obtener libros del autor.
'''

# Desafío 4: Ampliación de la clase Autor con edad en lugar de premios
# Autor: Eliana D.
# Esta versión de la clase Autor incluye nuevos atributos y métodos para hacerla más completa,
# como la fecha de nacimiento, género literario, libros escritos, biografía y edad calculada automáticamente.

from datetime import datetime

class Autor:
    def __init__(self, nombre, nacionalidad, fecha_nacimiento, genero_literario):
        """Inicializa un objeto Autor con nombre, nacionalidad, fecha de nacimiento,
        género literario, lista de libros escritos y biografía."""
        self.__nombre = nombre
        self.__nacionalidad = nacionalidad
        self.__fecha_nacimiento = fecha_nacimiento  # Atributo privado
        self.__genero_literario = genero_literario  # Atributo privado
        self.__libros = []  # Lista privada de libros escritos por el autor
        self.__biografia = ""  # Biografía del autor
    
    @property
    def nombre(self):
        """Getter para el atributo nombre del autor."""
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        """Setter para el atributo nombre del autor."""
        self.__nombre = nombre
    
    @property
    def nacionalidad(self):
        """Getter para la nacionalidad del autor."""
        return self.__nacionalidad
    
    @nacionalidad.setter
    def nacionalidad(self, nacionalidad):
        """Setter para la nacionalidad del autor."""
        self.__nacionalidad = nacionalidad
    
    @property
    def fecha_nacimiento(self):
        """Getter para la fecha de nacimiento del autor."""
        return self.__fecha_nacimiento
    
    @fecha_nacimiento.setter
    def fecha_nacimiento(self, fecha_nacimiento):
        """Setter para la fecha de nacimiento del autor."""
        self.__fecha_nacimiento = fecha_nacimiento
    
    @property
    def genero_literario(self):
        """Getter para el género literario del autor."""
        return self.__genero_literario
    
    @genero_literario.setter
    def genero_literario(self, genero_literario):
        """Setter para el género literario del autor."""
        self.__genero_literario = genero_literario
    
    def agregar_libro(self, libro):
        """Agrega un libro a la lista de libros escritos por el autor."""
        self.__libros.append(libro)
    
    def obtener_libros(self):
        """Devuelve la lista de libros escritos por el autor."""
        return self.__libros
    
    def set_biografia(self, biografia):
        """Establece la biografía del autor."""
        self.__biografia = biografia
    
    def obtener_biografia(self):
        """Devuelve la biografía del autor."""
        return self.__biografia
    
    def obtener_edad(self):
        """Devuelve la edad del autor calculada a partir de la fecha de nacimiento."""
        today = datetime.today()
        birth_date = datetime.strptime(self.__fecha_nacimiento, "%d/%m/%Y")
        age = today.year - birth_date.year
        if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
            age -= 1
        return age

    def __str__(self):
        """Devuelve la representación del autor con todos sus atributos."""
        return f"Autor: {self.__nombre}, Nacionalidad: {self.__nacionalidad}, Género: {self.__genero_literario}, Edad: {self.obtener_edad()} años"

# Solicitar datos al usuario
nombre = input("Ingresa el nombre del autor: ")
nacionalidad = input("Ingresa la nacionalidad del autor: ")
fecha_nacimiento = input("Ingresa la fecha de nacimiento del autor (dd/mm/aaaa): ")
genero_literario = input("Ingresa el género literario del autor: ")

# Crear un objeto Autor
autor = Autor(nombre, nacionalidad, fecha_nacimiento, genero_literario)

# Agregar libros al autor
num_libros = int(input(f"¿Cuántos libros tiene {nombre}? "))
for _ in range(num_libros):
    titulo = input("Ingresa el título del libro: ")
    autor.agregar_libro(titulo)

# Establecer biografía del autor
biografia = input("Ingresa una breve biografía del autor: ")
autor.set_biografia(biografia)

# Imprimir la información del autor
print("\nInformación del autor:")
print(autor)

# Mostrar los libros del autor
print("\nLibros escritos por el autor:")
for libro in autor.obtener_libros():
    print(f"- {libro}")

# Mostrar la biografía del autor
print(f"\nBiografía del autor: {autor.obtener_biografia()}")

# Mostrar la edad del autor
print(f"\nEdad del autor: {autor.obtener_edad()} años")





























































































