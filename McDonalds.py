inventario = [{"nombre":"McFlury","precio":2.50, "stock":10}]

def menu_principal():
    """
    muestra el menu principal
    """
    while True:
        print("menu principal")
        print("1. agregar producto")
        print("2. mostrar inventario")
        print("3. vender producto")
        print("4. salir")
        
        opcion = input("seleccione un opcion: ")
        
        if opcion == "1":
            agregar_producto()
        elif opcion =="2":
            mostrar_inventario()
        elif opcion =="3":
            vender_producto()
        elif opcion =="4":
            break
        else:
            print("opcion no valida. por favor intente otra vez")
        
def agregar_producto():
    """
    agregar un nuevo producto al inventario 
    """
    
    nombre = input("ingrese el nombre del producto: ")
    precio = float(input("ingrese el precio del producto: "))
    cantidad = int(input("ingrese la cantidad del producto: "))
    
    producto = {"nombre": nombre, "precio": precio, "stock": cantidad}
    
    inventario.append(producto)
    
    print(f"producto {nombre} agregado al inventario")
    print(inventario)

def mostrar_inventario():
    """
    muestra todos los productos del inventario
    """
    
    if len(inventario) == 0:
        print("el inventario esta vacio")
    else:
        print("presentando inventario")
        
        for producto in inventario:
            print(f"nombre:{producto['nombre']}, precio: {producto['precio']:.2f}, cantidad: {producto['stock']}")

def vender_producto():
    """
    vende un producto, actualiza el inventario y muestra el total de la venta
    """
    
    nombre = input("ingrese el nombre del producto que desee vender: ")
    
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            cantidad = int(input(f"¿cuantas unidades de {nombre} desea vender?: "))
            if cantidad <= producto ["stock"]:
                producto["stock"] -= cantidad
                total = cantidad * producto["precio"]
                print(f"venta realizada. total: ${total:.2f}")
                
                if producto["stock"] ==0:
                    print(f"el producto {nombre} se ha agotado.")
                    
                return
            else:
                print("no hay suficiente stock en inventario")
                return
    print("producto no encontrado en el inventario")
        
menu_principal()