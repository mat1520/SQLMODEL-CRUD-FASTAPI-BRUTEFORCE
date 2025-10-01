# CRUD de Usuarios + Ataque de Fuerza Bruta

**Actividad:** CRUD de Usuarios + Prueba controlada de fuerza bruta contra tu propia API

## Objetivo

Construir una API REST con operaciones CRUD sobre usuarios y ejecutar un experimento de fuerza bruta de forma controlada y ética para comprender vulnerabilidades y diseñar medidas de mitigación.


## Resultados de Aprendizaje

- Diseñar e implementar endpoints CRUD seguros
- Comprender cómo un ataque de fuerza bruta explota credenciales débiles
- Medir tiempo/recursos y efectos del ataque
- Justificar estadísticas de seguridad



## Endpoints de la API

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/` | Información de la actividad |
| POST | `/users` | Crear usuario |
| GET | `/users` | Listar todos los usuarios |
| GET | `/users/{id}` | Obtener usuario por ID |
| PUT | `/users/{id}` | Actualizar usuario |
| DELETE | `/users/{id}` | Eliminar usuario |
| POST | `/login` | Autenticar usuario |

## Instalación

```bash
# Clonar repositorio
git clone https://github.com/mat1520/SQLMODEL-CRUD-FASTAPI-BRUTEFORCE.git
cd SQLMODEL-CRUD

# Crear entorno virtual
python3 -m venv env
source env/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

## Uso

### 1. Iniciar la API

```bash
fastapi dev

La API estará disponible en: `http://127.0.0.1:8000`

Documentación interactiva: `http://127.0.0.1:8000/docs`

### Ejecutar el Ataque de Fuerza Bruta

En otra terminal:

```bash
chmod +x attack.sh
./attack.sh


El script te pedirá ingresar la contraseña a atacar. 

**Ejemplo:**

Bienvenido :)
Ingresa la contraseña a atacar que deseas para atacar: abc


```

## Algoritmo de Fuerza Bruta

El archivo `bruteforce.py` contiene una función que intenta todas las combinaciones posibles de caracteres:

- **Alfabeto:** a-z, A-Z, 0-9, símbolos especiales
- **Método:** Iteración incremental (longitud 1 a `long_max`)
- **Retorna:** Contraseña encontrada y número de intentos

**Nota:** Contraseñas largas (>5 caracteres) pueden tomar mucho tiempo.

## Configuración del Script de Ataque

El script `attack.sh` tiene las siguientes variables configurables:

```bash
API_URL="http://127.0.0.1:8000"  
username="ARIEL"                 
max_length="8"                   


## Medidas de Mitigación Recomendadas

1. **Rate Limiting:** Limitar intentos de login por IP/usuario
2. **Contraseñas Fuertes:** Mínimo 12 caracteres, mixtos
3. **Hashing:** Nunca almacenar contraseñas en texto plano (usar bcrypt, argon2)
4. **2FA:** Autenticación de dos factores
5. **Bloqueo Temporal:** Bloquear cuenta tras X intentos fallidos
6. **Monitoreo:** Detectar patrones de ataque en logs

## Resultados Esperados

Para contraseñas cortas:
- **3 caracteres:** 
Bienvenido :)
Ingresa la contraseña a atacar que deseas para atacar: 123
Longitud 1...
Longitud 2...
Longitud 3...
Contraseña: 123
Intentos: 224399
Tiempo: 0.03s

- **4 caracteres:** Minutos
Bienvenido :)
Ingresa la contraseña a atacar que deseas para atacar: 12av
Longitud 1...
Longitud 2...
Longitud 3...
Longitud 4...
Contraseña: 12av
Intentos: 19968952
Tiempo: 1.93s

- **5+ caracteres:** 
Bienvenido :)
Ingresa la contraseña a atacar que deseas para atacar: 12345
Longitud 1...
Longitud 2...
Longitud 3...
Longitud 4...
Longitud 5...
Contraseña: 12345
Intentos: 1777705369
Tiempo: 172.48s (2.87 minutos)

## Análisis de Recursos Consumidos

### Recursos Computacionales Medidos

Durante la ejecución del ataque se consumen:

**CPU:**
- Uso intensivo de 1 core al 100%


**Memoria RAM:**
- Consumo mínimo: ~50-100 MB


## Efectos del Ataque

## Autor

[@mat1520](https://github.com/mat1520)