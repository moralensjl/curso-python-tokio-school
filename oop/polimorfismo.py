
class Perro:

    def ladrido(self):
        return "Guau!"


class Gato:
    def maullido(self):
        return "Miau"


p = Perro()
print(p.ladrido())

g = Gato()
print(g.maullido())


class Dog:
    def sonido(self):
        return "Guau"


class Cat:
    def sonido(self):
        return "Miau"


my_dog = Dog()
my_dog.sonido()

my_cat = Cat()
my_cat.sonido()