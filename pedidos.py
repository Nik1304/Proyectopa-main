import json
from archivos import cargar_datos, guardar_datos
from validaciones import validar_codigo_unico, validar_stock

def crear_pedido():
    pedidos = cargar_datos("pedidos.json")
    productos = cargar_datos("productos.json")

    codigo_pedido = input("Ingrese el código del pedido: ")
    if not validar_codigo_unico(codigo_pedido, pedidos):
        print("Error: El código de pedido ya existe.")
        return

    codigo_cliente = input("Ingrese el código del cliente: ")
    fecha = input("Ingrese la fecha del pedido (YYYY-MM-DD): ")
    detalles = []

    while True:
        codigo_producto = input("Ingrese el código del producto (o 'fin' para terminar): ")
        if codigo_producto.lower() == "fin":
            break

        producto = next((p for p in productos if p["codigo"] == codigo_producto), None)
        if not producto:
            print("Error: Producto no encontrado.")
            continue

        cantidad = int(input("Ingrese la cantidad: "))
        if not validar_stock(codigo_producto, cantidad):
            print("Error: Stock insuficiente.")
            continue

        detalle = {
            "codigo_producto": codigo_producto,
            "cantidad": cantidad,
            "precio_unitario": producto["precio_venta"]
        }
        detalles.append(detalle)

        # Reducir el stock
        producto["cantidad"] -= cantidad

    pedido = {
        "codigo_pedido": codigo_pedido,
        "codigo_cliente": codigo_cliente,
        "fecha": fecha,
        "detalles": detalles
    }

    pedidos.append(pedido)
    guardar_datos("pedidos.json", pedidos)
    guardar_datos("productos.json", productos)
    print("Pedido registrado exitosamente.")

def gestionar_pedidos():
    while True:
        print("\n----------- Gestión de Pedidos -----------")
        print("1. Crear Pedido")
        print("2. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_pedido()
        elif opcion == "2":
            break
        else:
            print("Opción no válida,No sabes leer?,Intente nuevamente.")