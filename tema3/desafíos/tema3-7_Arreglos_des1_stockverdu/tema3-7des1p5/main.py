# Tema 3 - Desafío 1p5: Gestión del Stock de la Verdulería
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
# Ahora recibes un envío de nuevos productos: "frutillas", "apio" y "papas".
"""

# **Pregunta 5: ¿Cómo verificas si las "papas" están ahora en el inventario?**

print("El inventario de productos es:\n")
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
print("¿Las papas están en el inventario?", "papas" in inventario)
