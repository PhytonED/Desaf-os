# 3_9_Recursividad
# **Desafío 1:**
# Crea una función recursiva que calcule el máximo común divisor (MCD) de dos números. El MCD de dos números es el número más grande que puede dividir ambos números sin dejar un residuo. Por ejemplo, el MCD de 8 y 12 es 4.
# Pista: Puedes usar el algoritmo de Euclides, que establece que el MCD de dos números también divide al 
# residuo de su división. Por lo tanto, el MCD de a y b (donde a > b) es el mismo que el MCD de b y a % b.
# Autor: Eliana Dalfolo

'''
Aspectos a destacar
- Algoritmo de Euclides:
- Recursión: La función mcd(a, b) llama a sí misma con los nuevos parámetros 
b y a mod b, 
La recursión continúa hasta que b=0.
- Base de la recursión: El caso base se alcanza cuando b=0, momento en el cual el MCD es simplemente el valor de a.
%: El operador % se utiliza para calcular el residuo de la división, lo que es la clave en el algoritmo de Euclides para reducir los números en cada paso recursivo.
'''

# Función recursiva para calcular el MCD de dos números
def mcd(a, b):
    """
    Calcula el Máximo Común Divisor (MCD) de dos números utilizando el algoritmo de Euclides.
    
    Parámetros:
    a (int): El primer número.
    b (int): El segundo número.
    
    Retorna:
    int: El MCD de a y b.
    """
    # Caso base: si b es 0, el MCD es a
    if b == 0:
        return a
    else:
        # Llamada recursiva: MCD de b y a % b
        return mcd(b, a % b)

# Ejemplo de uso
num1 = int(input("Ingresa el primer número: "))  # Solicita al usuario el primer número.
num2 = int(input("Ingresa el segundo número: "))  # Solicita al usuario el segundo número.

# Llamamos a la función y mostramos el resultado
resultado = mcd(num1, num2)  # Calcula el MCD de num1 y num2.
print(f"El MCD de {num1} y {num2} es: {resultado}")  # Muestra el resultado del MCD.

