# tema5_17_Manejo de archivos
# Número de desafío: 1
# Consigna:
'''
Desarrolla un programa que cree un archivo prestamos.txt 
y permita al usuario agregar el registro de un préstamo. 
El registro debe incluir el nombre del libro, el nombre 
del prestatario y la fecha del préstamo. Asegúrate de no sobrescribir el archivo cada vez que se agrega un nuevo préstamo.
'''
# Autora: Eliana D

def agregar_prestamo():
    # Abrir el archivo en modo "a" (append) para agregar sin sobrescribir
    with open('prestamos.txt', 'a') as archivo:
        # Solicitar los datos del préstamo
        libro = input("Ingrese el nombre del libro: ")
        prestatario = input("Ingrese el nombre del prestatario: ")
        fecha = input("Ingrese la fecha del préstamo (DD/MM/AAAA): ")

        # Escribir los datos en el archivo
        archivo.write(f"{libro}, {prestatario}, {fecha}\n")
        print("¡Préstamo agregado exitosamente!")

def mostrar_prestamos():
    try:
        # Mostrar los registros actuales de préstamos
        with open('prestamos.txt', 'r') as archivo:
            prestamos = archivo.readlines()
            if prestamos:
                print("\nRegistros de préstamos:")
                for prestamo in prestamos:
                    print(prestamo.strip())
            else:
                print("No hay registros de préstamos.")
    except FileNotFoundError:
        print("El archivo 'prestamos.txt' no existe. No hay préstamos registrados aún.")

def menu():
    while True:
        # Menú de opciones
        print("\nSistema de Registro de Préstamos")
        print("1. Agregar un préstamo")
        print("2. Mostrar préstamos")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_prestamo()
        elif opcion == '2':
            mostrar_prestamos()
        elif opcion == '3':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida, por favor intente nuevamente.")

# Ejecutar el programa
menu()
