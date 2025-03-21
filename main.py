from producto import gestionar_productos
from pedidos import gestionar_pedidos
from inventario import ver_inventario
def mostrar_menu():
    print("\n---------- Menú Principal -----------")
    print("1. Gestión de Productos")
    print("2. Gestión de Pedidos")
    print("3. Ver Inventario")
    print("4. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            gestionar_productos()
        elif opcion == "2":
            gestionar_pedidos()
        elif opcion == "3":
            ver_inventario()
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()