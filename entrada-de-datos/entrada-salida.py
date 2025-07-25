# ENTRADA Y SALIDA DE DATOS
valor = input(">> Introduzca su nombre: ")
print(valor)
print(type(valor))
# valor = int(valor) va a dar error
print(valor)

valor = int(input(">> Introduzca su edad por pantalla: "))
print(valor)
print(type(valor))

while True:
    if valor > 17:
        print("Es mayor de edad")
        break
    elif valor <= 17:
        print("No es mayor de edad")
        break
    elif valor == 30:
        print("Te puedes casar")
        break
    elif valor == 0:
        print("No puedes incluir este valor")
        break
