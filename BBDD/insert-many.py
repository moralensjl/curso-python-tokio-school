import sqlite3

conn = sqlite3.connect("example.db")
conn.set_trace_callback(print)
cursor = conn.cursor()

# Creamos una lista con varios usuarios
usuarios = [('Victoria', 22, 'victoria@pruebas.es'),
            ('Sarah', 33, 'sarah@pruebas.es'),
            ('Michael', 34, 'miguel@pruebas.es'),
            ('Noami', 25, 'naomi@pruebas.es'),
            ('Zaid', 31, 'zaid@pruebas.es'),
            ('Christopher', 29, 'chris@pruebas.es'),
            ('Lana', 26, 'lana@pruebas.es')]


# cursor.execute("""
#     INSERT INTO usuarios (nombre, edad, email)
#     VALUES (?, ?, ?)
# """, ("Laura", 29, "laura@pruebas.es"))



# Usamos el metodo executemany para inserta varios registros
cursor.executemany("INSERT INTO usuarios VALUES (?,?,?)", usuarios)

conn.commit()
conn.close()