class Device:
    def __init__(self, id:str, device_type:str, description=None:str):
        self.id = id
        self.type = device_type
        self.description = description