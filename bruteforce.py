import itertools
import time

def fuerza_bruta(contrasenia, long_max=8):
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-_=+[]{};:,.<>?/|"
    attempts = 0
    for longitud in range(1, long_max + 1):
        print(f"Longitud {longitud}...")
        for intento in itertools.product(alphabet, repeat=longitud):
            attempts += 1
            intento_s = ''.join(intento)
            if intento_s == contrasenia:
                return intento_s, attempts
    return None, attempts