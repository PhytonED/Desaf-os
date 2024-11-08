# Tema 3 - Desafío 1p3: Gestión del Stock de la Verdulería
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
# Un cliente viene y compra todas las bananas.
"""
# **Pregunta 3: ¿Cómo actualizarías el inventario después de la venta?**

#---------- Elimino el producto banana --------
#1. Indicando posición del elemento a eliminar: pop()
print("   ------------------------------------------")
print("\nSe eliminará el producto del inventario usanado pop()\n")
print("   ------------------------------------------")
print("El inventario de productos es:\n")
inventario = ["manzanas", "bananas", "zanahorias", "espinacas", "brócoli", "cebolla","kiwis"] 
print(inventario)# muestro el inventario inicial.
print("\nSe eliminará el producto: ", inventario.pop(1))# elimino el producto indicando la posición del producto en el inventario.
print("\nEl inventario sin el productos es:\n")
print(inventario)# muestro el inventario nuevamente para ver que el producto fue eliminado.
print("\nEl inventario ordenado alfabéticamente tras eliminarse productos es:\n")
inventario.sort()# ordeno el inventario en forma alfabética.
print(inventario)
#2. Indicando el nombre del elemento a eliminar: remove()
print("   ------------------------------------------")
print("\nSe eliminará el producto del inventario usanado remove()\n")
print("   ------------------------------------------")
print("El inventario de productos es:\n")
inventario = ["manzanas", "bananas", "zanahorias", "espinacas", "brócoli", "cebolla","kiwis"] 
print(inventario)# muestro el inventario inicial
print("\nSe eliminará el producto:",inventario[1])
inventario.remove("bananas")# elimino el producto indicando el nombre del producto.
print("\nEl inventario sin el productos es:\n")
print(inventario)# muestro el inventario nuevamente para ver que el producto fue eliminado.
print("\nEl inventario ordenado alfabéticamente tras eliminarse productos es:\n")
inventario.sort()# ordeno el inventario en forma alfabética.
print(inventario)

