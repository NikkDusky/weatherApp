from os.path import exists
from json import load

class Config():
    def __init__(self) -> None:        
        if exists("config.json"):
            with open("config.json", "r") as f:
                self.settings = load(f)
        else:
            with open("config.json", "w") as f:
                f.write('{\n\t"apikey": "",\n\t"lattitude": 0.0000,\n\t"longitude": 0.0000\n}')