edad = 20
num = 10
if edad and num >= 10:
    print("Es mayor de edad y tiene muchos anos de experiencia")
else:
    print("Ninguna de la opciones anteriores")



if edad > 18 or num > 7:
    print("Puede aplicar al trabajo")
else:
    print("No puede aplicar a ninguno de los dos")


# Pedir datos al usuario
cumpleanos = input(">Hoy es tu dia de cumpleanos? ").lower()

if cumpleanos == "si":
    print("Hoy es su dia de cumpleanos, felicidades!")
elif cumpleanos == "no":
    print("No es el dia de sus cumpleanos")