from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self, marca, anio):
        self._marca = marca
        self._anio = anio

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, value):
        self._anio = value


    @abstractmethod
    def estado(self):
        print("El carro esta corriendo")


class Coche(Vehiculo):
    def __init__(self, marca, anio, color):
        super().__init__(marca, anio)

        self._color = color


    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value


    def estado(self):
        print("El carro esta corriendo")


    def __str__(self):
        return f"Marca: {self._marca} Anio: {self._anio} Color: {self._color}"


c1 = Coche("Ford", 2024, "Azul")
print(c1.marca)
c1.estado()