# tema4_10_TAD
# Título: Sistema de Gestión de Biblioteca con Entidades Interconectadas
# Autora: Eliana D
# Descripción: Este código muestra un sistema de gestión de biblioteca utilizando TADs para libros, usuarios, préstamos y multas. Los datos son ingresados por el usuario, y las entidades se gestionan de forma interconectada.

'''
Clase Libro: Esta clase representa a los libros en el sistema. Cada libro tiene un título, autor e ISBN.
Clase Usuario: Los usuarios tienen nombre, ID único y una lista de libros prestados. Los métodos prestar_libro y devolver_libro gestionan los préstamos de los libros.
Clase Prestamo: Maneja la información relacionada con el préstamo de un libro, incluyendo el libro prestado, el usuario, y las fechas de préstamo y devolución.
Clase Multa: Representa una multa generada cuando un libro no es devuelto a tiempo. Incluye el usuario, el monto de la multa y el motivo.
Función gestionar_biblioteca: Permite interactuar con el sistema ingresando datos como los libros, usuarios y generando los préstamos y multas. Las entradas se toman del usuario y se procesan para gestionar el sistema de forma interconectada.
'''

# Clase Libro
class Libro:
    """Clase que representa un libro en la biblioteca."""
    def __init__(self, titulo, autor, isbn):
        """
        Inicializa un libro con su título, autor y ISBN.
        :param titulo: Título del libro.
        :param autor: Autor del libro.
        :param isbn: Número de ISBN del libro.
        """
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn

# Clase Usuario
class Usuario:
    """Clase que representa a un usuario de la biblioteca."""
    def __init__(self, nombre, id_usuario):
        """
        Inicializa un usuario con nombre e ID.
        :param nombre: Nombre del usuario.
        :param id_usuario: ID único del usuario.
        """
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista de libros prestados por el usuario

    def prestar_libro(self, libro):
        """Método para prestar un libro al usuario."""
        self.libros_prestados.append(libro)
    
    def devolver_libro(self, libro):
        """Método para devolver un libro prestado por el usuario."""
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)
        else:
            print(f"El libro {libro.titulo} no fue prestado a {self.nombre}")

# Clase Prestamo
class Prestamo:
    """Clase que representa un préstamo de un libro."""
    def __init__(self, libro, usuario, fecha_prestamo, fecha_devolucion):
        """
        Inicializa un préstamo con libro, usuario, fecha de préstamo y fecha de devolución.
        :param libro: El libro prestado.
        :param usuario: El usuario que realiza el préstamo.
        :param fecha_prestamo: Fecha en que se realiza el préstamo.
        :param fecha_devolucion: Fecha límite para la devolución.
        """
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion

# Clase Multa
class Multa:
    """Clase que representa una multa por atraso en la devolución de un libro."""
    def __init__(self, usuario, monto, motivo):
        """
        Inicializa una multa con usuario, monto y motivo.
        :param usuario: El usuario multado.
        :param monto: Monto de la multa.
        :param motivo: Motivo de la multa.
        """
        self.usuario = usuario
        self.monto = monto
        self.motivo = motivo

# Función principal para interactuar con el sistema
def gestionar_biblioteca():
    """
    Función que gestiona la interacción con el sistema de biblioteca.
    Permite al usuario agregar libros, registrar usuarios, prestar libros, y generar multas.
    """
    # Ingreso de libros
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    isbn = input("Ingrese el ISBN del libro: ")
    libro = Libro(titulo, autor, isbn)  # Crear un libro con los datos ingresados

    # Ingreso de usuario
    nombre_usuario = input("Ingrese el nombre del usuario: ")
    id_usuario = input("Ingrese el ID del usuario: ")
    usuario = Usuario(nombre_usuario, id_usuario)  # Crear un usuario con los datos ingresados

    # Realizar préstamo
    usuario.prestar_libro(libro)  # El usuario toma el libro prestado

    # Verificación de retorno
    if libro in usuario.libros_prestados:
        print(f"El libro '{libro.titulo}' ha sido prestado a {usuario.nombre}.")
    
    # Generar multa si no se devuelve a tiempo
    fecha_actual = input("Ingrese la fecha actual (dd-mm-aaaa): ")  # Simulación de fecha actual
    fecha_devolucion = input("Ingrese la fecha de devolución (dd-mm-aaaa): ")
    
    if fecha_actual > fecha_devolucion:
        monto_multa = float(input("Ingrese el monto de la multa: "))
        motivo = input("Ingrese el motivo de la multa: ")
        multa = Multa(usuario, monto_multa, motivo)  # Crear una multa por atraso
        print(f"Se ha generado una multa de {multa.monto} a {usuario.nombre} por: {multa.motivo}.")
    else:
        print("No se ha generado multa, la devolución fue a tiempo.")

# Ejecución del sistema
gestionar_biblioteca()  # Ejecutamos la función para gestionar el sistema de biblioteca
