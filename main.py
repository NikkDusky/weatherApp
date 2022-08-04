from api_weather import Weather
from os.path import exists
from json import load

def startWeather() -> None:
    lat = config["lattitude"]
    lon = config["longitude"]
    api = config["apikey"]

    WeatherTEXT = Weather(lat, lon, api)
    print(WeatherTEXT)

if __name__ == "__main__":
    if exists("config.json"):
        with open("config.json", "r") as f:
            config = load(f)
    else:
        with open("config.json", "w") as f:
            f.write('{\n\t"apikey": "",\n\t"lattitude": 0.0000,\n\t"longitude": 0.0000\n}')

    startWeather()