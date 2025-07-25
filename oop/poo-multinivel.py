class Abuelo:
    def __init__(self, nombre_abuelo= None):
        self._nombre_abuelo = nombre_abuelo

    @property
    def nombre_abuelo(self):
        return self._nombre_abuelo


    @nombre_abuelo.setter
    def nombre_abuelo(self, value):
        self._nombre_abuelo = value


    def lenguaje_abuelo(self):
        print(f"{self._nombre_abuelo} programa en C++")


    def __str__(self):
        return f"{self._nombre_abuelo}"



class Padre(Abuelo):
    def __init__(self, nombre_abuelo=None, nombre_padre=None):
        super().__init__(nombre_abuelo)
        self._nombre_padre = nombre_padre


    @property
    def nombre_padre(self):
        return self._nombre_padre

    @nombre_padre.setter
    def nombre_padre(self, value):
        self._nombre_padre = value


    def lenguaje_padre(self):
        print(f"{self._nombre_padre} programa en Java")


    def __str__(self):
        return f"{self._nombre_padre}"




class Hijo(Padre):
    def __init__(self, nombre_abuelo,nombre_padre, nombre_hijo):
        super().__init__(nombre_padre, nombre_abuelo)
        self._nombre_hijo = nombre_hijo


    @property
    def nombre_hijo(self):
        return self._nombre_hijo


    @nombre_hijo.setter
    def nombre_hijo(self, value):
        self._nombre_hijo = value


    def lenguaje_hijo(self):
        print(f"{self._nombre_hijo} es programador python")



if __name__== "__main__":
    print("***---***---*** HIJO ***---***---***")
    h1 = Hijo("James", "Jacob", "Jaden")
    print(h1.nombre_abuelo)
    print(h1.nombre_padre)
    print(h1.nombre_hijo)

    h1.lenguaje_abuelo()
    #h1.nombre_padre()
    h1.lenguaje_hijo()

    print("***---***---*** PADRE ***---***---***")
    p1 = Padre("James", "Jacob")
    print(p1.nombre_abuelo)
    print(p1.nombre_padre)

    p1.lenguaje_abuelo()
    #p1.nombre_padre()
    #p1.lenguaje_hijo()

    print("***---***---*** ABUELO ***---***---***")
    a1 = Abuelo("James")
    print(a1.nombre_abuelo)
    a1.lenguaje_abuelo()
