persona = {
    "nombre": "Sarah",
    "edad": 25,
    "cuidad": "Madrid"
}
""" Diccionario con la funcion dict """

usuario = dict(nombre= "Ana", activo= True)
print(usuario)

person = dict(nombre= "Carmen", edad= 22, cuidad= "Barcelona")
print(person)

""" Acceder a los elementos """
print(person["nombre"])
print(usuario.get("activo"))
print(usuario.get("correo", "No disponible"))

""" Modificar elementos o Agregar elementos"""
usuario["nombre"] = "Fior" # Modifica
usuario["correo"] = "fior@exam.es" # Agrega
print(usuario)

""" Eliminar elementos """
usuario.pop("activo") # Elimina la clave y su valor
print(usuario)

# usuario.popitem() # Elimina el ultimo por anadido
# del usuario["nombre"] # Elimina por clave
# usuario.clear() # Vacia el diccionario


""" Recorrer un diccionario """
for clave in usuario: # Recorre las claves del diccionario
    print(clave)


for valor in usuario.values(): # Recorre los valores del dict
    print(valor)


for clave, valor in usuario.items(): # Recorre las claves y los valores del dict
    print(f"{clave}: {valor}")

print(usuario.keys()) # devuelve todas las claves
print(usuario.items()) # Devuelve lista de tuplas, clave valor

# dict.update()	Agrega otro diccionario

""" Ejemplo completo de diccionario """

persona2 = dict(nombre= "Laura", edad= 30, profesion= "Ingeniera")

persona2["cuidad"] = "Hong Kong"
print(persona2)

for person, personas in persona2.items():
    print(f"{person}: {personas}")

""" 🧪 Mini ejercicio para practicar """

productos = dict(laptop= 230, iphone= 570, backpack= 20)
productos["iPad"] = 300
print(productos)
productos.pop("iPad")
print(productos)

for i, j in productos.items():
    print(f"{i}: {j}")


