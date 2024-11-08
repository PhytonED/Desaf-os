"""Desafío 2: Mejora del Cálculo del Promedio
Toma el ejemplo del cálculo del promedio de calificaciones y mejóralo. En lugar de pedir las calificaciones
una por una, modifica el código para pedir todas las calificaciones al mismo tiempo (el estudiante puede
ingresar las calificaciones separadas por comas) y luego calcular el promedio.

Autor: Eliana Dalfolo

Se solicita al usuario que ingrese:
- los valores numéricos correspondientes a las calificaciones. Deberán ser valores comprendidos entre 1 y 12 pudiendo ser decimales.
- La función input() permite que el usuario ingrese los valores solicitados desde la consola.
- \n permite hacer salto de línea.
- Se imprimirán los resultados en la consola utilizando la función print() y función f-string (f"").
  - {} 
   -- si usamos la función f-strings, sirven para colocar en su interior la variable."""

# Explica de qué trata el programa.
print("***** Calculamos promedio de calificaciones *****\n")

print("Este programa solicita al usuario que ingrese las calificaciones separadas por "," y luego calcula el promedio.")

"""Los números introducidos son de tipo string, por lo que se debe convertir a tipo int o float. Dado que las calificaciones a ingresar pueden ser decimales, uso float."""

contador_calificaciones = 0
suma_calificaciones = 0

# Pido al usuario que ingrese las calificaciones separadas por ´,´.

while True:
    calificaciones = input("\nIngrese una calificación entre 1 y 12. Para terminar de ingresar ingrese 0 : ")    
    lista = calificaciones.split(',')
    for i in lista:
        califica = float(i)
        if califica < 1 or califica > 12:
            print("\nLa calificación debe estar entre 1 y 12. Inténtalo de nuevo.")
            exit()# Reinicio el bucle si se ingresa un valor fuera del rango.

        suma_calificaciones += califica
        contador_calificaciones += 1
        promedio = suma_calificaciones / contador_calificaciones

# Imprimo los resultados en la pantalla.
    print(f"\n=============== *****  RESULTADOS  ***** =============== ")
    print(f"El promedio de las calificaciones es: {promedio}")
 
