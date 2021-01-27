class Device:
    def __init__(self, id: str, device_type: str, name=None: str, description=None: str):
        self.id = id
        self.type = device_type
        self.name = name if name != None else "Датчик пин #" + str(pin)
        self.description = description if description != None else "Датчик " + str(pin)
