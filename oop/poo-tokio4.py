class Galleta:
    empresa = "Cuetara"

    def __init__(self, sabor, forma, chocolate):
        self.sabor = sabor
        self.forma = forma
        self.chocolate = chocolate
        if self.chocolate:
            print(f"Se acaba de crear una galleta {self.sabor}, {self.forma} y con chocolate")
        else:
            print(f"Se acaba de crear una galleta {self.sabor}, {self.forma} y sin chocolate")


    def chocolatear(self):
        print("Vamos a chocolatear la galleta")
        self.chocolate = True


    def tiene_chocolate(self):
        if self.chocolate == True:
            print("Soy una galleta chocolateada :-D")
        else:
            print("Soy una galleta sin chocolate :-(")



# Creamos los objetos

g = Galleta("Salada", "Cuadrada", True)
print(g.chocolate)

g1 = Galleta("Dulce", "Redonda", False)
