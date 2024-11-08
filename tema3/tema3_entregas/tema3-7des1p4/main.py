# Tema 3 - Desafío 1p4: Gestión del Stock de la Verdulería
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

# **Pregunta 4: ¿Cómo añadirías estos productos al inventario?**

#---------- Agrego productos  --------
#1. Agrego productos de forma individual: append()
print("\n   ------------------------------------------")
print("\nSe agregarán productos al inventario usanado append()\n")
print("   ------------------------------------------\n")
print("El inventario de productos es:\n")
inventario = ["manzanas", "bananas", "zanahorias", "espinacas", "brócoli", "cebolla","kiwis"] 
print(inventario)# muestro el inventario inicial.
agregar = ["frutillas", "apio", "papas"]
print("\nSe agregarán los siguientes productos: \n")# elimino el producto indicando la posición del producto en el inventario.
print(agregar)
inventario.append("frutillas") 
inventario.append("apio")
inventario.append("papas")
print("\nEl inventario con los productos agregados es:\n")
print(inventario)# muestro el inventario nuevamente para ver que el producto fue eliminado.
print("\nEl inventario ordenado alfabéticamente tras agregarse productos es:\n")
inventario.sort()# ordeno el inventario en forma alfabética.
print(inventario)
#2. Agrego varios productos: extend()
print("\n   ------------------------------------------")
print("\nSe agregarán productos al inventario usanado extend()\n")
print("   ------------------------------------------\n")
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


