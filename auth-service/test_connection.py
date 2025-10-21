import psycopg2

connection_db = psycopg2.connect(
    host="localhost",
    port=5432,
    database="main_db",
    user="devuser",
    password="devpass" 
)

# Creamos un cursor para ejecutar consultas
cursor_con = connection_db.cursor()

# Probar la conexión
cursor_con.execute("SELECT version();")
version = cursor_con.fetchone()
print("Conectado a:", version)

# Cerrar la conexión
cursor_con.close()
connection_db.close()