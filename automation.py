def set_automation(automatizacion_dict, device, action, time):
    automatizacion_dict["device"] = device
    automatizacion_dict["action"] = action
    automatizacion_dict["time"] = time
    

def show_automation(automatizacion_dict):
    return automatizacion_dict