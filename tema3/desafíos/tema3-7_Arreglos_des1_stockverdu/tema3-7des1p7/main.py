# Tema 3 - Desafío 1p7: Gestión del Stock de la Verdulería
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
# Decides que sería más fácil gestionar el inventario si estuviera ordenado alfabéticamente.
"""

# **Pregunta 7: ¿Cómo ordenarías el inventario?**

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
    print("Producto eliminado para hacer espacio para dragonfruit:", producto_eliminado)

# Agregamos el "dragonfruit" al inventario
inventario.append("dragonfruit")

# Mostramos el inventario actualizado
print("Inventario después de agregar dragonfruit:", inventario)

# === Código de la pregunta 7

# Ordenamos el inventario alfabéticamente
inventario.sort()

# Mostramos el inventario ordenado
print("Inventario ordenado alfabéticamente:", inventario)
