# 4_13_Polimorfismo
# Número de desafío: 4
# Consigna: Implementa el polimorfismo con métodos de clase en figuras geométricas.
# Se crea una clase base Figura con un método area, y dos subclases Circulo y Cuadrado que sobrescriben este método.
# Autora: Eliana D

# Puntos principales:
# - La clase Figura define un método area, pero no realiza cálculos.
# - Las subclases Circulo y Cuadrado sobrescriben este método para calcular el área específica de cada figura.
# - Se demuestra el polimorfismo al usar el mismo método para diferentes tipos de figuras.

import math  # Importamos la librería math para operaciones matemáticas como el valor de pi

# Clase base Figura con un método área
class Figura:
    def area(self):
        pass  # Método vacío que se sobrescribirá en las subclases

# Subclase Circulo que sobrescribe el método area
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio  # Atributo para el radio del círculo

    def area(self):
        return math.pi * (self.radio ** 2)  # Cálculo del área de un círculo

# Subclase Cuadrado que sobrescribe el método area
class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado  # Atributo para el lado del cuadrado

    def area(self):
        return self.lado ** 2  # Cálculo del área de un cuadrado

# Solicitar datos al usuario
radio = float(input("\nIngrese el radio del círculo: "))
lado = float(input("Ingrese el lado del cuadrado: "))

# Instanciación de objetos
circulo = Circulo(radio)  # Crear un objeto de la clase Circulo
cuadrado = Cuadrado(lado)  # Crear un objeto de la clase Cuadrado

# Mostrar los resultados de las áreas de las figuras
print(f"\nÁrea del círculo: {circulo.area()}")  # Cálculo del área del círculo
print(f"Área del cuadrado: {cuadrado.area()}")  # Cálculo del área del cuadrado
