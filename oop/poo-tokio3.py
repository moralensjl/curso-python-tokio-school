class Galleta:
    chocolate = False # atributo de la clase
    def __init__(self):
        print("Se acaba de crear una galleta")


    def chocolatear(self):
        print("Vamos a chocolatear la galleta")
        self.chocolate = True


    def tiene_chocolate(self):
        if self.chocolate == True:
            print("Soy una galleta chocolateada :-D")
        else:
            print("Soy una galleta sin chocolate :-(")


print("GALLETA 1")
g = Galleta()
g.tiene_chocolate()
g.chocolatear()
g.tiene_chocolate()


g1 = Galleta()
g2 = Galleta()
# print(g1)
