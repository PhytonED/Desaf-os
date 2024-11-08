#Objetivo: Determinar si un número dado es múltiplo de 2, 3, 5, 7, 9, 10, y 11 utilizando comparaciones y operadores lógicos.
#Descripción: Crea un programa que, dado un número, verifique si es múltiplo de los números mencionados. Para cada uno de estos números, el programa debe indicar si el número dado es o no un múltiplo de estos.

#Autor: Eliana Dalfolo
# Creo variables para cada divisor para que si se desea modificar, se haga en las variables y no a lo largo de todo el código.

# Variables con los divisores.
m1 = 2
m2 = 3
m3 = 5
m4 = 7
m5 = 9
m6 = 10
m7 = 11

# Explica de qué trata el programa. \n permite hacer salto de línea
print("Este programa te solicita que ingreses un número entero y te permite determinar si el mismo es múltiplo de 2, 3, 5, 7, 9, 10 y 11 \n")

# Se solicita al usuario que ingrese un número entero.
# La función int() convierte el valor ingresado en un número entero.
# La función input() permite que el usuario ingrese un valor desde la consola.
# La función print() muestra el valor de la variable en la consola. 
# Los valores ingresados por el usuario se almacenan en la variable num.
# Procedimiento:
# 1. Se realiza una división entre el número ingresado y los divisores usando el operador (/) -> devuelve el resultado en número real.
# 2. Se realiza una división entre el número ingresado y los divisores usando el operador (//) -> devuelve la parte entera del resultado.
# 3. Se realiza una comparación entre el resultado en número real y el de la parte entera. 
# 4. Si el resultado en número real es > al de la parte entera, entonces el número no es múltiplo (no son valores justos).

num = int(input("Ingresa un número entero para indicar si es múltiplo: "))
print("\n")
if (num / m1 > num // m1):
    print(num,"NO es múltiplo de", m1,"\n")
else:
    print(num,"SÍ es múltiplo de", m1,"\n")
if (num / m2 > num // m2):
  print(num,"NO es múltiplo de", m2,"\n")
else:
  print(num,"SÍ es múltiplo de", m2,"\n")
if (num / m3 > num // m3):
  print(num,"NO es múltiplo de", m3,"\n")
else:
  print(num,"SÍ es múltiplo de", m3,"\n")
if (num / m4 > num // m4):
  print(num,"NO es múltiplo de", m4,"\n")
else:
  print(num,"SÍ es múltiplo de", m4,"\n")
if (num / m5 > num // m5):
  print(num,"NO es múltiplo de", m5,"\n")
else:
  print(num,"SÍ es múltiplo de", m5,"\n")
if (num / m6 > num // m6):
  print(num,"NO es múltiplo de", m6,"\n")
else:
  print(num,"SÍ es múltiplo de", m6,"\n")
if (num / m7 > num // m7):
  print(num,"NO es múltiplo de", m7,"\n")
else:
  print(num,"SÍ es múltiplo de", m7,"\n")