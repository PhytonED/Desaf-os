"""Objetivo: 
Desafío 1: Calificaciones Aprobatorias y Desaprobatorias.
Al analizar las calificaciones de los estudiantes quieres saber cuántos aprobaron y cuántos desaprobaron. Se considera que una calificación de 7 o superior es aprobatoria y cualquier calificación menor a 7 es desaprobatoria. Utiliza lo que aprendiste sobre bucles y condicionales para resolver este problema.

Autor: Eliana Dalfolo

Se solicita al usuario que ingrese:
- los valores numéricos correspondientes a las calificaciones. Deberán ser valores comprendidos entre 1 y 12 pudiendo ser decimales.
- La función input() permite que el usuario ingrese los valores solicitados desde la consola.
- \n permite hacer salto de línea.
- Con los valores ingresados se realizarán operaciones lógicas para analizar si:
   * calificación => calificación ingresada como mínima aprobatoria, es aprobatoria. En la letra dada sería 7 o superior 
  * calificación < calificación ingresada como mínima aprobatoria, es desaprobatoria.

- Se imprimirán los resultados en la consola utilizando la función print() y función f-string (f"").
  - {} 
   -- si usamos la función f-strings, sirven para colocar en su interior la variable."""

# Explica de qué trata el programa.
print("***** Calificaciones Aprobatorias y Desaprobatorias *****\n")

print("Este programa solicita al usuario que ingrese la calificación mínima de aprobación y luego las calificaciones. Cuenta las de aprobación (mayor o igual a la calificación ingresada como mínima aprobatoria) y desaprobación (menores a la calificación ingresada como mínima aprobatoria).\n\nNo hay límites de ingresos y para dar finalización a los mismos se debe ingresar el valor 0 (cero).")

'''Los números introducidos son de tipo string, por lo que se debe convertir a tipo int o float. Dado que las calificaciones a ingresar pueden ser decimales, uso float.'''

# Inicializo las variables que contarán las calificaciones aprobatorias y desaprobatorias.
aprobado = 0 
desaprobado = 0
minimo_aprobacion = float(input("\nIngrese la calificación mínima de aprobación: ")) 

# Pido al usuario que ingrese las calificaciones.

while True: # Se ejecuta el bloque de código hasta que se cumpla la condición de salida.
    calificacion = float(input("\nIngrese una calificación (entre 1 y 12) o 0 para terminar: "))  
    
    if calificacion == 0:
      break # Salgo del bucle porque se cumplie con la condición de terminación.
    
    if calificacion < 1 or calificacion > 12:
      print("\nLa calificación debe estar entre 1 y 12. Inténtalo de nuevo.")
      continue # Reinicio el bucle si se ingresa un valor fuera del rango.
    
    if calificacion >= minimo_aprobacion: #Si la calificación es mayor o igual al mínimo de aprobación, se cuenta como aprobada de lo contrario se cuenta como desaprobada.
      aprobado += 1
    else: 
      desaprobado += 1
      
# Imprimo los resultados en la pantalla.
print(f"\n=============== *****  RESULTADOS  ***** =============== ")
print(f"\nAprobaron {aprobado} estudiantes y desaprobaron {desaprobado} estudiantes.")



  



