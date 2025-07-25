class Animal:
    def __init__(self, nombre_animal, familia,):
        self.nombre_animal = nombre_animal
        self.familia = familia
        print(f"El nombre del animal es {self.nombre_animal}")


    def __str__(self):
        return f"{self.familia} {self.nombre_animal}"



class Zoologico:
    def __init__(self, nombre, animales=None):
        self.nombre = nombre
        self.animales = animales

        if len(self.animales) == 0:
            print("La lista esta vacia")
        else:
            print(f"Se ha creado una lista de animales")


    def agregar_animal(self, a):
        self.animales.append(a)
        print(f"Se ha agregado un animal a la lista {a}")


    def mostrar_animales(self):
        print(f"Nombre de zoologico: {self.nombre}")
        for a in self.animales:
            print(f" >> {a}")


    def __str__(self):
        return "El {} tiene {} animales".format( self.nombre, len(self.animales))


a1 = Animal(nombre_animal= "Perro", familia= "Canina")
a2 = Animal(nombre_animal="Elefante", familia="Elephantidae")

lista_de_animales = [a1, a2]

zoo = Zoologico("zoologico nacional", animales=lista_de_animales)
#print(lista_de_animales)
print(zoo)

zoo.mostrar_animales()

# Vamos a agregar mas animales
zoo.agregar_animal(Animal(nombre_animal="Gato", familia="Felino"))
zoo.mostrar_animales()

# Otra forma de agregar elementos
a3 = Animal(nombre_animal="Tiburon", familia="Chondrichthyes")

zoo.agregar_animal(a3)
zoo.mostrar_animales()




