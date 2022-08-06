from api import GetWeather
from config import Config
class Main():
    def __init__(self) -> None:
        pass

    def Info(self) -> None:
        lat = Settings["lattitude"]
        lon = Settings["longitude"]
        api = Settings["apikey"]
        self.WeatherJSON = GetWeather(lat, lon, api)
    
if __name__ == "__main__":
    Settings = Config()
    if Settings == None:
        print("Укажите apikey, долготу и широту в config.json")
    else:
        WeatherApp = Main()
        WeatherApp.Info()
        print(WeatherApp.WeatherJSON)
        print(f'Температура {WeatherApp.WeatherJSON["main"]["temp"]} градуса')
        print(f'Ощущается как {WeatherApp.WeatherJSON["main"]["feels_like"]} градуса')