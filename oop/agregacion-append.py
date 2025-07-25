def agregar_nombres(elemento, lista=None):
    if lista is None:
        lista = []
    lista.append(elemento)

    return lista


print(agregar_nombres(12))
print(agregar_nombres(13))
print(agregar_nombres(15))
print(agregar_nombres(14))
print(agregar_nombres(16))
print(agregar_nombres(18))


def agregar_personas(nombres, personas=[]):
    personas.append(nombres)
    return personas

print(agregar_personas("Fitz"))
print(agregar_personas("Max"))
print(agregar_personas("Cam"))
print(agregar_personas("James"))