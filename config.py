from os.path import exists
from json import load
from typing import TypedDict, Union

class ConfigDictionary(TypedDict):
    lattitude: float
    longitude: float
    apikey: str

def Config() -> Union[ConfigDictionary, None]:        
    if exists("config.json"):
        with open("config.json", "r") as f:
            settings = load(f)
        return settings
    else:
        with open("config.json", "w") as f:
            f.write('{\n\t"apikey": "",\n\t"lattitude": 0.0000,\n\t"longitude": 0.0000\n}')
        return None