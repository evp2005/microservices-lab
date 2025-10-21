// ...existing code...
# Laboratorio de Microservicios (Django + React)

## Resumen
Repositorio de ejemplo con una arquitectura de microservicios para practicar integración local usando Docker Compose. Contiene servicios de autenticación, blog, email, frontend y un reverse-proxy, además de servicios base PostgreSQL y Redis.

## Estructura del proyecto
- [auth-service](auth-service/) — Servicio de autenticación (Django).  
  - [auth-service/Dockerfile](auth-service/Dockerfile)  
  - [auth-service/requirements.txt](auth-service/requirements.txt)  
  - [auth-service/test_connection.py](auth-service/test_connection.py) — script de prueba de conexiones.
- [blog-service](blog-service/) — Servicio de posts (esqueleto).
- [email-service](email-service/) — Servicio de correo (esqueleto).
- [frontend](frontend/) — Interfaz React (esqueleto).
- [reverse-proxy](reverse-proxy/) — Gateway local (esqueleto).
- [docker-compose.yml](docker-compose.yml) — Orquestador local.
- [.env](.env) — Variables de entorno usadas en ejemplos.

## Requisitos
- Docker y Docker Compose instalados.
- (Opcional) Python 3.10+ si quieres ejecutar el script de prueba localmente sin contenedores.

## Arrancar los servicios con Docker Compose
1. Levanta los servicios base (Postgres y Redis):
```sh
docker compose up -d
```
2. Verifica que los contenedores estén corriendo:
```sh
docker compose ps
```

Los puertos expuestos son:
- PostgreSQL: 5432 (host -> contenedor) definido en [docker-compose.yml](docker-compose.yml)
- Redis: 6379 (host -> contenedor) definido en [docker-compose.yml](docker-compose.yml)

## Probar conexiones (script)
El repositorio incluye un script de comprobación en [auth-service/test_connection.py](auth-service/test_connection.py). Este script contiene dos funciones principales:
- [`test_connection.verify_connection`](auth-service/test_connection.py) — prueba la conexión a PostgreSQL.
- [`test_connection.test_redis`](auth-service/test_connection.py) — prueba la conexión a Redis y guarda/recupera una clave.

Ejecuta el script desde la raíz del proyecto (si los servicios corren en el host tal como en docker compose con puertos mapeados):
```sh
python auth-service/test_connection.py
```

Si prefieres ejecutarlo dentro de un contenedor que tenga Python y las dependencias, podrías crear un contenedor temporal con las librerías listadas en [auth-service/requirements.txt](auth-service/requirements.txt) o usar la imagen definida en [auth-service/Dockerfile](auth-service/Dockerfile).

## Salida esperada / Resultados
Salida típica al ejecutar el script (ejemplo):

- Resultado de PostgreSQL (imprime la versión):
Consola:
```
Conectado a: ('PostgreSQL 15.x on x86_64-pc-linux-gnu, compiled by ...',)
```

- Resultado de Redis (imprime el valor recuperado):
Consola:
```
b'Franco'
```

(NOTA: el texto exacto de la versión de PostgreSQL variará según la imagen utilizada.)

## Variables de entorno
El archivo [.env](.env) contiene variables usadas como ejemplo:
- POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB
- REDIS_HOST, REDIS_PORT

Asegúrate de que las credenciales en el script de prueba coincidan con las de [.env](.env) o con la configuración de tu despliegue.

## Recomendaciones
- No incluyas archivos de entorno sensibles en el repositorio (ya está en `.gitignore`).
- Usa contenedores para ejecutar los servicios y evitar conflictos con instalaciones locales.
- Para producción, reemplaza contraseñas por secretos gestionados y no uses `restart: always` sin monitoreo.

## Referencias rápidas en el repo
- [docker-compose.yml](docker-compose.yml)  
- [.env](.env)  
- [auth-service/Dockerfile](auth-service/Dockerfile)  
- [auth-service/requirements.txt](auth-service/requirements.txt)  
- [auth-service/test_connection.py](auth-service/test_connection.py) — funciones: [`test_connection.verify_connection`](auth-service/test_connection.py), [`test_connection.test_redis`](auth-service/test_connection.py)

## Contribuciones
Pull requests y issues son bienvenidos. Describe cambios y pasos para reproducir localmente.

