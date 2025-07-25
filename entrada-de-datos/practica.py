producto = input(">> Introduce el producto que quieras comprar: ")
venta = int(input(">> Que cantidad necesita: "))
print("Bienvenido a nuestra tienda online >>")
while True:
    if venta == 1:
        print(">> Gracias por comprar nuestros productos, gracias por preferirnos")
        break
    elif venta == 2:
        print(">> Si compras dos productos te llevas mas")
        venta += 2
        print(f">> Ahora tienes {venta} unidades de {producto}")
        print(">> Gracias por tu compra")
    else:
        print("Gracias por visitar nuestra tienda")
        break