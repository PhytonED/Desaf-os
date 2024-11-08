#TEMA 3.8 - Desafío 1:
# Crea una función que tome una lista de números y devuelva la suma y el promedio de esos números.
# Autor: Eliana Dalfolo

def suma_y_promedio(lista):
    """
    Esta función recibe una lista de números y devuelve la suma y el promedio de esos números.
    """
    # Calcular la suma de los números en la lista
    suma = sum(lista)  # 'sum' es una función incorporada en Python que devuelve la suma de los elementos de la lista.
    
    # Calcular el promedio
    promedio = suma / len(lista)  # El promedio se obtiene dividiendo la suma entre la cantidad de elementos en la lista.
    
    # Retornar los resultados como una tupla (suma, promedio)
    return suma, promedio  # Se devuelve la suma y el promedio como una tupla, que es una estructura que puede contener varios valores.

# Función para permitir la entrada de números por parte del usuario
def ingresar_numeros():
    while True:
        try:
            # Pedir al usuario que ingrese una lista de números separados por comas
            entrada = input("\nIngrese una lista de números separados por comas (ej. 1, 2, 3): ")
            
            # Convertir la entrada en una lista de cadenas
            lista_str = entrada.split(",")
            
            # Intentar convertir las cadenas a números (enteros o flotantes)
            lista_numeros = [float(x.strip()) for x in lista_str]  # 'strip()' elimina los espacios extra alrededor de cada número
            
            # Si todo salió bien, salir del bucle
            break
        except ValueError:
            # Si ocurre un error (por ejemplo, el usuario no ingresa un número válido), mostrar un mensaje y volver a intentarlo
            print("\nError: Todos los valores deben ser números. Intente nuevamente.")
    
    return lista_numeros

# --- Ejemplo de uso de la función ---
numeros = ingresar_numeros()  # Pedir al usuario que ingrese una lista de números
resultado = suma_y_promedio(numeros)  # Llamar a la función pasando la lista de números

# Mostrar el resultado
print("\nSuma:", resultado[0])  # Mostrar la primera parte de la tupla: la suma
print("\nPromedio:", resultado[1])  # Mostrar la segunda parte de la tupla: el promedio
