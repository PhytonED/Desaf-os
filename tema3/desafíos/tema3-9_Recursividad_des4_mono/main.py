# 3_9_Recursividad
# **Desafío 4:**
'''
Imagina que tenemos un mono que intenta contar plátanos. Sin embargo, nuestro mono es un poco distraído y olvida cuántos plátanos ha contado cada vez que empieza a contar de nuevo. Cada vez que termina una secuencia de conteo, se olvida de los plátanos contados antes y vuelve a empezar, sumando todos desde el principio. Implementa una función recursiva que simule cómo el mono cuenta plátanos.
Reglas:
- El mono puede contar un plátano a la vez.
- Cada vez que el mono termina de contar una pila de plátanos, tiene que volver a contar desde cero, pero sigue acumulando el total.
Por ejemplo:
- Si el mono tiene 5 plátanos en la pila, contará uno por uno, luego olvida y vuelve a empezar, acumulando la suma.
'''
# Autor: Eliana Dalfolo

# contar_platanos.py

def contar_platanos(cantidad_platanos, total_acumulado=0):
    """
    Función recursiva que simula cómo el mono cuenta los plátanos. Cada vez que empieza una nueva secuencia de conteo,
    el mono olvida lo contado antes, pero acumula el total.

    Parámetros:
    cantidad_platanos (int): La cantidad de plátanos en la pila que el mono cuenta.
    total_acumulado (int): El total acumulado de plátanos contados hasta el momento.

    Retorna:
    int: El total acumulado de plátanos después de contar la pila actual.
    """
    # Caso base: Si no hay más plátanos, devolvemos el total acumulado
    if cantidad_platanos == 0:
        return total_acumulado
    
    # El mono cuenta un plátano, luego se olvida y vuelve a contar desde cero.
    return contar_platanos(cantidad_platanos - 1, total_acumulado + 1)
