# Tema 3-8 FUNCIONES
# Desafío 5: Palíndromo
# Crea una función llamada es_palindromo que tome una una cadena y devuelva true si es palindromo o false si no lo es.
# Autor: Eliana Dalfolo

def es_palindromo(cadena):
    """
    Esta función recibe una cadena de texto y devuelve True si la cadena es un palíndromo,
    y False si no lo es. 
    Se ignoran los espacios y se considera insensible a mayúsculas.
    """
    # Eliminamos los espacios de la cadena y convertimos todo a minúsculas para hacer la comparación insensible a mayúsculas
    cadena_limpia = cadena.replace(" ", "").lower()

    # Comparamos la cadena limpia con su reverso
    return cadena_limpia == cadena_limpia[::-1]

# Ejemplo de uso de la función
cadena = input("\nIngrese una cadena para verificar si es un palíndromo: ")  # Pedimos al usuario que ingrese una cadena
if es_palindromo(cadena):  # Llamamos a la función es_palindromo para verificar la cadena
    print("\nLa cadena es un palíndromo.")
else:
    print("La cadena no es un palíndromo.\n")
