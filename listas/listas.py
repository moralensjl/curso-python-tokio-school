# lista = []
# Coleccion ordenada y modificable. Permite miembros duplicados.

# los puntos mas importantes de una lista es:
# 1) crear
# 2) acceder
# 3) agregar
# 4) editar
# 5) eliminar
numeros = [1, 2, 3, 4, 5]
print(f'Lista de numeros: {numeros}')

nombres = ['Alens', 'James', 'Tamara', 'Amanda']
print(f'lista de nombres: {nombres}')

# accader a los elementos
print(nombres[0])
print(nombres[-1])
print(nombres[0:3])
print(nombres[-3:-1])

edad = 34
nombre = 'Sarah'
pi = 3.14

elementos = [numeros, nombres, edad, nombre, pi, numeros]
print(elementos)

numeros = numeros + [6, 7, 8, 9]
elementos = [numeros, nombres, edad, nombre, pi, numeros]
print(numeros)

# modificar, editar elementos
names = ['Olivia', 'Maria', 'Nataly', 'Jorge', 'Axel']
names[3] = 'George'
print(names)

names[1] = 'Ellen'
print(names)

# agregar elementos
names.append('Clara') # agrega un elemento al final de la lista
print(names)

names.insert(0, 'Rossanna') # agrega un elemento en la posicion correcta
print(names)

# eliminar
names.remove('Clara')
print(names)

names.pop(0) # elimina la posicion de un lista
print(names)
