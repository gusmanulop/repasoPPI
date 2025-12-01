import pymysql

def get_db_connection():
    conn = pymysql.connect(
        host='localhost',  # Cambia por tu host de MySQL
        user='root',  # Cambia por tu usuario de MySQL
        password='root',  # Cambia por tu contraseña de MySQL
        database='unida',  # Cambia por tu base de datos
        port=3307,
        auth_plugin_map={
            "caching_sha2_password": "pymysql.auth.caching_sha2_password"  # Mapeo del plugin de autenticación
        }
    )
    return conn
