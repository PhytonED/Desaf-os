#Objetivo: Escribir un programa que, utilizando valores predefinidos, calcule el área de un rectángulo y presente los resultados de manera amigable utilizando texto.
#Descripción:
#Define dos variables numéricas que representen el ancho y el largo de un rectángulo.
#Define variables de tipo string que contengan texto explicativo sobre lo que hace el programa.
#Calcula el área del rectángulo (ancho x largo).
#Utiliza tanto variables numéricas como de texto para presentar el resultado de una manera que sea fácil de entender para alguien que no está viendo el código.

largo = 10
ancho = 4
area = largo*ancho
print("Este programa calcula el área de un rectángulo con valores predefinidos")
linea1 = str("La base (largo) del rectángulo es: ")
linea2 = str("La altura (ancho) del rectángulo es: ")
linea3 = str("El Área del rectángulo es: ")
print(str(linea1) + str(largo))
print(str(linea2) + str(ancho))
print(str(linea3) + str(area))