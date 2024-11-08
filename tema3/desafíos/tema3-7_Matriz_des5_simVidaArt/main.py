'''
# Desafío 5: Crear una simulación de "vida artificial" en un tablero de juego (matriz)
En este desafío, implementarás una simulación del famoso Juego de la vida de Conway. 
Se trata de un autómata celular desarrollado por el matemático británico John Horton Conway en 1970. 
Es un juego de cero jugadores, lo que significa que su evolución se determina por su estado inicial, sin necesidad de más entradas humanas.

### Objetivos del Desafío
Crear el Tablero de Juego:
Implementa una función para crear un tablero de juego de dimensiones n x m, donde cada celda puede estar viva (1) o muerta (0). 
Inicializa el tablero con un patrón inicial.

### Definir las Reglas del Juego:
Cada celda en el tablero tiene 8 vecinos. Las reglas para la evolución del estado de las celdas son:
Una celda viva con menos de dos celdas vecinas vivas muere por subpoblación.
Una celda viva con dos o tres celdas vecinas vivas sigue viva en la siguiente generación.
Una celda viva con más de tres celdas vecinas vivas muere por sobrepoblación.
Una celda muerta con exactamente tres celdas vecinas vivas se convierte en una celda viva por reproducción.

### Simular la Evolución:
Implementa una función para actualizar el tablero siguiendo las reglas del juego. Esta función debería generar la nueva configuración del tablero después de un número específico de iteraciones.

### Visualizar la Simulación:
Utiliza Matplotlib para visualizar la evolución del tablero a lo largo de las iteraciones. Muestra cada estado del tablero como una imagen en una animación.

APORTE:
# ax: Es el objeto de los ejes (Axes) en Matplotlib. Es donde se dibujan los gráficos o imágenes
# La función set_xticks() establece las posiciones de las marcas del eje x en el gráfico. 
# Si le pasas una lista vacía [], estás indicando que no deseas que aparezcan marcas en el eje x.
# set_yticks() es igual pero para el eje y
'''
# Autor: Eliana Dalfolo

# Importar librerías necesarias
import numpy as np  # Librería para crear y manipular matrices (tableros)
import matplotlib.pyplot as plt  # Librería para visualizar gráficos
from matplotlib.animation import FuncAnimation  # Librería para crear animaciones (si se necesita)

# --- Crear el tablero de juego ---
def crear_tablero(n, m):
    """
    Esta función crea un tablero de tamaño n x m con valores aleatorios entre 0 y 1.
    0 representa una celda muerta, y 1 representa una celda viva.
    """
    return np.random.randint(2, size=(n, m))  # Devuelve una matriz de n x m con valores aleatorios de 0 o 1

# --- Actualizar el tablero según las reglas del Juego de la Vida ---
def actualizar_tablero(tablero):
    """
    Esta función recibe el tablero actual y genera el tablero actualizado
    aplicando las reglas del Juego de la Vida de Conway.
    """
    n, m = tablero.shape  # Obtener las dimensiones del tablero
    nuevo_tablero = np.copy(tablero)  # Hacer una copia del tablero para modificarla

    # Recorrer cada celda del tablero
    for i in range(n):
        for j in range(m):
            # Contar las celdas vecinas vivas alrededor de la celda actual
            vecinos_vivos = 0
            for x in range(i-1, i+2):  # Recorrer filas vecinas
                for y in range(j-1, j+2):  # Recorrer columnas vecinas
                    # Asegurarse de no contar la celda misma
                    if (x != i or y != j) and 0 <= x < n and 0 <= y < m:
                        vecinos_vivos += tablero[x][y]  # Sumar las celdas vecinas vivas

            # Aplicar las reglas del Juego de la Vida
            if tablero[i][j] == 1:  # Si la celda está viva
                if vecinos_vivos < 2 or vecinos_vivos > 3:  # Subpoblación o sobrepoblación
                    nuevo_tablero[i][j] = 0  # La celda muere
            elif tablero[i][j] == 0:  # Si la celda está muerta
                if vecinos_vivos == 3:  # Reproducción
                    nuevo_tablero[i][j] = 1  # La celda revive

    return nuevo_tablero  # Retorna el tablero actualizado

# --- Visualizar el tablero con Matplotlib ---
def visualizar_tablero(tablero):
    """
    Esta función muestra el tablero actual utilizando Matplotlib.
    El tablero es visualizado como una imagen en blanco y negro.
    """
    fig, ax = plt.subplots()  # Crear una figura y un eje para la visualización
    ax.imshow(tablero, cmap="binary")  # Mostrar el tablero usando un mapa de colores binario (0=negro, 1=blanco)
    ax.set_xticks([])  # Ocultar las etiquetas del eje X
    ax.set_yticks([])  # Ocultar las etiquetas del eje Y
    plt.show()  # Mostrar la imagen

# --- Función principal para ejecutar el Juego de la Vida ---
def juego_vida():
    """
    Esta es la función principal donde se solicita la entrada del usuario
    para las dimensiones del tablero y el número de iteraciones. Luego,
    se ejecuta la simulación durante las iteraciones solicitadas.
    """
    # Solicitar al usuario las dimensiones del tablero (número de filas y columnas)
    n = int(input("Ingrese el número de filas del tablero: "))  # Pedir el número de filas
    m = int(input("Ingrese el número de columnas del tablero: "))  # Pedir el número de columnas
    
    # Solicitar al usuario el número de iteraciones
    iteraciones = int(input("Ingrese el número de iteraciones: "))  # Pedir el número de iteraciones
    
    # Crear el tablero inicial con valores aleatorios (0 o 1)
    tablero = crear_tablero(n, m)
    
    # Ejecutar las iteraciones del juego
    for _ in range(iteraciones):
        visualizar_tablero(tablero)  # Mostrar el tablero en cada iteración
        tablero = actualizar_tablero(tablero)  # Actualizar el tablero según las reglas del Juego de la Vida

# --- Ejecutar el Juego de la Vida ---
juego_vida()  # Llamar a la función principal para iniciar la simulación
