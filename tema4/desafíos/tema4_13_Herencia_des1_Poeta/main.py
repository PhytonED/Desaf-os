#4_13_Herencia
### Desafío 1: Implementa una clase Poeta que herede de Autor y 
# tenga un atributo para el tipo de poesía que escribe.
# Autor: Eliana Dalfolo

'''
Clase de la que hereda (Autor): Contiene atributos comunes para los autores, como nombre.
Clase que hereda (Poeta): Hereda de Autor e incluye un atributo adicional tipo_poesia.
'''
# -------------------------------
# Clase Autor como base para Poeta
# -------------------------------

class Autor:
    """
    Clase base que representa a un autor.
    """
    
    def __init__(self, nombre):
        """
        Constructor de la clase Autor.
        
        Parámetros:
            nombre (str): El nombre del autor.
        """
        self.__nombre = nombre  # Atributo privado del nombre del autor
    
    @property
    def nombre(self):
        """Método getter para obtener el nombre del autor."""
        return self.__nombre

# -------------------------------
# Clase Poeta que hereda de Autor
# -------------------------------

class Poeta(Autor):
    """
    Clase que representa a un poeta, derivada de Autor.
    Incluye un atributo adicional para el tipo de poesía.
    """
    
    def __init__(self, nombre, tipo_poesia):
        """
        Constructor de la clase Poeta.
        
        Parámetros:
            nombre (str): El nombre del poeta.
            tipo_poesia (str): El tipo de poesía que escribe.
        """
        super().__init__(nombre)  # Llamada al constructor de la clase base Autor
        self.__tipo_poesia = tipo_poesia  # Atributo privado del tipo de poesía
    
    @property
    def tipo_poesia(self):
        """Método getter para obtener el tipo de poesía."""
        return self.__tipo_poesia

# -------------------------------
# Función para interactuar con el usuario
# -------------------------------

def ingresar_poeta():
    """
    Función que permite al usuario ingresar los datos de un poeta.
    """
    nombre = input("\nIngresa el nombre del poeta: ")
    tipo_poesia = input("Ingresa el tipo de poesía que escribe: ")
    poeta = Poeta(nombre, tipo_poesia)  # Crea una instancia de Poeta
    print(f"\nPoeta creado: {poeta.nombre}, Tipo de Poesía: {poeta.tipo_poesia}")

# -------------------------------
# Llamada al menú de interacción para el desafío 1
# -------------------------------

ingresar_poeta()





