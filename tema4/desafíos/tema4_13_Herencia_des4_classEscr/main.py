#4_13_Herencia
### Desafío 4: Implementa una clase EscritorAcademico que herede de Escritor y Academico,
# e incluya un método adicional para publicar artículos académicos. 
# Asegúrate de utilizar correctamente la función super() para inicializar las clases base.
# Autor: Eliana Dalfolo

'''
Clase Escritor: Define atributos comunes a los escritores, como nombre.
Clase Academico: Incluye atributos académicos específicos como institución.
Clase que hereda (EscritorAcademico): 
Hereda de ambas clases para representar un escritor académico, y utiliza super() para inicializar las clases base, lo cual facilita la administración de herencia múltiple y asegura que ambos constructores se inicialicen adecuadamente.
'''
# -------------------------------
# Clase Escritor como parte de la herencia múltiple
# -------------------------------

class Escritor:
    """
    Clase que representa a un escritor.
    """
    
    def __init__(self, nombre):
        """
        Constructor de la clase Escritor.
        
        Parámetros:
            nombre (str): El nombre del escritor.
        """
        self.nombre = nombre  # Atributo público para el nombre del escritor
    
    def obtener_nombre(self):
        """Método para obtener el nombre del escritor."""
        return self.nombre

# -------------------------------
# Clase Academico como parte de la herencia múltiple
# -------------------------------

class Academico:
    """
    Clase que representa a un académico.
    """
    
    def __init__(self, institucion):
        """
        Constructor de la clase Academico.
        
        Parámetros:
            institucion (str): La institución a la que pertenece el académico.
        """
        self.institucion = institucion  # Atributo público para la institución
    
    def obtener_institucion(self):
        """Método para obtener la institución del académico."""
        return self.institucion

# -------------------------------
# Clase EscritorAcademico que hereda de Escritor y Academico
# -------------------------------

class EscritorAcademico(Escritor, Academico):
    """
    Clase que representa a un escritor académico, derivada de Escritor y Academico.
    Incluye un método adicional para publicar artículos académicos.
    """
    
    def __init__(self, nombre, institucion):
        """
        Constructor de la clase EscritorAcademico.
        
        Parámetros:
            nombre (str): El nombre del escritor académico.
            institucion (str): La institución académica a la que pertenece.
        """
        # Inicialización de las clases base utilizando super()
        super().__init__(nombre)
        Academico.__init__(self, institucion)  # También inicializa la clase Academico
    
    def publicar_articulo(self, titulo_articulo):
        """
        Método para publicar un artículo académico.
        
        Parámetros:
            titulo_articulo (str): El título del artículo académico.
            
        Retorna:
            str: Mensaje que confirma la publicación del artículo.
        """
        return f"{self.nombre} ha publicado un artículo titulado '{titulo_articulo}' en {self.institucion}."

# -------------------------------
# Función para interactuar con el usuario
# -------------------------------

def ingresar_escritor_academico():
    """
    Función que permite al usuario ingresar los datos de un escritor académico y un artículo.
    """
    nombre = input("\nIngresa el nombre del escritor académico: ")
    institucion = input("Ingresa la institución del académico: ")
    escritor_academico = EscritorAcademico(nombre, institucion)  # Crear instancia de EscritorAcademico
    
    while True:
        titulo_articulo = input("Ingresa el título del artículo académico: ")
        print(escritor_academico.publicar_articulo(titulo_articulo))  # Publica el artículo
        
        # Confirmar si el usuario desea ingresar otro artículo
        continuar = input("\n¿Deseas ingresar otro artículo? (s/n): ")
        if continuar.lower() == 'n':
            break

# -------------------------------
# Llamada al menú de interacción para el desafío 4
# -------------------------------

ingresar_escritor_academico()
