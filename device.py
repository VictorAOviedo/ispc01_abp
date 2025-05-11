def list_device(lista):
    return lista

def search_device(lista, device):
    return device in lista

def new_device(lista, device):
    if device not in lista:
        lista.append(device)

def delete_device(lista, device):
    if device in lista:
        lista.remove(device)
    else:
        print("Dispositivo no encontado")
