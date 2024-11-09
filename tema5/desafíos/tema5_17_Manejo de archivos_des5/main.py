# tema5_17_Manejo de archivos
# Número de desafío: 5
# Consigna:
'''
Desarrolla una función que lea un archivo de texto grande, como libros.txt, 
y cuente cuántas veces aparece cada palabra. 
Luego, muestra las 5 palabras más comunes y cuántas veces aparecen.
'''
# Autora: Eliana D


import re
from collections import Counter

def contar_palabras_mas_comunes(archivo):
    try:
        # Abrir el archivo en modo lectura
        with open(archivo, 'r', encoding='utf-8') as f:
            # Leer todo el contenido del archivo
            texto = f.read()
            
            # Limpiar el texto: convertir a minúsculas y extraer solo palabras
            palabras = re.findall(r'\b\w+\b', texto.lower())  # \b\w+\b encuentra las palabras
            
            # Contar las palabras usando Counter
            contador = Counter(palabras)
            
            # Mostrar las 5 palabras más comunes
            print("Las 5 palabras más comunes son:")
            for palabra, cantidad in contador.most_common(5):
                print(f"{palabra}: {cantidad}")
    
    except FileNotFoundError:
        print(f"El archivo '{archivo}' no existe.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Llamar a la función con el nombre del archivo
contar_palabras_mas_comunes('libros.txt')
























