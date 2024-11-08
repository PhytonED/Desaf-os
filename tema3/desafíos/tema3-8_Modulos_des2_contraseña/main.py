# Tema 3-8 Módulos
# **Desafío 2:**
# Utiliza el módulo `random` de Python para crear un programa que genere una contraseña aleatoria de 8 caracteres que incluya letras minúsculas, letras mayúsculas y números.
# Autor Eliana Dalfolo

# Importamos el módulo random para generar la contraseña aleatoria
import random  # El módulo random permite realizar operaciones aleatorias, como seleccionar caracteres al azar.
import string  # El módulo string nos da acceso a secuencias de caracteres predefinidos (letras y dígitos)

# Función para generar una contraseña aleatoria
def generar_contraseña():
    """
    Esta función genera una contraseña aleatoria de 8 caracteres.
    La contraseña incluirá letras minúsculas, mayúsculas y números.
    """
    
    # Definir los caracteres posibles para la contraseña
    caracteres_posibles = string.ascii_lowercase + string.ascii_uppercase + string.digits
    # 'string.ascii_lowercase' son las letras minúsculas (a-z)
    # 'string.ascii_uppercase' son las letras mayúsculas (A-Z)
    # 'string.digits' son los números (0-9)
    # Se concatenan todas estas secuencias para formar una lista de caracteres disponibles para la contraseña.

    # Usamos random.choice() para seleccionar aleatoriamente 8 caracteres de los posibles
    contraseña = ''.join(random.choice(caracteres_posibles) for _ in range(8))
    # random.choice(caracteres_posibles): Elige aleatoriamente un carácter de los posibles caracteres en cada iteración.
    # for _ in range(8): Repite el proceso 8 veces para generar una contraseña de 8 caracteres.
    # ''.join(...): Convierte la lista de caracteres generados en una cadena de texto.

    return contraseña  # Retorna la contraseña generada

# Llamar a la función y generar la contraseña aleatoria
contraseña_generada = generar_contraseña()  # Llamamos a la función que devuelve una contraseña aleatoria.

# Mostrar la contraseña generada
print("\nContraseña generada:", contraseña_generada)
# Imprime la contraseña generada para que el usuario la vea.
