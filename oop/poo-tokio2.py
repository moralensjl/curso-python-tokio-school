class Galleta:
    pass
# Atributos: hacen referencia a las variables internas de la clase
# Metodos: hacen referencia a las funciones internas de la clase

if __name__ == "__main__":
    mi_galleta = Galleta()

    mi_galleta.sabor = "Salado"
    mi_galleta.color = "Marron"

    print(f"El sabor de la galleta es: {mi_galleta.sabor}")