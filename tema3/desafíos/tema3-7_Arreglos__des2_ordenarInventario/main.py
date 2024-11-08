# Tema 3 - Desafío 2: Ordenar el Inventario de Libros
# Objetivo: Ordenar una lista de libros en orden decreciente de sus códigos de identificación sin modificar la lista original.
# Autor: Eliana Dalfolo

# Importamos la biblioteca array para crear un arreglo de códigos de libros
from array import array

# Creamos un arreglo con los códigos de libros en la biblioteca
libros = array('i', [345, 129, 672, 219, 500])  # 'i' indica enteros en el arreglo

# 1. Utilizamos sorted() para obtener una copia ordenada en orden decreciente
# Esto no modifica el arreglo original
libros_ordenados = array('i', sorted(libros, reverse=True))

# 2. Imprimimos el arreglo original para verificar que no se ha modificado
print("Arreglo original de códigos:", libros)

# 3. Imprimimos el arreglo ordenado en orden decreciente
print("Arreglo ordenado en orden decreciente:", libros_ordenados)


"""
RESPUESTAS 
    
1. ¿Por qué es importante no modificar el arreglo original?

Tener el arreglo original sin modificar es importante por si deseamos volver a usarlo con los datos originales.

2. ¿Por qué no puedo usar el método sort() sobre el arreglo original?

El método sort() no está disponible para los objetos de tipo array en Python. 
Además, sort() ordena en su lugar, lo que alteraría los datos originales. 
Con sorted(), generamos una copia del contenido, por lo que podemos tener el arreglo original y mostrar otra copia con los datos ordenados
"""