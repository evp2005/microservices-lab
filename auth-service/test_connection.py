import redis
import psycopg2

host_db="localhost"
port_db=5432
database_db="main_db"
user_db="devuser"
password_db="devpass" 

def verify_connection(host,port,database,user,password):
    connection_db = psycopg2.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password 
    )

    # Creamos un cursor para ejecutar consultas
    cursor_con = connection_db.cursor()

    # Probar la conexión
    cursor_con.execute("SELECT version();")
    version = cursor_con.fetchone()
    result = f"Conectado a: {version}"

    # Cerrar la conexión
    cursor_con.close()
    connection_db.close()
    return print(result)

def test_redis(host, username):
    # Conectar al servicio Redis que corre en tu Docker
    r = redis.Redis(host=host, port=6379, db=0)

    # Guardar un valor
    r.set('usuario', username)

    # Recuperarlo
    return print(r.get('usuario'))  # b'Evor'
    
verify_connection("localhost",5432,"main_db","devuser","devpass")
test_redis("localhost", username="Franco")

