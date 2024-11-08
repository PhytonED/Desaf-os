# 3_9_Recursividad
# **Desafío 3:**
# Crea una función recursiva que invierta las palabras en una oración 
# sin utilizar funciones incorporadas de Python para invertir cadenas o lista
# Autor: Eliana Dalfolo

def invertir_palabras(oracion):
    """
    Función recursiva que invierte las palabras en una oración.
    
    Parámetros:
    oracion (str): La oración que contiene las palabras a invertir.
    
    Retorna:
    str: La oración con las palabras invertidas.
    
    - Uso de split(" ", 1):
    split(" ", 1) divide la oración en dos partes: la primera palabra y el resto de la oración. 
    Esto asegura que se maneje palabra por palabra.
    """
    # Caso base: Si la oración está vacía o solo contiene un espacio, no hay palabras que invertir
    if not oracion.strip():
        return oracion

    # Encontramos la primera palabra (por espacio)
    palabras = oracion.split(" ", 1)  # Se divide en dos partes: la primera palabra y el resto de la oración

    # Invertir la primera palabra y procesar el resto recursivamente
    return palabras[0] + " " + invertir_palabras(palabras[1]) if len(palabras) > 1 else palabras[0]
