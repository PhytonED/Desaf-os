#4_13_Encapsulamiento
### Desafío 3: 
# Implementa la clase Autor con métodos getter y setter 
# utilizando decoradores @property para manejar los atributos privados nombre y nacionalidad.

# Autor: Eliana Dalfolo

# -------------------------------
# Clase Autor con Métodos Getter y Setter usando Decoradores
# -------------------------------

class Autor:
    """
    Clase que representa a un autor con nombre y nacionalidad.
    Utiliza decoradores para los métodos getter y setter.
    """
    
    def __init__(self, nombre, nacionalidad):
        """
        Constructor que inicializa un autor con nombre y nacionalidad.
        
        Parámetros:
            nombre (str): El nombre del autor.
            nacionalidad (str): La nacionalidad del autor.
        """
        self.__nombre = nombre  # Atributo privado para el nombre del autor
        self.__nacionalidad = nacionalidad  # Atributo privado para la nacionalidad del autor

    @property
    def nombre(self):
        """Método getter para obtener el nombre del autor."""
        return self.__nombre  # Devuelve el nombre del autor
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        """Método setter para cambiar el nombre del autor."""
        self.__nombre = nuevo_nombre  # Establece el nuevo nombre
    
    @property
    def nacionalidad(self):
        """Método getter para obtener la nacionalidad del autor."""
        return self.__nacionalidad  # Devuelve la nacionalidad del autor
    
    @nacionalidad.setter
    def nacionalidad(self, nueva_nacionalidad):
        """Método setter para cambiar la nacionalidad del autor."""
        self.__nacionalidad = nueva_nacionalidad  # Establece la nueva nacionalidad

# -------------------------------
# Función para Ingresar Datos del Autor
# -------------------------------

def ingresar_datos_autor():
    """
    Función para que el usuario ingrese los datos del autor.
    
    Retorna un objeto de la clase Autor con el nombre y la nacionalidad proporcionados.
    """
    nombre = input("\nIngresa el nombre del autor: ")  # Solicita el nombre del autor
    nacionalidad = input("Ingresa la nacionalidad del autor: ")  # Solicita la nacionalidad del autor
    return Autor(nombre, nacionalidad)  # Devuelve un objeto Autor con los datos ingresados

# -------------------------------
# Función para Modificar los Datos del Autor
# -------------------------------

def modificar_autor(autor):
    """Función para modificar los datos del autor."""
    print(f"\nAutor actual: {autor.nombre}, Nacionalidad: {autor.nacionalidad}")  # Muestra los datos actuales
    autor.nombre = input("\nIngresa el nuevo nombre del autor: ")  # Modifica el nombre del autor
    autor.nacionalidad = input("Ingresa la nueva nacionalidad del autor: ")  # Modifica la nacionalidad del autor
    print(f"\nDatos actualizados: Autor: {autor.nombre}, Nacionalidad: {autor.nacionalidad}")  # Muestra los datos actualizados

# -------------------------------
# Menú Principal Interactivo
# -------------------------------

def menu_principal():
    """
    Menú principal interactivo para gestionar autores.
    Permite al usuario agregar nuevos autores, modificar datos de autores existentes y salir del programa.
    """
    autores = []  # Lista para almacenar los autores

    while True:
        print("\n--- Menú Principal ---")
        print("1. Agregar un autor")
        print("2. Modificar los datos de un autor")
        print("3. Ver lista de autores")
        print("4. Salir")
        
        opcion = input("\nSelecciona una opción: ").strip()
        
        if opcion == "1":
            autor = ingresar_datos_autor()  # Llama a la función para ingresar un autor
            autores.append(autor)  # Añade el autor a la lista de autores
            print(f"\nAutor '{autor.nombre}' agregado exitosamente.")
        
        elif opcion == "2":
            if autores:  # Si hay autores en la lista
                print("\n--- Lista de Autores ---")
                for i, autor in enumerate(autores, 1):
                    print(f"{i}. {autor.nombre} ({autor.nacionalidad})")  # Muestra los autores disponibles
                try:
                    seleccion = int(input("\nSelecciona el número del autor que deseas modificar: ")) - 1
                    if 0 <= seleccion < len(autores):
                        modificar_autor(autores[seleccion])  # Llama a la función para modificar el autor seleccionado
                    else:
                        print("\nNúmero de autor no válido.")
                except ValueError:
                    print("\nPor favor ingresa un número válido.")
            else:
                print("\nNo hay autores disponibles para modificar.")
        
        elif opcion == "3":
            if autores:  # Si hay autores en la lista
                print("\n--- Lista de Autores ---")
                for autor in autores:
                    print(f"{autor.nombre} ({autor.nacionalidad})")  # Muestra todos los autores
            else:
                print("\nNo hay autores disponibles.")
        
        elif opcion == "4":
            print("Saliendo")
            break  # Sale del programa
        
        else:
            print("\nOpción no válida. Por favor selecciona una opción válida.")

# -------------------------------
# Llamada al Menú Principal
# -------------------------------

menu_principal()  # Ejecuta el menú principal


































































