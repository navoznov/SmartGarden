import json

def __get_config():
    config_json_str = open("gardenConfig.json").read()
    return json.loads(config_json_str)

config = __get_config()