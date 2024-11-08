# Desafío 4: Control de Notas de Estudiantes
# Como profesor, necesitas manejar las notas de tus estudiantes. Permite ingresar todas las notas de los estudiantes y realiza varias operaciones con esos datos.
#**Pregunta 1: Calcula el promedio de las notas de la clase. ¿Cómo lo harías?**
#**Pregunta 2: Encuentra la nota más baja y la más alta. ¿Cómo lo harías?**
#**Pregunta 3: Identifica la nota que más se repite. ¿Cómo lo harías?**
#_Nota:_ La función Counter es útil porque simplifica el conteo de elementos en una lista, permitiendo identificar rápidamente la frecuencia de cada nota.
#**Pregunta 4 (Plus): Realiza un gráfico de barras con las notas. ¿Cómo lo harías?**
#_Nota:_ La biblioteca matplotlib.pyplot es útil porque proporciona funciones fáciles de usar para crear visualizaciones de datos, como gráficos de barras, que pueden ayudar a visualizar la distribución de las notas de manera clara y comprensible.
# Autor: Eliana Dalfolo

# Tema: Control de Notas de Estudiantes
# Desafío 4: Control de Notas de Estudiantes con cálculo de promedio, mínima, máxima y visualización de datos

# Importamos las bibliotecas necesarias
from collections import Counter  # Para contar la frecuencia de cada nota fácilmente
import matplotlib.pyplot as plt  # Para la visualización de datos en gráficos

# Lista para almacenar las notas de los estudiantes
notas = []  # Inicializamos una lista vacía para almacenar las notas

# Pedimos al usuario la cantidad de estudiantes
cantidad_estudiantes = int(input("\nIngrese la cantidad de estudiantes: "))  # Solicita el número de estudiantes

# Ingresamos las notas de los estudiantes
for i in range(cantidad_estudiantes):  # Itera el número de estudiantes
    nota = float(input(f"\nIngrese la nota del estudiante {i + 1}: "))  # Solicita la nota de cada estudiante
    notas.append(nota)  # Agrega la nota a la lista 'notas'

# Pregunta 1: Calcular el promedio de las notas
suma_notas = sum(notas)  # Suma todas las notas usando sum()
promedio = suma_notas / len(notas)  # Calcula el promedio
print(f"\nEl promedio de la clase es: {promedio:.2f}")  # Muestra el promedio con dos decimales

# Pregunta 2: Encontrar la nota más baja y la más alta
nota_minima = min(notas)  # Encuentra la nota mínima usando min()
nota_maxima = max(notas)  # Encuentra la nota máxima usando max()
print(f"\nLa nota más baja es: {nota_minima}")  # Muestra la nota mínima
print(f"\nLa nota más alta es: {nota_maxima}")  # Muestra la nota máxima

# Pregunta 3: Identificar la nota que más se repite usando Counter
conteo_notas = Counter(notas)  # Cuenta la frecuencia de cada nota en la lista
nota_mas_repetida, max_frecuencia = conteo_notas.most_common(1)[0]  # Obtiene la nota más común y su frecuencia
print(f"\nLa nota que más se repite es: {nota_mas_repetida} (repetida {max_frecuencia} veces)")

# Pregunta 4 (Plus): Realizar un gráfico de barras con las notas usando matplotlib.pyplot
plt.bar(conteo_notas.keys(), conteo_notas.values(), color='skyblue')  # Crea el gráfico de barras con notas y frecuencias
plt.xlabel('Notas')  # Etiqueta del eje X
plt.ylabel('Frecuencia')  # Etiqueta del eje Y
plt.title('Distribución de Notas')  # Título del gráfico
plt.show()  # Muestra el gráfico de barras

