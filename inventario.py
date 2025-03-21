from archivos import cargar_datos

def ver_inventario():
    productos = cargar_datos("productos.json")
    print("\n--- Inventario ---")
    for producto in productos:
        print(f"{producto['nombre']} - Stock: {producto['cantidad']}")