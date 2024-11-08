# Tema 3 - Desafío 1p8: Gestión del Stock de la Verdulería
# Objetivo: Realizar varias operaciones sobre un inventario de frutas y verduras.
# Autor: Eliana Dalfolo

"""
¡Bienvenido al desafío de la verdulería! 
Has sido nombrado el nuevo gerente de una tienda de frutas, verduras y hortalizas. 
Tu tarea será manejar el stock de la tienda utilizando un arreglo. 
Aquí hay una serie de tareas que tendrás que completar.

# Inventario inicial
#Aquí está el inventario inicial de la tienda:
#inventario = ["manzanas", "bananas", "zanahorias", "espinacas", "brocoli", "cebolla", "kiwis"]
"""
"""
# Gestión del inventario
# Un nuevo empleado viene y necesita una copia del inventario para poder reponer los estantes.
"""

# **Pregunta 8: ¿Cómo proporcionarías una copia del inventario al nuevo empleado, asegurándote de que si el empleado hace cambios en su copia, el inventario original no se vea afectado?**

# === Código de ejercicios de preguntas anteriores

print("\nEl inventario de productos es:\n")
inventario = ["manzanas", "bananas", "zanahorias", "espinacas", "brócoli", "cebolla","kiwis"] 
print(inventario)# muestro el inventario inicial.
agregar = ["frutillas", "apio", "papas"]
print("\nSe agregarán los siguientes productos: \n")# elimino el producto indicando la posición del producto en el inventario.
print(agregar)
inventario.extend(["frutillas", "apio", "papas"])
print("\nEl inventario con los productos agregados es:\n")
print(inventario)# muestro el inventario nuevamente para ver que el producto fue eliminado.
print("\nEl inventario ordenado alfabéticamente tras agregarse productos es:\n")
inventario.sort()# ordeno el inventario en forma alfabética.
print(inventario)


# Decido tener en el inventario 7 productos
if len(inventario) > 7:
    # Eliminamos el último producto para hacer espacio
    producto_eliminado = inventario.pop()
    print("\nProducto eliminado para hacer espacio para dragonfruit:", producto_eliminado)

# Agregamos el "dragonfruit" al inventario
inventario.append("dragonfruit")

# Mostramos el inventario actualizado
print("\nInventario después de agregar dragonfruit:", inventario)

# === Código de la pregunta 7

# Ordenamos el inventario alfabéticamente
inventario.sort()

# Mostramos el inventario ordenado
print("\nInventario ordenado alfabéticamente:", inventario)

# Código pregunta 8 

# Hacemos una copia independiente del inventario
copia_inventario = inventario.copy()

# Mostramos la copia del inventario
print("\nCopia del inventario para el nuevo empleado:", copia_inventario)

# Si el empleado hace cambios en la copia, el inventario original no se verá afectado
copia_inventario.append("dragonfruit")  # Agregamos un producto solo a la copia

# Mostramos los resultados
print("\nCopia del inventario después de la modificación:", copia_inventario)
print("\nInventario original después de la modificación en la copia:", inventario)

