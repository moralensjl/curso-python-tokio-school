class Dog:
    especie = "Canina" # Atributo de clase

    def __init__(self, raza, nombre):
        self.raza = raza
        self.nombre = nombre


    def estado(self):
        print(f"{self.nombre} esta caminando")


# Creacion de los objetos
my_dog1 = Dog("Bulldog", "Max")
my_dog1.estado()

my_dog2 = Dog("Chihuahua", "Tommy")
print(my_dog2.nombre)

# Configurar algunas propiedades
my_dog2.nombre = "Tom"
print(my_dog2.nombre)