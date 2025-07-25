class Coche:
    def __init__(self, modelo, anio, numeroMatricula):
        self._modelo = modelo
        self._anio = anio
        self._numeroMatricula = numeroMatricula

     # Getters y Setters

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, nuevo_modelo):
        self._modelo = nuevo_modelo


    @property
    def anio(self):
        return self._anio


    @anio.setter
    def anio(self, anio_carro):
        self._anio = anio_carro


    def matricula(self):
        print(f"Numero de matricula => {self._numeroMatricula}")



    def __str__(self):
        return f"{self._modelo}, {self._anio}, {self._numeroMatricula}"


mi_coche = Coche("Ford", 2023, "HDI-467")
print(f"Modelo: { mi_coche.modelo}")
print(f"Anio: {mi_coche.anio}")



class Vehiculo(Coche):
    
    def __init__(self, modelo, anio, cantidad_puertas, tipo_de_coche):
        super().__init__(modelo, anio, self._numeroMatricula)

        self.cantidad_puertas = cantidad_puertas
        self.tipo_de_coche = tipo_de_coche

    @property
    def cantidad_puertas(self):
        return self._cantidad_puertas

    @property
    def tipo_de_coche(self):
        return self.tipo_de_coche

    @tipo_de_coche.setter
    def tipo_de_coche(self, value):
         self._tipo_de_coche = value


    @cantidad_puertas.setter
    def cantidad_puertas(self, value):
        self._cantidad_puertas = value


v1 = Vehiculo("Mazda", 2022, 4, "Yipeta")