import json
from archivos import cargar_datos, guardar_datos
from validaciones import validar_codigo_unico

def registrar_producto():
    productos = cargar_datos("productos.json")
    codigo = input("Ingrese el código del producto: ")
    
    if not validar_codigo_unico(codigo, productos):
        print("Error: El código ya existe.")
        return
    
    nombre = input("Ingrese el nombre del producto: ")
    categoria = input("Ingrese la categoría del producto: ")
    proveedor = input("Ingrese el proveedor: ")
    cantidad = int(input("Ingrese la cantidad en stock: "))
    precio_compra = float(input("Ingrese el precio de compra: "))
    precio_venta = float(input("Ingrese el precio de venta: "))

    producto = {
        "codigo": codigo,
        "nombre": nombre,
        "categoria": categoria,
        "proveedor": proveedor,
        "cantidad": cantidad,
        "precio_compra": precio_compra,
        "precio_venta": precio_venta
    }

    productos.append(producto)
    guardar_datos("productos.json", productos)
    print("Producto registrado exitosamente.")

def buscar_producto():
    productos = cargar_datos("productos.json")
    criterio = input("Buscar por (nombre/categoría/código): ").lower()
    valor = input(f"Ingrese el {criterio}: ")

    resultados = []
    for producto in productos:
        if valor.lower() in producto[criterio].lower():
            resultados.append(producto)

    if resultados:
        for producto in resultados:
            print(producto)
    else:
        print("No se encontraron resultados.")

def gestionar_productos():
    while True:
        print("\n--- Gestión de Productos ---")
        print("1. Registrar Producto")
        print("2. Buscar Producto")
        print("3. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            buscar_producto()
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Intente nuevamente.")