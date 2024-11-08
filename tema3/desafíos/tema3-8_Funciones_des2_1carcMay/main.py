# Tema 3-8 Funciones
# Desafío 2:
# Diseña una función que tome una cadena y devuelva la misma cadena, pero con el primer carácter de cada palabra en mayúsculas.
# Autor: Eliana Dalfolo

def capitalizar_palabras(cadena):
    """
    Esta función recibe una cadena de texto y devuelve la misma cadena, pero con la primera letra de cada palabra en mayúsculas.
    """
    # Utilizamos el método 'split()' para dividir la cadena en una lista de palabras
    palabras = cadena.split()
    
    # Capitalizamos la primera letra de cada palabra usando una comprensión de lista y el método 'capitalize()'
    palabras_capitalizadas = [palabra.capitalize() for palabra in palabras]
    
    # Unimos las palabras capitalizadas nuevamente en una cadena con 'join()'
    resultado = ' '.join(palabras_capitalizadas)
    
    return resultado  # Retornamos la cadena resultante

# Ejemplo de uso de la función
cadena = input("\nIngrese una cadena de texto: ")  # Pedimos al usuario que ingrese una cadena de texto
cadena_modificada = capitalizar_palabras(cadena)  # Llamamos a la función para capitalizar las palabras
print("Tu cadena modificada:", cadena_modificada)  # Mostramos el resultado
