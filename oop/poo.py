class Coche:
    def __init__(self, marca, year):
        self._marca = marca
        self._year = year


    def arrancar(self):
        print("El carro arranca")

    # Getters
    @property
    def marca(self):
        return self._marca

    @property
    def year(self):
        return self._year

    # Setters
    @marca.setter
    def marca(self, nueva_marca):
        self._marca = nueva_marca


    @year.setter
    def year(self, new_year):
        self._year = new_year


miCoche = Coche(marca= "Ford", year= 2019)
print(miCoche.marca)
print(miCoche.year)
miCoche.arrancar()

# Usar el setter
miCoche.marca = "Mazda"
print(miCoche.marca)

""" HERENCIA EN PYTHON """

class Vehiculo(Coche):
    def __init__(self, marca, year, puertas):
        super().__init__(marca, year)
        self._puertas = puertas


    def cantida_de_puertas(self):
        print(f"Soy un vehiculo y tengo {self.puertas} puertas")


    # Getters
    @property
    def puertas(self):
        return self._puertas


    # Setters
    @puertas.setter
    def puertas(self, cantidad_puertas):
        self._puertas = cantidad_puertas



""" Creamos los objetos de la clase Vehiculo """
mi_vehiculo = Vehiculo("Toyota", 2021, 4)
print(mi_vehiculo.puertas)
mi_vehiculo.cantida_de_puertas()

