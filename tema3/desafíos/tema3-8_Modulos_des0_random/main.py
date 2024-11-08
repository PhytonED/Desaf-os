# Tema 3-8 Módulos
# **Desafio 0:**
# Utiliza el módulo `random` para crear un programa que genere un número aleatorio entre 1 y 100.
# Autor Eliana Dalfolo

# Importamos el módulo random para generar números aleatorios
import random

# Función para generar un número aleatorio entre 1 y 100
def generar_numero_aleatorio():
    """
    Función que genera un número aleatorio entre 1 y 100 usando el módulo random.
    """
    numero = random.randint(1, 100)  # Generamos el número aleatorio
    return numero  # Devolvemos el número generado

# Ejecutamos la función y mostramos el número aleatorio
numero_generado = generar_numero_aleatorio()  # Llamamos a la función para generar el número
print(f"El número aleatorio generado es: {numero_generado}")  # Mostramos el número generado












