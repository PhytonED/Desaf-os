# 2_4_Tipos_de_datos_y_operadores
# Desafío 2: Calcular promedio
# Crear un programa que lea un número variable de calificaciones y calcule su promedio.
# Autor: Eliana Dalfolo

# Solicita al usuario la cantidad de calificaciones que desea ingresar
cantidad_calificaciones = int(input("\nIngrese la cantidad de calificaciones a promediar: "))

# Inicializa la suma de calificaciones y un contador para llevar el conteo
suma_calificaciones = 0.0
contador = 0

# Bucle `while` para pedir cada calificación de forma individual
while contador < cantidad_calificaciones:
    # Solicita cada calificación y la convierte a flotante
    calificacion = float(input(f"Ingrese la calificación {contador + 1}: "))
    # Suma la calificación a la acumuladora
    suma_calificaciones += calificacion
    # Incrementa el contador para pasar a la siguiente calificación
    contador += 1

# Calcula el promedio dividiendo la suma total entre la cantidad de calificaciones ingresadas
promedio = suma_calificaciones / cantidad_calificaciones

# Imprime el promedio calculado, formateado a dos decimales
print(f"\nEl promedio de las calificaciones es: {promedio:.2f}")

























