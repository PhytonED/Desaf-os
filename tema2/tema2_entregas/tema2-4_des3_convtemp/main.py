# Desafío 3: Convertidor de temperaturas
# Realizar conversiones de una temperatura dada en Celsius a Fahrenheit y Kelvin utilizando operaciones directas sobre las variables. Los cálculos se realizarán directamente al asignar los valores a las variables.

#Autor: Eliana Dalfolo

# Conversión:
# De Celsius a Fahrenheit: se multiplica por 1.8 y se suma 32. 
# De Celsius a Kelvin: se suma 273.15

# Explica de qué trata el programa. \n permite hacer salto de línea.

print("Este programa solicita que el usuario ingrese una temperatura en Celsius (°C) para ser convertida a Fahrenheit (°F) y a Kelvin (°K). El separador decimal es el (.)\n")

# Solicito al usuario que ingrese el valor de la temperatura en Celsius.
# La función float() convierte el valor ingresado en un número punto flotante.
# La función input() permite que el usuario ingrese un valor desde la consola.
# La función print() muestra el valor de la variable en la consola. 
# Los valores ingresados por el usuario se almacenan en la variable Celsius.

# Procedimiento:
# 1. Se ingresa la temperatura con o sin valores decimales.
# 2. Se realiza la conversión a Fahrenheit y se muestra el resultado.
# 3. Se realiza la conversión a Kelvin y se muestra el resultado.

Celsius = float(input("Ingrese la temperatura en grados Celsius(°C): "))
print("\n **** CONVERSIÓN ****")
Fahrenheit = (Celsius * 1.8) + 32
print("\n El valor en grados Fahrenheit es:", Fahrenheit, "°F")
Kelvin = Celsius + 273.15
print("\n El valor en grados Kelvin es:", Kelvin, "°K")


