# Tema 3-8 Módulos
# **Desafío 4: Utiliza el módulo `collections` para analizar un texto y generar estadísticas avanzadas, como las 10 palabras más comunes y su frecuencia. 
# Extiende esto creando un gráfico de barras con matplotlib para visualizar la frecuencia de las palabras.
# Autor Eliana Dalfolo

'''
Aspectos a destacar

- re: Usado para trabajar con expresiones regulares, lo utilizamos aquí para limpiar el texto de caracteres no deseados (como puntuación o números).
re.sub(r'[^a-zA-Z\s]', '', texto): Elimina todos los caracteres que no sean letras del alfabeto (tanto mayúsculas como minúsculas) ni espacios, usando una expresión regular.
- zip(*palabras_comunes): Desempaqueta la lista de tuplas palabras_comunes en dos listas separadas: una de palabras y otra de frecuencias.
- plt.bar(palabras, frecuencias): Crea un gráfico de barras donde el eje X es para las palabras y el eje Y para las frecuencias.
- plt.xticks(rotation=45): Rota las etiquetas del eje X para mejorar su legibilidad.
- plt.show(): Muestra el gráfico generado.
'''


# Importar los módulos necesarios
from collections import Counter  # Importamos Counter, una clase de collections que cuenta las ocurrencias de los elementos en una lista.
import matplotlib.pyplot as plt  # Importamos matplotlib para crear gráficos. Específicamente, plt es utilizado para crear gráficos de barras.
import re  # Importamos el módulo de expresiones regulares (re) para limpiar el texto de caracteres no deseados como signos de puntuación.

# Función para procesar el texto y contar las palabras
def analizar_texto(texto):
    """
    Esta función toma un texto, lo limpia, cuenta la frecuencia de las palabras y devuelve las 10 más comunes.
    """
    # Limpiar el texto: eliminar caracteres no alfabéticos y convertirlo a minúsculas.
    texto = re.sub(r'[^a-zA-Z\s]', '', texto)  # Utilizamos una expresión regular para eliminar todo lo que no sea letras o espacios. El 'r' indica que la cadena es una expresión regular.
    texto = texto.lower()  # Convertimos todo el texto a minúsculas para evitar que palabras en mayúsculas y minúsculas se cuenten como diferentes.

    # Separar el texto en palabras
    palabras = texto.split()  # split() divide el texto en una lista de palabras, usando los espacios como delimitadores.

    # Contar la frecuencia de las palabras
    contador_palabras = Counter(palabras)  # Creamos un objeto Counter, que cuenta la frecuencia de cada palabra en la lista 'palabras'.
    
    # Obtener las 10 palabras más comunes
    palabras_comunes = contador_palabras.most_common(10)  # most_common(10) devuelve las 10 palabras más frecuentes junto con su frecuencia.

    return palabras_comunes  # Retorna las 10 palabras más comunes y su frecuencia.

# Solicitar al usuario que ingrese un texto
texto_usuario = input("Ingresa un texto para analizar: ")  # Utilizamos input() para pedir al usuario que ingrese un texto. Este texto será procesado por nuestra función.

# Llamar a la función para analizar el texto ingresado
palabras_comunes = analizar_texto(texto_usuario)  # Llamamos a la función 'analizar_texto' pasando el texto ingresado por el usuario.

# Mostrar las 10 palabras más comunes y su frecuencia
print("Las 10 palabras más comunes y su frecuencia son:")  # Imprimimos un mensaje para indicar que a continuación se mostrarán las palabras más comunes.
for palabra, frecuencia in palabras_comunes:  # Iteramos sobre la lista 'palabras_comunes', que contiene tuplas con la palabra y su frecuencia.
    print(f"{palabra}: {frecuencia}")  # Para cada palabra y frecuencia, imprimimos la palabra y su número de ocurrencias en el texto.

# Generar un gráfico de barras para visualizar la frecuencia de las palabras
def graficar_frecuencia(palabras_comunes):
    """
    Esta función toma las 10 palabras más comunes y genera un gráfico de barras para mostrar su frecuencia.
    """
    # Desempaquetar las palabras y sus frecuencias
    palabras, frecuencias = zip(*palabras_comunes)  # zip(*palabras_comunes) desempaqueta la lista de tuplas en dos listas separadas: una de palabras y otra de frecuencias.

    # Crear el gráfico de barras
    plt.bar(palabras, frecuencias)  # plt.bar() crea el gráfico de barras. Las palabras se muestran en el eje X y las frecuencias en el eje Y.
    
    # Añadir título y etiquetas a los ejes
    plt.title('Frecuencia de las 10 palabras más comunes')  # Añadimos un título al gráfico.
    plt.xlabel('Palabras')  # Etiqueta para el eje X, que mostrará las palabras.
    plt.ylabel('Frecuencia')  # Etiqueta para el eje Y, que mostrará la cantidad de veces que cada palabra aparece.

    # Rotar las etiquetas del eje X para mejorar la legibilidad
    plt.xticks(rotation=45)  # Rotamos las etiquetas del eje X 45 grados para evitar que se sobrepongan.

    # Mostrar el gráfico
    plt.show()  # Finalmente, mostramos el gráfico en la pantalla.

# Llamar a la función para graficar las palabras más comunes y su frecuencia
graficar_frecuencia(palabras_comunes)  # Llamamos a la función graficar_frecuencia y le pasamos las 10 palabras más comunes obtenidas.
