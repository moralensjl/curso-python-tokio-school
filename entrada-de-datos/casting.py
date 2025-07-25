# CASTING -> conversion de datos
a = 2
print(a)
b = str(a)
print(type(b))


nombre = "moralens"
print(nombre)
print(type(nombre))

nombre = int(nombre)
print(type(nombre))



print(isinstance(a, str))

texto = "Buenos dias"

if isinstance(texto, str):
    print("Es una cadena de texto")
else:
    print("No es una cadena de texto")

edad = "26"
edad = int(edad)
print(type(edad))

