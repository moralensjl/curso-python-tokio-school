class Coche:
    def __init__(self, marca, anio, numeroMatricula):
        self._marca = marca
        self._anio = anio
        self._numeroMatricula = numeroMatricula

    # Getters y Setters
    @property
    def marca(self):
        return self._marca

    @property
    def anio(self):
        return self._anio

    @property
    def numeroMatricula(self):
        return self._numeroMatricula


    @numeroMatricula.setter
    def numeroMatricula(self, value):
        self._numeroMatricula = value


    @marca.setter
    def marca(self, value):
        self._marca = value


    @anio.setter
    def anio(self, value):
        self._anio = value


    def registroMatricula(self):
        print(f"Numero de Matricula registrado: {self._numeroMatricula}")




class Vehiculo(Coche):
    def __init__(self, marca, anio, numeroMatricula, cantidad_puertas, tipo_coche):
        super().__init__(marca, anio, numeroMatricula)

        self.cantidad_puertas = cantidad_puertas
        self.tipo_coche = tipo_coche


    @property
    def cantidad_puertas(self):
        return self._cantidad_puertas


    @property
    def tipo_coche(self):
        return self._tipo_coche


    @cantidad_puertas.setter
    def cantidad_puertas(self, value):
        self._cantidad_puertas = value


    @tipo_coche.setter
    def tipo_coche(self, value):
        self._tipo_coche = value



v1 = Vehiculo("Maserati", 2024, "HDY-465", 4, "Yipeta")

print(f"Marca: {v1.marca}")
print(f"Tipo de coche: {v1.tipo_coche}")
v1.registroMatricula()

print(v1.__dict__)

