#4_13_Herencia
### Desafío 3: Diseña una clase LibroDigital que herede de Libro y 
# añada atributos como formato (e.g., PDF, EPUB) y tamaño_archivo. 
# Además, implementa una subclase EBook que sobrescriba un método 
# para mostrar información específica, como enlaces de descarga.
# Autor: Eliana Dalfolo

'''
Clase de la que hereda (Libro): Contiene atributos comunes de un libro como título.
Clase que hereda(LibroDigital): Hereda de Libro e incluye atributos adicionales específicos de un libro digital, como formato y tamaño_archivo.
Subclase (EBook): Hereda de LibroDigital y sobrescribe el método mostrar_info() para incluir información adicional, como enlaces de descarga.
'''

# -------------------------------
# Clase Libro como base para LibroDigital
# -------------------------------

class Libro:
    """
    Clase base que representa un libro.
    """
    
    def __init__(self, titulo):
        """
        Constructor de la clase Libro.
        
        Parámetros:
            titulo (str): El título del libro.
        """
        self.__titulo = titulo  # Atributo privado para el título del libro
    
    @property
    def titulo(self):
        """Método getter para obtener el título del libro."""
        return self.__titulo

# -------------------------------
# Clase LibroDigital que hereda de Libro
# -------------------------------

class LibroDigital(Libro):
    """
    Clase que representa un libro digital, derivada de Libro.
    Incluye atributos adicionales como formato y tamaño de archivo.
    """
    
    def __init__(self, titulo, formato, tamaño_archivo):
        """
        Constructor de la clase LibroDigital.
        
        Parámetros:
            titulo (str): El título del libro.
            formato (str): El formato del libro digital (e.g., PDF, EPUB).
            tamaño_archivo (float): Tamaño del archivo en MB.
        """
        super().__init__(titulo)  # Llamada al constructor de la clase base Libro
        self.__formato = formato  # Atributo privado para el formato
        self.__tamaño_archivo = tamaño_archivo  # Atributo privado para el tamaño de archivo
    
    @property
    def formato(self):
        """Método getter para obtener el formato del libro digital."""
        return self.__formato
    
    @property
    def tamaño_archivo(self):
        """Método getter para obtener el tamaño de archivo del libro digital."""
        return self.__tamaño_archivo
    
    def mostrar_info(self):
        """Método para mostrar la información del libro digital."""
        return f"Título: {self.titulo}, Formato: {self.formato}, Tamaño: {self.tamaño_archivo} MB"

# -------------------------------
# Subclase EBook que hereda de LibroDigital
# -------------------------------

class EBook(LibroDigital):
    """
    Clase que representa un eBook, derivada de LibroDigital.
    Incluye un método adicional para mostrar enlaces de descarga.
    """
    
    def __init__(self, titulo, formato, tamaño_archivo, enlace_descarga):
        """
        Constructor de la clase EBook.
        
        Parámetros:
            titulo (str): El título del eBook.
            formato (str): El formato del eBook (e.g., PDF, EPUB).
            tamaño_archivo (float): Tamaño del archivo en MB.
            enlace_descarga (str): Enlace de descarga del eBook.
        """
        super().__init__(titulo, formato, tamaño_archivo)  # Inicialización de la clase base LibroDigital
        self.__enlace_descarga = enlace_descarga  # Atributo privado para el enlace de descarga
    
    def mostrar_info(self):
        """Método sobrescrito para mostrar la información completa del eBook, incluyendo el enlace de descarga."""
        info_basica = super().mostrar_info()  # Llama al método de la clase padre
        return f"{info_basica}, Enlace de Descarga: {self.__enlace_descarga}"

# -------------------------------
# Función para interactuar con el usuario
# -------------------------------

def ingresar_ebook():
    """
    Función que permite al usuario ingresar los datos de un eBook.
    """
    titulo = input("\nIngresa el título del eBook: ")
    formato = input("Ingresa el formato del eBook (e.g., PDF, EPUB): ")
    while True:
        try:
            tamaño_archivo = float(input("Ingresa el tamaño del archivo en MB: "))
            break
        except ValueError:
            print("Valor no válido. Ingresa un número decimal.")
    enlace_descarga = input("Ingresa el enlace de descarga del eBook: ")
    
    ebook = EBook(titulo, formato, tamaño_archivo, enlace_descarga)
    print(f"\nInformación del eBook:\n")
    print(f"{ebook.mostrar_info()}")
# -------------------------------
# Llamada al menú de interacción para el desafío 3
# -------------------------------

ingresar_ebook()











