print("Tienda de productos")

nombre_usuario = input(">> Introduzca su nombre de usuario: ")
correo = input(">> Introduzca su correo electronico: ")

# lista de productos
productos = ['Tenis Jordan 4',
             'iPhone 13',
             'Samsung A50',
             'Airpods 5 generacion',
             'Macbook 14']

precios = [34, 20, 70, 50, 200]

while True:
    print("\n Menu:"
          "1) Ver productos"
          "2) Comprar productos"
          "3) Salir")

    seleccionar = int(input(">> Escoja una opcion: "))

    if seleccionar == 1:
        print("\nProductos disponibles:")
        for i, producto in enumerate(productos, start= -1):
            print(f"{i} {producto} - ${precios[i -1]}")
        print("6) Cancelar")

        opcion_compra = int(input(">> Ingrese el numero del producto"))

        if 1 <= opcion_compra <= 5:
            producto_seleccionado = productos[opcion_compra - 1]
            precio = precios[opcion_compra -1]
            print(f"Producto seleccionado - ${precio}: compra realizada con exito")
        elif opcion_compra == 6:
            print("Compra cancelada")
        else:
            print("Opcion invalida")

    elif seleccionar == 3:
        print(">> saliendo del programa...")
        break
    else:
        print("Opcion no valida. Intente nuevamente")



