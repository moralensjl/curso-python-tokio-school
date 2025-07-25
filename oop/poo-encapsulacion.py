# Sin encapsulacion

class Persona:
    def __init__(self, nombre, saldo):
        self.nombre = nombre
        self.saldo = saldo

p = Persona(nombre="Carls", saldo=500)
p.saldo = 900 # modificamos la informacion
print(p.saldo)



# Ejemplo con encapsulacion
class Person:
    def __init__(self, nombre, saldo):
        self._nombre = nombre
        self._saldo = saldo


    # Getters
    @property
    def nombre(self):
        return self._nombre


    @property
    def saldo(self):
        return self._saldo


    # Setters
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre


    @saldo.setter
    def saldo(self, nuevo_saldo):
        if self._saldo > 0:
            self._saldo = nuevo_saldo



    def __str__(self):
        return f"{self._nombre} {self._saldo}"


p1 = Person(nombre="Samuel", saldo=50000)
print(p1.saldo)
print(p1.nombre)

p1.nombre = "Claire" # Modificamos la informacion
print(p1.nombre)
print(p1.__dict__)


