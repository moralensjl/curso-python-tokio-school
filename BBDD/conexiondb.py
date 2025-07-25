import sqlite3

# Nos conectamos a la Base de datos example.db
conexion = sqlite3.connect("example.db")


# Cerramos la conexion, si no la cerramos se mantendra el uso y no podremos usar el fichero
conexion.close()