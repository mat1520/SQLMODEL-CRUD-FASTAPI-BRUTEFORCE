#!/bin/bash

API_URL="http://127.0.0.1:8000"
username="ARIEL"
password=""
max_length="8"

printf "Bienvenido :)\n"
read -p "Ingresa la contraseña a atacar que deseas para atacar: " password

curl -s -X POST "$API_URL/users?username=$username&password=$password" > /dev/null

./env/bin/python3 -c "
from bruteforce import fuerza_bruta
import time

start = time.time()
resultado, intentos = fuerza_bruta('$password', $max_length)
end = time.time()

print(f'Contraseña: {resultado}')
print(f'Intentos: {intentos}')
print(f'Tiempo: {end - start:.2f}s')
"
