# Creamos una lista
mi_lista = [1, 2, 3, 4, 5]

# Acceso a una lista
print(mi_lista[3])

# Agregar un elemento a una lista
mi_lista.append(6)
print(mi_lista)

# agrega un elemento en indice especifico
mi_lista.insert(0, 1)
print(mi_lista)

# agrega varios elementos
mi_lista.extend([7, 8])

# Editamos una lista
mi_lista[0] = 0
print(mi_lista)

# Eliminar un elemento de una lista
mi_lista.remove(2)
print(mi_lista)



# Longitud del elemento
print(len(mi_lista))

# mi_lista.clear()
# print(mi_lista)

# Recorrer una lista
for lista in mi_lista:
    print(f"* {lista}")

for lista in range(len(mi_lista)):
    print(mi_lista[lista])

if 99 not in mi_lista:
    print("Este numero no esta en la lista")
else:
    print("Este numero esta en la lista")

print("***---***---***---")

if 90 in mi_lista:
    print("El numero 99 esta en la lista")
else:
    print("Dicho elemento no esta en la lista")

print("***---***---***---")

if 10 not in mi_lista:
    print("No esta en la lista")
else:
    print("Esta en la lista")

print("***---***---***---")

if len(mi_lista) > 0:
    print("El indice 0 existe")
else:
    print("Ese indice 0 no existe")

lista_nombres = ["Sarah", "Cristina", "Jessica"]
print(lista_nombres)
if "Sarah" in lista_nombres:
    print("Sarah esta en la lista")
else:
    print("No esta en la lista")

print(lista_nombres)

if "Jessica" not in lista_nombres:
    print("El nombre no aparece en la lista")
else:
    print("El nombre esta en la lista")

# Devuelve un indice de un elemento
mi_lista.index(3)
print(mi_lista)

# Cuantas veces aparece un elemento
mi_lista.count(3)
print(mi_lista)

# Ordena de menor a mayor
mi_lista.sort()
print(mi_lista)

# Invierte el orden
mi_lista.reverse()
print(mi_lista)