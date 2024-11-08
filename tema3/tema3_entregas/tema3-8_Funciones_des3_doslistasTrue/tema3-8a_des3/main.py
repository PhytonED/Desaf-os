'''
Desafío 3:
Construye una función que tome dos listas y devuelva True si tienen al menos un elemento en común, de lo contrario, que devuelva False.

#Autor: Eliana Dalfolo
'''
'''
Además de cumplir con lo solicitado, me muestra la cantidad de elementos en común y cuáles son.
'''

# Función que compara las dos listas
# Devuelve TRUE si tienen al menos un elemento en común, o FALSE si no.
def comparar_listas(lista1, lista2):
    encontrado = False  # Variable que indica si se encontró al menos un elemento en común
    elementos_en_comun = []  # Lista de elementos en común
    cantidad = 0  # Cantidad de elementos en común inicializada en 0
    for elemento in lista1:  # Recorre la primera lista
        if elemento in lista2:  # Si el elemento está en la segunda lista
            # Si el elemento no está en la lista de elementos en común
            if elemento not in elementos_en_comun:
                encontrado = True  # Se encontró al menos un elemento en común
                cantidad += 1  # Se incrementa la cantidad de elementos en común
                # Se agrega el elemento a la lista de elementos en común
                elementos_en_comun.append(elemento)
                # Devuelve la tupla con los resultados
    return (encontrado, cantidad, elementos_en_comun)


# Función principal
def main():
    print("\n ------------- INGRESO DE LISTAS --------------\n")
    entrada1 = input("Introduce la primera lista: ")
    entrada1 = entrada1.split()  # Se convierte la cadena en una lista
    entrada2 = input("\nIntroduce la segunda lista: ")
    entrada2 = entrada2.split()
    encont, cant, comun = comparar_listas(entrada1, entrada2)
    if encont:  # Si se encontró al menos un elemento en común
        print("\n ------------- RESULTADOS --------------\n")
        print(f"Hay elementos en común: {encont}")
        print(f"\nLa cantidad de elementos en común es: {cant}")
        print(f"\nLos elementos en común son: {comun}")
    else:
        print("No hay elementos en común.")

main()
