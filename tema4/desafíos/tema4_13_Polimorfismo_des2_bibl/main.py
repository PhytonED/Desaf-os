# 4_13_Polimorfismo
# Número de desafío: 2
# Consigna: Añade un método biografia a la clase Autor y sobrescríbelo en la clase Escritor.
# Instancia un objeto de la clase Escritor y muestra cómo se puede acceder al método biografia de ambas clases.
# Autora: Eliana D

# Puntos principales:
# - La clase Autor tiene un método biografia que proporciona una biografía general.
# - La clase Escritor hereda de Autor y sobrescribe biografia con información específica de un escritor.
# - Se demuestran las diferencias al acceder al método biografia de ambas clases.

# Clase base Autor
class Autor:
    def biografia(self):
        return "Biografía de un autor general."  # Método biografía base para la clase Autor

# Subclase Escritor que sobrescribe el método biografía
class Escritor(Autor):
    def biografia(self):
        return "Biografía de un escritor."  # Método biografía sobrescrito para la clase Escritor

# Instanciación de objetos de ambas clases
autor = Autor()
escritor = Escritor()

# Llamada al método biografia en el objeto de la clase Autor
print(autor.biografia())  # Biografía de un autor general.
# Llamada al método biografia en el objeto de la clase Escritor
print(escritor.biografia())  # Biografía de un escritor.




















































