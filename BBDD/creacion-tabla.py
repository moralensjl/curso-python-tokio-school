# from BBDD.conexiondb import conexion
import sqlite3

conexion = sqlite3.connect("example.db")

# Creamos el cursor
c = conexion.cursor()

# Ahora creamos la tabla para insertar datos dentro de ella
c.execute("CREATE TABLE usuarios (name VARCHAR(100), ege INTEGER, email VARCHAR(100) )")


# Guardamos los cambios con commit
conexion.commit()

conexion.close()