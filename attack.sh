#!/bin/bash

print "BIENVENIDO :) "
read -p "Ingresa la contraseña a atacar que deseas para atacar:. " password

curl -X POST -e "http://127.0.0.1:8000/users?username=ARIEL&password=$password\n" 

./env/bin/python3 -c "
from bruteforce import fuerza_bruta
from time import time

tiempo = time()
respuesta, intentos = fuerza_bruta('$password', 8)
print(f'Contraseña: {respuesta}\nIntentos: {intentos}\nTiempo: {time()-tiempo:.2f}s')
"