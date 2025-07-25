import sqlite3

conn = sqlite3.connect("tienda.db")
conn.set_trace_callback(print)
cur = conn.cursor()

# Creamos la tabla
cur.execute("CREATE TABLE productos (id INTEGER, nombre VARCHAR(100), precio REAL, stock INTEGER)")

productos = [(1, "Iphone", 44.7, 20),
             (2, "Lenovo Legion", 100.78, 21),
             (3, "Jordan Brand", 23.5, 12),
             (4, "T-shirt", 11, 10),
             (5, "BackPack Hight Sierra", 22.89, 14)]


cur.executemany("INSERT INTO productos VALUES (?,?,?,?)", productos)

conn.commit()
conn.close()

