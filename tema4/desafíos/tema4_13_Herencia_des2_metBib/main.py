#4_13_Herencia
### Desafío 2: Crea una clase Bibliotecario que herede de Usuario y 
# tenga atributos específicos como sección y años_experiencia.
# Autor: Eliana Dalfolo

'''
Clase de la que hereda(Usuario): Representa atributos básicos de un usuario.
Clase que hereda (Bibliotecario): Hereda de Usuario e incluye atributos específicos como sección y años_experiencia.
'''

# -------------------------------
# Clase Usuario como base para Bibliotecario
# -------------------------------

class Usuario:
    """
    Clase base que representa un usuario en general.
    """
    
    def __init__(self, nombre):
        """
        Constructor de la clase Usuario.
        
        Parámetros:
            nombre (str): El nombre del usuario.
        """
        self.__nombre = nombre  # Atributo privado para el nombre del usuario
    
    @property
    def nombre(self):
        """Método getter para obtener el nombre del usuario."""
        return self.__nombre

# -------------------------------
# Clase Bibliotecario que hereda de Usuario
# -------------------------------

class Bibliotecario(Usuario):
    """
    Clase que representa a un bibliotecario, derivada de Usuario.
    Incluye atributos adicionales específicos de su rol.
    """
    
    def __init__(self, nombre, seccion, años_experiencia):
        """
        Constructor de la clase Bibliotecario.
        
        Parámetros:
            nombre (str): El nombre del bibliotecario.
            seccion (str): La sección de la biblioteca donde trabaja.
            años_experiencia (int): Los años de experiencia del bibliotecario.
        """
        super().__init__(nombre)  # Llamada al constructor de la clase base Usuario
        self.__seccion = seccion  # Atributo privado para la sección
        self.__años_experiencia = años_experiencia  # Atributo privado para los años de experiencia
    
    @property
    def seccion(self):
        """Método getter para obtener la sección donde trabaja."""
        return self.__seccion
    
    @property
    def años_experiencia(self):
        """Método getter para obtener los años de experiencia."""
        return self.__años_experiencia

# -------------------------------
# Función para interactuar con el usuario
# -------------------------------

def ingresar_bibliotecario():
    """
    Función para ingresar datos del bibliotecario y crear un objeto Bibliotecario.
    """
    nombre = input("Ingresa el nombre del bibliotecario: ")
    seccion = input("Ingresa la sección donde trabaja: ")
    while True:
        try:
            años_experiencia = int(input("Ingresa los años de experiencia: "))
            break
        except ValueError:
            print("Valor no válido. Ingresa un número entero.")
    
    bibliotecario = Bibliotecario(nombre, seccion, años_experiencia)
    print(f"\nBibliotecario creado: {bibliotecario.nombre}, Sección: {bibliotecario.seccion}, Años de experiencia: {bibliotecario.años_experiencia}")

# -------------------------------
# Llamada al menú de interacción para el desafío 2
# -------------------------------

ingresar_bibliotecario()








































