# 3_9_Recursividad
# **Desafío 2:**
# Utiliza el modulo creado _procesador_texto_ para resaltar recursivamente todas las ocurrencias de una palabra clave en un texto largo.
# Autor: Eliana Dalfolo

# _procesador_texto.py

def resaltar_palabra_clave(texto, palabra_clave):
    """
    Función recursiva que resalta todas las ocurrencias de la palabra clave en el texto.
    La palabra clave será resaltada en mayúsculas.

    Parámetros:
    texto (str): El texto completo donde buscar y resaltar la palabra clave.
    palabra_clave (str): La palabra clave que se desea resaltar.

    Retorna:
    str: El texto con las ocurrencias de la palabra clave resaltadas en mayúsculas.
    
    - texto.find(palabra_clave) busca la primera aparición de la palabra clave en el texto. Si no se encuentra, retorna -1, lo cual termina la recursión.
    """
    # Buscar la posición de la primera ocurrencia de la palabra clave en el texto
    posicion = texto.find(palabra_clave)
    
    # Caso base: Si no se encuentra más la palabra clave, devolvemos el texto tal como está
    if posicion == -1:
        return texto
    
    # Resaltamos la palabra clave convirtiéndola a mayúsculas
    texto_resaltado = texto[:posicion] + texto[posicion:posicion + len(palabra_clave)].upper() + texto[posicion + len(palabra_clave):]

    # Llamada recursiva para buscar la siguiente ocurrencia de la palabra clave
    return resaltar_palabra_clave(texto_resaltado, palabra_clave)
