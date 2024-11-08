import numpy as bn  # Usamos bn como alias para numpy
from os import system # Para limpiar la consola

# Función para limpiar la consola en caso de que se ejecute en otro sistema operativo.
'''def clear_screen():
   os.system('cls' if os.name == 'nt' else 'clear')

clear_screen() '''

system("clear")

# Crea una matriz de tamano dado con barcos colocados aleatoriamente.

def crear_tablero(fc=5, barcos=3): # fc = filas y columnas, barcos = cantidad de barcos
    tablero = bn.zeros((fc, fc), dtype=int) # Crea una matriz de ceros de tamaño fc x fc
    fila = bn.random.randint(fc, size=barcos) # Genera filas aleatorias para colocar los barcos
    columna = bn.random.randint(fc, size=barcos) # Genera columnas aleatorias para colocar los barcos
    tablero[fila, columna] = 1 # Coloca los barcos en el tablero
    return tablero # Retorna el tablero con los barcos colocados


# Cuenta los barcos hundidos en el tablero (donde el valor es 0).
def barco_hundido(tablero): # tablero = tablero con los barcos colocados
    return bn.sum(tablero == 0)  # Consideramos el valor 0 para los barcos hundidos

# Muestra el tablero en formato de matriz.
def tablero_visible(tablero): # tablero = tablero con los barcos colocados
    print("\n-- Tablero --\n") 
    for fila in tablero: # Recorre cada fila del tablero
        print("  ".join(map(str, fila))) # Convierte cada elemento de la fila en una cadena y los une con espacios

# Procesa el tiro y actualiza el tablero.
def tirar_bomba(tablero, fila, columna, valor_hundido, valor_marca): # tablero = tablero con los barcos colocados
    if tablero[fila, columna] == 1: # Si hay un barco en la posición (fila, columna)
        tablero[fila, columna] = valor_marca # Marca la posición con el valor deseado
        print("\n¡Hundido!") 
        return True # Retorna True para indicar que se hundió un barco    
    print("\nAgua")
    return False # Retorna False para indicar que no se hundió ningún barco

# Solicita y valida las coordenadas del jugador o permite salir con 'x'.
def ingresar_coordenadas(jugador): # jugador = nombre del jugador

    while True: #
        # Solicitar coordenadas de la fila
        datof = input(f"\nJugador {jugador} --> Ingrese fila (0-4) o 'x' para salir: ") 
        if datof.lower() == 'x': # Si el jugador ingresa 'x' o 'X'lo pasa a minúsculas. 
            print("\nAbandonando partida...")
            input("Presiona Enter para continuar...") # Pausa la ejecución hasta que el usuario presione Enter.
            system("clear") # Limpia la pantalla.
            return None  # Retorna None para indicar que se quiere salir del juego.
        if datof < '0' or datof > '4': # Si los datos ingresados no son válidos.
            print("\nEntrada inválida. Ingrese un número entero entre 0 y 4 o 'x' para salir.")
            continue # Vuelve al inicio del bucle.
        fila = int(datof) # Convierte la entrada a un número entero.

        # Solicitar coordenadas de la columna
        datoc = input(f"\nJugador {jugador} --> Ingrese columna (0-4) o 'x' para salir: ") 
        if datoc.lower() == 'x':
            print("\nAbandonando partida...")
            input("Presiona Enter para continuar...")
            system("clear")
            return None 
        if datoc < '0' or datoc> '4': 
            print("\nEntrada inválida. Ingrese un número entero entre 0 y 4 o 'x' para salir.")
            continue
        columna = int(datoc) # Convierte la entrada a un número entero.
        return fila, columna # Retorna las coordenadas ingresadas por el jugador.

