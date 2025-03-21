def validar_codigo_unico(codigo, lista):
    return all(item["codigo"] != codigo for item in lista)

def validar_stock(codigo_producto, cantidad):
    productos = cargar_datos ("productos.json")
    producto = next((p for p in productos if p["codigo"] == codigo_producto), None)
    return producto and producto["cantidad"] >= cantidad
