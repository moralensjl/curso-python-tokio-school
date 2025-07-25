# tabulaciones
print("Esto es una tabulacion\tun texto")
# salto de linea
print("Salto de linea\nun texto")
# triple comilla
print("""
Instrucciones para el usuario
otra instruccion

otra linea\tuna tabulacion
""")

"""
Comentario de varias lineas
esto me gusta porque no es como vscode
lo puedes poner en cualquier linea
"""

# sep y and
print(1, 2, 3, 4, 5)
print(1, 2, 3, 4, sep=',')
print(1, 2, 3, 4, end='...')

# metodo format
informacion = """
Hay varios anuncios importantes que queremos darle\n 
por favor presten atencion a los diferentes comentarios y\n
anuncios que estaremos diciendo.
""".upper()

print(f"El presidente de la junta dio la siguiente informacion: {informacion}")