# Función principal para jugar de a un solo jugador.
def jugar_un_jugador(menu_letra): # menu_letra = letra del menú 'p'(secreta) o 'j'
    tablero = crear_tablero() 
    barcos_hundidos_contador = 0 # Contador de barcos hundidos.

    while barcos_hundidos_contador < 3: # Mientras no se hundan todos los barcos.
        if menu_letra == 'p': # Si el jugador eligió la opción de jugar de a un solo jugador.
            tablero_visible(tablero)
        coordenadas = ingresar_coordenadas("1") # Solicita las coordenadas al jugador 1.
        if coordenadas is None:
            return # Retorna None para indicar que se quiere salir del juego.
        fila, columna = coordenadas # Asigna las coordenadas ingresadas a las variables fila y columna.
        if tirar_bomba(tablero, fila, columna, 1, 0): # Llama a la función tirar_bomba para hacer el tiro.
            barcos_hundidos_contador += 1 # Incrementa el contador de barcos hundidos. 
        if barcos_hundidos_contador == 3: # Si se hundieron todos los barcos.
           
            print("\n¡HAS GANADO!!!\n")
            input("Presiona Enter para continuar...")
            system("clear")
            break # Sale del bucle while.

# Función para jugar de a dos jugadores.
def jugar_dos_jugadores():
    tablero = crear_tablero()  # Crea un tablero nuevo
    barcos_totales = 3  # Número total de barcos en el juego para cada jugador

    # Inicializa contadores de barcos hundidos para cada jugador
    barcos_hundidos_jugador1 = 0
    barcos_hundidos_jugador2 = 0

    while True:
    # El tablero solamente se muestra para fines de prueba.
        # tablero_visible(tablero)

        # Turno del Jugador 1
        print("\nTurno del Jugador 1:")
        coordenadas = ingresar_coordenadas("1")
        if coordenadas is None:  # Si el jugador ingresa 'x' o 'X'
            Menu()  # Vuelve al menú principal
            return  # Termina la función y sale del juego
        fila, columna = coordenadas
        if tirar_bomba(tablero, fila, columna, 1, 9):
            barcos_hundidos_jugador1 += 1  # Incrementa el contador de barcos hundidos del Jugador 1
            if barcos_hundidos_jugador1 > 1 <= barcos_totales:  # Si el Jugador 1 ha hundido todos los barcos
                print("\n¡Jugador 1 ha ganado!")
                input("Presiona Enter para continuar...")
                system("clear")
                Menu()
                return  # Vuelve al menú

        # Turno del Jugador 2
        print("\nTurno del Jugador 2:")
        coordenadas = ingresar_coordenadas("2")
        if coordenadas is None:  # Si el jugador ingresa 'x' o 'X'
            Menu()  # Vuelve al menú principal
            return  # Termina la función y sale del juego
        fila, columna = coordenadas
        if tirar_bomba(tablero, fila, columna, 1, 5):
            barcos_hundidos_jugador2 += 1  # Incrementa el contador de barcos hundidos del Jugador 2
            if barcos_hundidos_jugador2 > 1 <= barcos_totales:  # Si el Jugador 2 ha hundido todos los barcos
                print("\n¡Jugador 2 ha ganado!")
                input("Presiona Enter para continuar...")
                system("clear")
                Menu()
                return  # Vuelve al menú

# Muestra el menú principal y maneja la selección del usuario.
def Menu():
    while True:
        print("-------------------------------------------")
        print("------------  /BATALLA NAVAL/  ------------")
        print("-------------------------------------------")
        print("")  # p - Practicar | 1 jugador (oculta), tablero visible.
        print("j - Jugar | 1 jugador ") # jugar con tablero no visible.
        print("b - Jugar | 2 jugadores ") # jugar con tablero no visible.
        print("x - Salir")
        menu_letra = input("\nIngrese opción: ")
        system("clear")

        if menu_letra in ('p', 'j'): 
            jugar_un_jugador(menu_letra)
        elif menu_letra == 'b':
            jugar_dos_jugadores()
        elif menu_letra == 'x':
            print("\nGracias por jugar.")
            input("Presiona Enter para continuar...")
            system("clear")
            break
        else:
            print("\n¡¡Ingrese una opción válida!!\n")
            input("Presiona Enter para continuar...")
            system("clear")
Menu()

