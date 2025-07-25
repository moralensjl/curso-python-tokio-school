mi_lista = []
print(mi_lista)

mi_lista.append("Carls")
print(mi_lista)

def agregar_elementos(elementos, lista=[]):
    lista.append(elementos)
    return lista


mi_lista2 = agregar_elementos("Fitz")
mi_lista3 = agregar_elementos("Max")
mi_lista4 = agregar_elementos("King")
# print(mi_lista2)
# print(mi_lista3)
print(mi_lista4)

listas_de_nombres = []

