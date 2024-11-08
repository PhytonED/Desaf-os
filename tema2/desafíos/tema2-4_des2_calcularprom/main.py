# Desafío 2: Calcular promedio
# Crear un programa que lea 5 calificaciones y calcule su promedio.
# Autor: Eliana Dalfolo

# Tema 2 - Desafío 2: Calcular Promedio
# Objetivo: Leer 5 calificaciones ingresadas por el usuario y calcular su promedio.

# Inicializamos una variable para la suma de las calificaciones
suma_calificaciones = 0

# Pedimos al usuario que ingrese 5 calificaciones y las sumamos
for i in range(5):
    calificacion = float(input(f"Ingrese la calificación {i + 1}: "))
    suma_calificaciones += calificacion

# Calculamos el promedio dividiendo la suma total entre 5
promedio = suma_calificaciones / 5

# Mostramos el promedio
print("El promedio de las calificaciones es:", promedio)






























