# Catalogo de peliculas

class Pelicula:
    def __init__(self, titulo, duracion, lanzamiento, director):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        self.director = director
        print(f"Gracias por registrar su pelicula favorita {self.titulo}")


    def __str__(self):
        return f"{self.titulo} ({self.lanzamiento})."




class Catalogo:

    def __init__(self, nombre, peliculas=None):
        self.nombre = nombre
        self.peliculas = peliculas

        if len(self.peliculas) == 0:
            print("Se ha creado un catalogo vacio")
        else:
            print("Se ha creado el catalogo con las peliculas asignadas")


    def agregar(self, p):
        self.peliculas.append(p)
        print(f"Se ha agregado al catalogo la pelicula {p}")


    def mostrar(self):
        print(f"Catalogo: {self.nombre}")
        for p in self.peliculas:
            print(f" >>> {p}")


    def __str__(self):
        return "El catalogo {} tiene {} Peliculas".format(self.nombre, len(self.peliculas))

p1 = Pelicula(titulo="Outlander", duracion=1000, lanzamiento=2018, director="Miguel Sastre")
p2 = Pelicula(titulo="Age Ultron", duracion=250, lanzamiento=2021, director= "Jonas Miguel")

lista_de_peliculas = [p1, p2]

c1 = Catalogo(nombre="Peliculas favoritas", peliculas=[p1, p2]) # Aqui lo paso de manera directa
c2 = Catalogo(nombre="Peliculas favoritas", peliculas= lista_de_peliculas)
print(lista_de_peliculas)

print(c2)
c2.mostrar()

p3 = Pelicula(titulo="Los hermanos Grimm", duracion=300, lanzamiento= 1950, director="Ibrahms")
p4 = Pelicula(titulo="Wakanda Forever", duracion= 350, lanzamiento= 2022, director="Jonas Grant")
# agregamos las peliculas directamente
c2.agregar(Pelicula(titulo="Los hermanos Grimm", duracion=300, lanzamiento= 1950, director="Ibrahms"))

print(c2)
c2.agregar(p4)
c2.mostrar()

c3 = Catalogo(nombre="Pelis pendientes", peliculas=[])
c3.mostrar()

p5 = Pelicula(titulo="Black Panther", duracion=400, lanzamiento=2023, director="Alens Borrego")
p6 = Pelicula(titulo="Iron Man", duracion=400, lanzamiento=2021, director="Alez Liendo")
p7 = Pelicula(titulo="Transformers", duracion=400, lanzamiento=2024, director="Nico Badona")

c4 = Catalogo(nombre="Peliculas de ciencia ficcion", peliculas=[p5,p6,p7])
c4.mostrar()
c3.agregar(p5)
c3.mostrar()