{ changed code }
```// filepath: README.md
// ...existing code...
# Laboratorio de Microservicios (Django + React)

## Resumen
Repositorio de ejemplo con una arquitectura de microservicios para practicar integración local usando Docker Compose. Contiene servicios de autenticación, blog, email, frontend y un reverse-proxy, además de servicios base PostgreSQL y Redis.

## Estructura del proyecto
- [auth-service](auth-service/) — Servicio de autenticación (Django).  
  - [auth-service/Dockerfile](auth-service/Dockerfile)  
  - [auth-service/requirements.txt](auth-service/requirements.txt)  
  - [auth-service/test_connection.py](auth-service/test_connection.py) — script de prueba de conexiones.
- [blog-service](blog-service/) — Servicio de posts (esqueleto).
- [email-service](email-service/) — Servicio de correo (esqueleto).
- [frontend](frontend/) — Interfaz React (esqueleto).
- [reverse-proxy](reverse-proxy/) — Gateway local (esqueleto).
- [docker-compose.yml](docker-compose.yml) — Orquestador local.
- [.env](.env) — Variables de entorno usadas en ejemplos.

## Requisitos
- Docker y Docker Compose instalados.
- (Opcional) Python 3.10+ si quieres ejecutar el script de prueba localmente sin contenedores.

## Arrancar los servicios con Docker Compose
1. Levanta los servicios base (Postgres y Redis):
```sh
docker compose up -d
```
2. Verifica que los contenedores estén corriendo:
```sh
docker compose ps
```

Los puertos expuestos son:
- PostgreSQL: 5432 (host -> contenedor) definido en [docker-compose.yml](docker-compose.yml)
- Redis: 6379 (host -> contenedor) definido en [docker-compose.yml](docker-compose.yml)

## Probar conexiones (script)
El repositorio incluye un script de comprobación en [auth-service/test_connection.py](auth-service/test_connection.py). Este script contiene dos funciones principales:
- [`test_connection.verify_connection`](auth-service/test_connection.py) — prueba la conexión a PostgreSQL.
- [`test_connection.test_redis`](auth-service/test_connection.py) — prueba la conexión a Redis y guarda/recupera una clave.

Ejecuta el script desde la raíz del proyecto (si los servicios corren en el host tal como en docker compose con puertos mapeados):
```sh
python auth-service/test_connection.py
```

Si prefieres ejecutarlo dentro de un contenedor que tenga Python y las dependencias, podrías crear un contenedor temporal con las librerías listadas en [auth-service/requirements.txt](auth-service/requirements.txt) o usar la imagen definida en [auth-service/Dockerfile](auth-service/Dockerfile).

## Salida esperada / Resultados
Salida típica al ejecutar el script (ejemplo):

- Resultado de PostgreSQL (imprime la versión):
Consola:
```
Conectado a: ('PostgreSQL 15.x on x86_64-pc-linux-gnu, compiled by ...',)
```

- Resultado de Redis (imprime el valor recuperado):
Consola:
```
b'Franco'
```

(NOTA: el texto exacto de la versión de PostgreSQL variará según la imagen utilizada.)

## Variables de entorno
El archivo [.env](.env) contiene variables usadas como ejemplo:
- POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB
- REDIS_HOST, REDIS_PORT

Asegúrate de que las credenciales en el script de prueba coincidan con las de [.env](.env) o con la configuración de tu despliegue.

## Recomendaciones
- No incluyas archivos de entorno sensibles en el repositorio (ya está en `.gitignore`).
- Usa contenedores para ejecutar los servicios y evitar conflictos con instalaciones locales.
- Para producción, reemplaza contraseñas por secretos gestionados y no uses `restart: always` sin monitoreo.

## Referencias rápidas en el repo
- [docker-compose.yml](docker-compose.yml)  
- [.env](.env)  
- [auth-service/Dockerfile](auth-service/Dockerfile)  
- [auth-service/requirements.txt](auth-service/requirements.txt)  
- [auth-service/test_connection.py](auth-service/test_connection.py) — funciones: [`test_connection.verify_connection`](auth-service/test_connection.py), [`test_connection.test_redis`](auth-service/test_connection.py)

## Contribuciones
Pull requests y issues son bienvenidos. Describe cambios y pasos para reproducir localmente.

{ changed code }