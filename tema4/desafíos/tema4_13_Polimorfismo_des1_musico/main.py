# 4_13_Polimorfismo
# Número de desafío: 1
# Consigna: Crea una clase Musico que tenga un método instrumento y crea dos subclases 
# Guitarrista y Baterista que sobrescriban el método instrumento. Instancia objetos de estas clases 
# y demuestra el polimorfismo.
# Autora: Eliana D

# Puntos principales:
# - Se define una clase base Musico con un método instrumento.
# - Se crean subclases Guitarrista y Baterista que sobrescriben el método instrumento.
# - Se demuestra el polimorfismo al llamar al mismo método en diferentes objetos, pero con comportamientos distintos.

# Clase base Musico
class Musico:
    def instrumento(self):
        pass  # El método base no hace nada, pero es sobrescrito por las subclases

# Subclase Guitarrista que sobrescribe el método instrumento
class Guitarrista(Musico):
    def instrumento(self):
        return "Toco la guitarra."  # Sobrescribimos el método para la guitarra

# Subclase Baterista que sobrescribe el método instrumento
class Baterista(Musico):
    def instrumento(self):
        return "Toco la batería."  # Sobrescribimos el método para la batería

# Instanciación de objetos de cada subclase
guitarrista = Guitarrista()
baterista = Baterista()

# Demostración del polimorfismo llamando al mismo método en objetos diferentes
print(guitarrista.instrumento())  # Toco la guitarra.
print(baterista.instrumento())    # Toco la batería.





