# 4_12_Clases_y_objetos
### Desafío 5: Desarrolla una función que reciba una lista de objetos Autor y devuelva el autor que ha escrito el mayor número de libros.
# Utiliza el encapsulamiento para acceder a la información necesaria de cada objeto Autor.
# Autor: Eliana Dalfolo

'''
Encapsulamiento: 
Los libros de cada autor están almacenados en una lista privada (__libros). 
Se accede a la cantidad de libros sólo a través del método contar_libros().

Autor con Más Libros: 
La función autor_con_mas_libros recibe la lista de autores y compara el número de libros de cada autor usando contar_libros(). 
Devuelve el autor con el mayor número de libros.
'''

# Clase Libro: representa un libro con título, género e ISBN
class Libro:
    def __init__(self, titulo, genero, isbn):
        # Inicializa el título, género e ISBN del libro
        self.titulo = titulo
        self.genero = genero
        self.isbn = isbn

# Clase Autor: representa un autor con su nombre y una lista de libros
class Autor:
    def __init__(self, nombre):
        # Inicializa el nombre del autor
        self.nombre = nombre
        # Inicializa una lista privada para almacenar los libros del autor
        self.__libros = []

    def agregar_libro(self, libro):
        """Método para agregar un libro a la lista de libros del autor."""
        # Agrega el libro a la lista privada de libros
        self.__libros.append(libro)

    def contar_libros(self):
        """Método que devuelve la cantidad de libros escritos por el autor."""
        # Retorna la cantidad de libros en la lista privada
        return len(self.__libros)

    def obtener_nombre(self):
        """Método que devuelve el nombre del autor."""
        # Retorna el nombre del autor
        return self.nombre

# Función para encontrar el autor con el mayor número de libros
def autor_con_mas_libros(lista_autores):
    """Recibe una lista de objetos Autor y devuelve el autor con mayor cantidad de libros."""
    # Si la lista de autores está vacía, retorna None
    if not lista_autores:
        return None

    # Inicializa el primer autor como el que tiene más libros
    autor_max = lista_autores[0]
    # Obtiene la cantidad de libros del primer autor
    max_libros = autor_max.contar_libros()
    
    # Recorre cada autor en la lista para comparar el número de libros
    for autor in lista_autores[1:]:
        # Obtiene el número de libros del autor actual
        num_libros = autor.contar_libros()
        # Si el autor actual tiene más libros que el máximo encontrado
        if num_libros > max_libros:
            # Actualiza el autor con más libros y la cantidad máxima
            autor_max = autor
            max_libros = num_libros

    # Retorna el autor con la mayor cantidad de libros
    return autor_max

# Código principal

# Lista para almacenar objetos Autor
lista_autores = []

# Ciclo del menú principal
while True:
    # Muestra el menú al usuario
    print("\n--- Menú ---")
    print("1. Ingresar datos de un nuevo autor y sus libros")
    print("2. Mostrar autor con el mayor número de libros")
    print("3. Salir")
    
    # Solicita la opción del usuario
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        # Solicita el nombre del autor
        nombre_autor = input("\nIngrese el nombre del autor: ")
        
        # Crea un nuevo objeto Autor con el nombre ingresado
        autor = Autor(nombre_autor)
        
        # Ciclo para ingresar libros del autor
        while True:
            # Solicita el título del libro o permite salir
            titulo = input(f"\nIngrese el título del libro de {nombre_autor} (o 's' para salir): ")
            if titulo.lower() == 's':
                break
            # Solicita el género del libro
            genero = input("Ingrese el género del libro: ")
            # Solicita el ISBN del libro
            isbn = input("Ingrese el ISBN del libro: ")
            
            # Crea un objeto Libro con los datos ingresados
            libro = Libro(titulo, genero, isbn)
            # Agrega el libro a la lista de libros del autor
            autor.agregar_libro(libro)
            print(f"\nEl libro '{titulo}' ha sido agregado al autor {nombre_autor}.\n")
        
        # Agrega el autor a la lista de autores
        lista_autores.append(autor)
    
    elif opcion == "2":
        # Llama a la función para encontrar el autor con más libros
        autor_mayor = autor_con_mas_libros(lista_autores)
        
        # Muestra el resultado si hay al menos un autor
        if autor_mayor:
            print(f"\nEl autor con más libros es: {autor_mayor.obtener_nombre()}")
        else:
            print("\nNo hay autores registrados.")
    
    elif opcion == "3":
        # Opción para salir del programa
        print("\nSaliendo del programa. ¡Hasta luego!")
        break
    
    else:
        # Mensaje de error en caso de opción inválida
        print("Opción no válida. Por favor, seleccione nuevamente.")






















































































