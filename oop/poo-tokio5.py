
class Director:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        print(f"Se ha creado el director {self.nombre} {self.apellido} con una edad {self.edad}")



    def __str__(self):
        return f"Director {self.nombre} {self.apellido} con edad {self.edad}"


d1 = Director("Ridley", "Scott", 84)
d2 = Director("George", "Lucas", 34)
print(d1)
print(d1.nombre)
print(d2)
print(d2.nombre)




class Pelicula:
    def __init__(self, titulo, duracion, lanzamiento, director):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        self.director = director
        print(f"Se ha creado la pelicula {self.titulo}")


    def __str__(self):
        return f"{self.titulo} ({self.lanzamiento}) -> {self.director}."



p1 = Pelicula(titulo="El padrino",duracion=175, lanzamiento=1975, director= d1)
print(p1)

# Los objetos en python estan almacenados en dict
peli = p1.__dict__ # Vemos todos los elementos atrves de un diccionario
print(peli)
print(p1.__dict__)

p2 = Pelicula("Agente 007", 190, 2007, d2)
print(p2.director)
print(p2.director.nombre)




