# tema4_10_TAD
# Título: Gestión de Personajes y Armas para un Juego de Video
# Autora: Eliana D
# Descripción: Este código maneja personajes y armas en un juego, permitiendo cambios frecuentes en los requisitos y la adición de nuevos personajes y habilidades.

'''
Clase Personaje: Representa un personaje en el juego. Cada personaje tiene un nombre, salud y habilidades. El método atacar simula el ataque del personaje con un arma.
Clase Arma: Representa un arma en el juego, con nombre y daño asociado.
Función gestionar_juego: Permite crear personajes y asignarles armas, con la posibilidad de actualizar los personajes añadiendo nuevas habilidades o armas según los cambios en los requisitos del juego.
'''

class Personaje:
    """Clase que representa a un personaje en el juego."""
    def __init__(self, nombre, salud, habilidades):
        """
        Inicializa un personaje con nombre, salud y habilidades.
        :param nombre: Nombre del personaje.
        :param salud: Salud inicial del personaje.
        :param habilidades: Lista de habilidades del personaje.
        """
        self.nombre = nombre
        self.salud = salud
        self.habilidades = habilidades

    def atacar(self, arma):
        """Simula el ataque de un personaje usando un arma."""
        print(f"{self.nombre} ataca con {arma.nombre} causando {arma.daño} de daño.")

class Arma:
    """Clase que representa un arma en el juego."""
    def __init__(self, nombre, daño):
        """
        Inicializa un arma con nombre y daño.
        :param nombre: Nombre del arma.
        :param daño: Daño que causa el arma.
        """
        self.nombre = nombre
        self.daño = daño

# Función principal para gestionar personajes y armas
def gestionar_juego():
    """
    Función que permite crear personajes y asignarles armas en el juego.
    Permite cambios en los requisitos al agregar nuevas habilidades o armas.
    """
    # Crear personajes y armas
    nombre_personaje = input("Ingrese el nombre del personaje: ")
    salud = int(input("Ingrese la salud del personaje: "))
    habilidades = input("Ingrese las habilidades del personaje (separadas por coma): ").split(",")
    personaje = Personaje(nombre_personaje, salud, habilidades)

    # Crear arma
    nombre_arma = input("Ingrese el nombre del arma: ")
    daño = int(input("Ingrese el daño del arma: "))
    arma = Arma(nombre_arma, daño)

    # Personaje ataca con el arma
    personaje.atacar(arma)

# Ejecución del sistema
gestionar_juego()  # Ejecutamos la función para gestionar personajes y armas
