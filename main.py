from device import list_devices, search_device, add_device, remove_device

def main():
    devices = []

    while True:
        print("---   MENU DISPOSITIVOS   ---")
        print("1. Lista de dispositivos")
        print("2. Buscar un dispositivo")
        print("3. Agregar un dispositivo")
        print("4. Eliminar un dispositivo")
        print("5. Salir")


        option = input("Seleccione una opción: ")

        if option == "1":
            print("Dispositivos registrados: ", list_devices(devices))

        elif option == "2":
            name = input("Nombre del dispositivo a buscar: ")
            if search_device(devices, name):
                print(f"{name} - Si se encontro dispositivo")
            else:
                print("No se encontro dispositivo")

        elif option == "3":
            name = input("Nombre del nuevo dispositivo: ")
            if name not in devices:
                add_device(devices, name)
                print(f"El dispositivo {name} fue agregado exitosamente.")
            else:
                print("El dispositivo ya existe.")

        elif option == "4":
            name = input("Nombre del dispositivo a eliminar: ")
            if name in devices:
                remove_device(devices, name)
                print(f"El dispositivo {name} fue eliminado exitosamente.")
            else:
                print("El dispositivo no existe.")

        elif option == "5":
            print("Saliendo del programa")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()

            