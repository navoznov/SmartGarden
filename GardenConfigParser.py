from garden import Garden
import json

class GardenConfigParser:
    @staticmethod
    def parse(jsonStr: str):
        return json.loads(jsonStr)