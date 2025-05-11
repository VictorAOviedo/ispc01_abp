def list_devices(device_list):
    return device_list

def search_device(device_list, device):
    return device in device_list

def add_device(device_list, device):
    if device not in device_list:
        device_list.append(device)

def remove_device(device_list, device):
    if device in device_list:
        device_list.remove(device)
