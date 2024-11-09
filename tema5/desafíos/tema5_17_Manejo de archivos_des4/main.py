# tema5_17_Manejo de archivos
# Número de desafío: 4
# Consigna:
'''
Escribe un programa que permita eliminar el registro de un préstamo de un archivo prestamos.txt. 
El programa debe mostrar los registros actuales, permitir al usuario seleccionar cuál eliminar, 
y luego actualizar el archivo sin el registro eliminado.
'''
# Autora: Eliana D

def mostrar_prestamos():
    try:
        # Leer el archivo y mostrar los registros de préstamos
        with open('prestamos.txt', 'r') as archivo:
            prestamos = archivo.readlines()
            
            if prestamos:
                print("\nRegistros de préstamos:")
                for idx, prestamo in enumerate(prestamos, start=1):
                    print(f"{idx}. {prestamo.strip()}")
                return prestamos
            else:
                print("No hay registros de préstamos.")
                return []
    except FileNotFoundError:
        print("El archivo 'prestamos.txt' no existe.")
        return []

def eliminar_prestamo():
    # Mostrar los préstamos actuales
    prestamos = mostrar_prestamos()
    
    if prestamos:
        try:
            # Solicitar al usuario el número del préstamo a eliminar
            seleccion = int(input("\nIngrese el número del préstamo que desea eliminar: "))
            
            if 1 <= seleccion <= len(prestamos):
                # Eliminar el préstamo seleccionado
                prestamos.pop(seleccion - 1)
                print("¡Préstamo eliminado exitosamente!")
                
                # Escribir los registros actualizados de vuelta al archivo
                with open('prestamos.txt', 'w') as archivo:
                    archivo.writelines(prestamos)
            else:
                print("Número de préstamo inválido.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    else:
        print("No hay préstamos para eliminar.")

# Ejecutar la función
eliminar_prestamo()


