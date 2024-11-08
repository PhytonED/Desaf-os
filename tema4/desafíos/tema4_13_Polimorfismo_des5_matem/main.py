# 4_13_Polimorfismo
# Número de desafío: 5
# Consigna: Aplica el polimorfismo para realizar diferentes operaciones matemáticas.
# Se crea una clase base Operación y dos subclases Suma y Multiplicación que sobrescriben el método resultado.
# Autora: Eliana D

# Puntos principales:
# - La clase base Operación define un método resultado, pero no realiza ningún cálculo.
# - Las subclases Suma y Multiplicación sobrescriben este método para realizar la operación correspondiente.
# - Se demuestra el polimorfismo al realizar diferentes operaciones con el mismo método.

# Clase base Operacion
class Operacion:
    def resultado(self, num1, num2):
        pass  # El método base no hace nada, se sobrescribe en las subclases

# Subclase Suma que sobrescribe el método resultado
class Suma(Operacion):
    def resultado(self, num1, num2):
        return num1 + num2  # Realiza la operación de suma

# Subclase Multiplicacion que sobrescribe el método resultado
class Multiplicacion(Operacion):
    def resultado(self, num1, num2):
        return num1 * num2  # Realiza la operación de multiplicación

# Solicitar datos al usuario para realizar las operaciones
num1 = float(input("\nIngrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Instanciación de objetos de las subclases
suma = Suma()
multiplicacion = Multiplicacion()

# Mostrar los resultados de las operaciones
print(f"\nSuma: {suma.resultado(num1, num2)}")  # Resultado de la suma
print(f"Multiplicación: {multiplicacion.resultado(num1, num2)}")  # Resultado de la multiplicación
