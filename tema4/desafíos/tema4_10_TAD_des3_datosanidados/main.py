# tema4_10_TAD 
# Título: Sistema de Inventario para una Cadena de Tiendas
# Autora: Eliana D
# Descripción: Este código maneja un sistema de inventario para una cadena de tiendas, donde cada tienda tiene productos, empleados y transacciones. Utiliza estructuras de datos anidadas para gestionar las relaciones entre estas entidades.

'''
Clase Producto: Representa un producto en la tienda con su nombre, precio y cantidad disponible. El método vender gestiona la venta de un producto, disminuyendo su cantidad disponible.
Clase Tienda: Representa una tienda que contiene productos y empleados. Los métodos agregar_producto y agregar_empleado permiten añadir elementos a la tienda.
Función gestionar_inventario: Permite agregar productos y empleados a una tienda, así como gestionar las ventas. Los productos se venden reduciendo la cantidad disponible en la tienda.
'''

class Producto:
    """Clase que representa un producto en el inventario."""
    def __init__(self, nombre, precio, cantidad):
        """
        Inicializa un producto con nombre, precio y cantidad disponible.
        :param nombre: Nombre del producto.
        :param precio: Precio del producto.
        :param cantidad: Cantidad disponible del producto.
        """
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def vender(self, cantidad):
        """Método para vender una cantidad de un producto."""
        if cantidad <= self.cantidad:
            self.cantidad -= cantidad
            print(f"Se han vendido {cantidad} unidades de {self.nombre}.")
        else:
            print("Cantidad insuficiente para vender.")

class Tienda:
    """Clase que representa una tienda con productos y empleados."""
    def __init__(self, nombre, productos, empleados):
        """
        Inicializa una tienda con nombre, productos y empleados.
        :param nombre: Nombre de la tienda.
        :param productos: Lista de productos disponibles en la tienda.
        :param empleados: Lista de empleados que trabajan en la tienda.
        """
        self.nombre = nombre
        self.productos = productos  # Lista de objetos Producto
        self.empleados = empleados  # Lista de empleados

    def agregar_producto(self, producto):
        """Método para agregar un producto a la tienda."""
        self.productos.append(producto)

    def agregar_empleado(self, empleado):
        """Método para agregar un empleado a la tienda."""
        self.empleados.append(empleado)

# Función principal para gestionar el inventario
def gestionar_inventario():
    """
    Función que gestiona el inventario, permite vender productos y registrar transacciones.
    """
    nombre_tienda = input("Ingrese el nombre de la tienda: ")
    productos = []
    empleados = []

    # Ingreso de productos
    num_productos = int(input("¿Cuántos productos desea agregar a la tienda? "))
    for _ in range(num_productos):
        nombre_producto = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad disponible del producto: "))
        producto = Producto(nombre_producto, precio, cantidad)
        productos.append(producto)

    # Ingreso de empleados
    num_empleados = int(input("¿Cuántos empleados tiene la tienda? "))
    for _ in range(num_empleados):
        nombre_empleado = input("Ingrese el nombre del empleado: ")
        empleados.append(nombre_empleado)

    # Crear la tienda
    tienda = Tienda(nombre_tienda, productos, empleados)

    # Vender productos
    producto_vender = input("¿Qué producto desea vender? ")
    cantidad_vender = int(input("¿Cuántas unidades desea vender? "))
    
    for producto in tienda.productos:
        if producto.nombre == producto_vender:
            producto.vender(cantidad_vender)
            break
    else:
        print("Producto no encontrado en la tienda.")

# Ejecución del sistema
gestionar_inventario()  # Ejecutamos la función para gestionar el inventario
