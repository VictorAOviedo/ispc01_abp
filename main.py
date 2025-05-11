from device import list_devices, search_device, add_device, remove_device
from automation import set_automation, show_automation

def main():
    devices = []
    automation = {}

    while True:
        print("---   MENU DISPOSITIVOS   ---")
        print("1. Lista de dispositivos")
        print("2. Buscar un dispositivo")
        print("3. Agregar un dispositivo")
        print("4. Eliminar un dispositivo")
        print("5. Establecer automatización")
        print("6. Mostrar automatizaciones")
        print("7. Salir")


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
            device = input("Introduce dispositivo a automatizar: ")
            if device in devices:           
                action = input("Introduce una acción para automatizar: ")
                time = input("Introduce la hora: ")
                set_automation(automation, device, action, time)
                print(f"Dispositivo: {device} - Acción: {action} -  Hora: {time}")
            else:
                print(f"No existe el dispositivo: {device}")

        elif option == "6":
            if show_automation(automation):
                print(f"Automatización programada: '{automation['device']}', {automation['action']} a las {automation['time']}")
            else:
                print("No hay automatización programada.")



        elif option == "7":
            print("Saliendo del programa")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()

            