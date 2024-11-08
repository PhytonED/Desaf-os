# formato_texto.py

# NEGRITA ----

def negrita(texto):
        return f'\033[1m{texto}\033[0m'

# CURSIVA ----

def cursiva(texto):
        return f'\033[3m{texto}\033[0m'

# SUBRAYADO ----

def subrayado(texto):
        return f'\033[4m{texto}\033[0m'

# COLOR TEXTO----
# Colores: rojo, verde, amarillo, azul, magenta, cian, blanco.

def color(texto, nombre_color):
        colores = {
            'rojo': '\033[31m',
            'verde': '\033[32m',
            'amarillo': '\033[33m',
            'azul': '\033[34m',
            'magenta': '\033[35m',
            'cian': '\033[36m',
            'blanco': '\033[37m'
        }
        codigo_color = colores.get(nombre_color.lower(), '\033[37m')
        return f'{codigo_color}{texto}\033[0m'

# COLOR FONDO
# Colores: rojo, verde, amarillo, azul, magenta, cian, blanco.
def colorf(texto, nombre_colorf):
        colores_fondo = {
            'rojo': '\033[41m',
            'verde': '\033[42m',
            'amarillo': '\033[43m',
            'azul': '\033[44m',
            'magenta': '\033[45m',
            'cian': '\033[46m',
            'blanco': '\033[47m'
        }
        codigo_colorf = colores_fondo.get(nombre_colorf.lower(), '\033[0m')
        return f'{codigo_colorf}{texto}\033[0m'

# MAYÚSCULAS ----

def a_mayusculas(texto):
        return texto.upper()

# MINÚSCULAS ----

def a_minusculas(texto):
        return texto.lower()

    
    
    
    
    
    
    
