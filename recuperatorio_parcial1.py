# "Chocolate en rama", "chocolate blanco", "chocolate con leche", "chocolate amargo"

productos = []
cantidades = []
salir = True
while salir:
    opcion = input(
    """Elija una opcion: 
    1. Agregar producto
    2. Ver productos agotados
    3. Actualizar stock
    4. Ver todos los productos
    5. Salir
    """
    )
    if opcion == "1":
        nombre_producto = input("ingrese el nombre del producto")
        productos.append(nombre_producto)
        cant_producto = input("Ingrese la cantidad del producto")
        cantidades.append(cant_producto)
        print("Producto agregado con exito")
    elif opcion == "2":
        print("Productos Agotados: ")
        agotados = False
        for i in range(len(productos)):
            if int(cantidades[i]) == 0:
                print(productos[i])
                agotados = True
            if agotados == False:
                print("No hay productos agiotados")
    elif opcion == "3":
        nombre_producto = input("Ingrese el nombre del producto")
        if nombre_producto in productos:
            indice_producto = productos.index(nombre_producto)
            cantidad_actualizada = input("Ingrese la nueva cantidad para este producto")
            cantidades[indice_producto] = cantidad_actualizada
            print("Stock Actualizado")
        else:
            print("Prodcuto no encontrado")
    elif opcion == "4":
        print("Lista de productos: ")
        for i in range(len(productos)):
            print("Producto: ",productos[i] ,"Cantidad: ", cantidades[i] )
    elif opcion == "5":
        print("Gracias por usar el sistema")
        salir = False
        