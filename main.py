from api import GetWeather
from config import Config
class Main():
    def __init__(self) -> None:
        pass

    def Info(self) -> None:
        lat = Config.settings["lattitude"]
        lon = Config.settings["longitude"]
        api = Config.settings["apikey"]
        self.WeatherJSON = GetWeather(lat, lon, api)
    
if __name__ == "__main__":
    WeatherApp = Main()
    WeatherApp.Info()
    print(WeatherApp.WeatherJSON)