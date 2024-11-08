# Tema 3-8 Módulos
# **Desafio 1:**
# Investiga y utiliza al menos tres funciones del módulo `string` 
# que puedan ser útiles para mejorar nuestro procesador de texto.
# Autor Eliana Dalfolo

'''
FUNCIONES que decidí probar
- string.ascii_letters: Devuelve una cadena con todas las letras del alfabeto en minúsculas y mayúsculas.
- string.punctuation: Devuelve una cadena con todos los signos de puntuación.
- string.whitespace: Devuelve una cadena con todos los caracteres de espacio en blanco.

Otros 
texto.lower(): Convierte todas las letras del texto a minúsculas.
texto.replace(" ", ""): Elimina todos los espacios en el texto.
texto.isalpha(): Verifica si todos los caracteres en el texto son letras del alfabeto, lo que puede ayudar a validar la entrada del usuario.
'''

# Importamos el módulo string para acceder a las funciones y constantes útiles
import string

# Función para limpiar el texto eliminando caracteres no alfabéticos
def limpiar_texto(texto):
    """
    Elimina todos los caracteres que no sean letras o espacios.
    """
    # Usamos string.ascii_letters para obtener las letras y string.whitespace para los espacios
    caracteres_validos = string.ascii_letters + string.whitespace

    # Filtramos el texto para mantener solo los caracteres válidos
    texto_limpio = ''.join([caracter for caracter in texto if caracter in caracteres_validos])
    
    return texto_limpio

# Función para contar los signos de puntuación en un texto
def contar_puntuacion(texto):
    """
    Cuenta cuántos signos de puntuación están presentes en el texto.
    """
    # Usamos string.punctuation para obtener todos los signos de puntuación
    puntuaciones = string.punctuation

    # Contamos cuántos caracteres del texto son signos de puntuación
    contador_puntuacion = sum(1 for caracter in texto if caracter in puntuaciones)
    
    return contador_puntuacion

# Función para verificar si un texto contiene solo letras
def es_alfabetico(texto):
    """
    Verifica si el texto contiene solo letras (sin números ni símbolos).
    """
    # Comprobamos si el texto contiene solo letras usando string.ascii_letters
    return all(caracter in string.ascii_letters for caracter in texto)

# Pedir al usuario que ingrese el texto de prueba
texto_prueba = input("\nIngresa el texto: ")

# Limpiar el texto (eliminar puntuaciones y caracteres no alfabéticos)
texto_limpio = limpiar_texto(texto_prueba)
print(f"\nTexto limpio: {texto_limpio}")

# Contar los signos de puntuación en el texto
puntuacion = contar_puntuacion(texto_prueba)
print(f"\nCantidad de signos de puntuación: {puntuacion}")

# Verificar si el texto solo contiene letras
es_alfabetico_resultado = es_alfabetico(texto_prueba)
print(f"\n¿El texto solo contiene letras? {es_alfabetico_resultado}")
