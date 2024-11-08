# Desafío 3: Simulación de una Carrera de Autos
# Vas a simular una carrera de autos. Cada auto tiene una velocidad aleatoria y cada ciclo representa un segundo de la carrera. 
# Autor: Eliana Dalfolo

# Importa el módulo random para generar velocidades aleatorias
import random

# Solicita al usuario la cantidad de autos en la carrera
cantidad_autos = int(input("\nIngrese la cantidad de autos en la carrera: "))

# Inicializa las posiciones de cada auto y las velocidades
# Nota: Usaremos variables individuales para cada auto en lugar de listas o arreglos
auto_1_posicion, auto_2_posicion, auto_3_posicion, auto_4_posicion = 0, 0, 0, 0
auto_1_velocidad = random.randint(10, 20)  # Velocidad aleatoria entre 10 y 20
auto_2_velocidad = random.randint(10, 20)
auto_3_velocidad = random.randint(10, 20)
auto_4_velocidad = random.randint(10, 20)

# Variable para el tiempo de carrera en segundos
segundos_carrera = 10

# Inicia la simulación de la carrera
contador = 0
while contador < segundos_carrera:
    # Cada segundo se suma la velocidad a la posición de cada auto
    auto_1_posicion += auto_1_velocidad
    auto_2_posicion += auto_2_velocidad
    auto_3_posicion += auto_3_velocidad
    auto_4_posicion += auto_4_velocidad
    # Incrementa el contador de tiempo
    contador += 1

# Determina el auto con la mayor posición alcanzada
distancia_maxima = max(auto_1_posicion, auto_2_posicion, auto_3_posicion, auto_4_posicion)

# Muestra el ganador o los autos que empataron en caso de haber más de uno
print("\nResultados finales:")
if auto_1_posicion == distancia_maxima:
    print("Auto 1 ha llegado a la distancia máxima:", auto_1_posicion)
if auto_2_posicion == distancia_maxima:
    print("Auto 2 ha llegado a la distancia máxima:", auto_2_posicion)
if auto_3_posicion == distancia_maxima:
    print("Auto 3 ha llegado a la distancia máxima:", auto_3_posicion)
if auto_4_posicion == distancia_maxima:
    print("Auto 4 ha llegado a la distancia máxima:", auto_4_posicion)
