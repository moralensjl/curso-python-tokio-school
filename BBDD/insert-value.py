import sqlite3

conexion = sqlite3.connect("example.db")

c = conexion.cursor()

# Insertamos un registro en la tabla usuario => Solo un registro
c.execute("INSERT INTO usuarios VALUES ('Moralens', 27, 'alensj@gmail.com') ")

conexion.commit()

conexion.close()