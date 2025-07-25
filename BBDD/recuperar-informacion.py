import sqlite3

conexion = sqlite3.connect("example.db")

c = conexion.cursor()

# Recuperamos los registros de la tabla usuarios
c.execute("SELECT name, email FROM usuarios")

# Recorremos el primer registro con el metodo fectone
usuario = c.fetchone()
print(usuario) # ('Moralens', 27, 'alensj@gmail.com')

conexion.close()