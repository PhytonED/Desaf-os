# 4_13_Polimorfismo
# Número de desafío: 3
# Consigna: Extiende la clase Libro para crear una subclase LibroEspecializado que tenga un campo de estudio 
# y un nivel de especialización.
# Autora: Eliana D

# Tema: Polimorfismo
# Número de desafío: 3
# Consigna: Extiende la clase Libro para crear una subclase LibroEspecializado que tenga un campo de estudio 
# y un nivel de especialización.
# Autora: Eliana D

# Puntos principales:
# - Se crea la clase base Libro con un método genérico de mostrar información.
# - Se extiende la clase Libro con la subclase LibroEspecializado, sobrescribiendo el método para incluir información adicional.
# - El polimorfismo se demuestra al sobrescribir un método en la subclase y usar un objeto de la subclase para invocar este comportamiento.

'''
Se crea una clase Libro con un método general para mostrar información.
En la subclase LibroEspecializado, sobrescribimos el método para que devuelva información adicional relacionada con el campo de estudio y el nivel de especialización.
Luego usamos el polimorfismo para mostrar cómo un objeto de la subclase puede "adoptar" el comportamiento sobrescrito.
'''
# Clase base Libro
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo  # Atributo para el título del libro
        self.autor = autor  # Atributo para el autor del libro

    def mostrar_info(self):
        """
        Método general para mostrar la información básica del libro.
        Este método puede ser sobrescrito por las subclases.
        """
        return f"Título: {self.titulo}\nAutor: {self.autor}"

# Subclase LibroEspecializado que extiende la clase Libro y sobrescribe el método mostrar_info
class LibroEspecializado(Libro):
    def __init__(self, titulo, autor, campo_estudio, nivel):
        super().__init__(titulo, autor)  # Llamada al constructor de la clase base
        self.campo_estudio = campo_estudio  # Atributo específico para el campo de estudio
        self.nivel = nivel  # Atributo para el nivel de especialización

    def mostrar_info(self):
        """
        Método sobrescrito para mostrar información detallada sobre el libro especializado,
        incluyendo el campo de estudio y el nivel de especialización.
        """
        # Llamamos al método de la clase base para obtener la información básica
        info_base = super().mostrar_info()
        # Extendemos la información con detalles específicos del libro especializado
        return f"{info_base}\nCampo de estudio: {self.campo_estudio}\nNivel: {self.nivel}"

# Función para solicitar datos al usuario y crear un libro especializado
def ingresar_libro_especializado():
    titulo = input("\nIngrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    campo_estudio = input("Ingrese el campo de estudio: ")
    nivel = input("Ingrese el nivel de especialización (básico, intermedio, avanzado): ")

    # Crear una instancia de la subclase LibroEspecializado
    libro_especializado = LibroEspecializado(titulo, autor, campo_estudio, nivel)

    # Mostrar la información del libro especializado
    print("\nInformación del libro especializado:")
    print(libro_especializado.mostrar_info())

# Llamada a la función para ingresar un libro especializado
ingresar_libro_especializado()


























