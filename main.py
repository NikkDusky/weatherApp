from api import GetWeather
from config import Config
class Main():
    def __init__(self) -> None:
        pass

    def Info(self) -> None:
        lat = Settings["lattitude"] #some problems with mypy Value of type "Optional[ConfigDictionary]" is not indexable
        lon = Settings["longitude"] #some problems with mypy Value of type "Optional[ConfigDictionary]" is not indexable
        api = Settings["apikey"] #some problems with mypy Value of type "Optional[ConfigDictionary]" is not indexable
        self.WeatherJSON = GetWeather(lat, lon, api)
    
if __name__ == "__main__":
    Settings = Config()
    if Settings == None:
        print("Укажите apikey, долготу и широту в config.json")
    else:
        WeatherApp = Main()
        WeatherApp.Info()
        print(WeatherApp.WeatherJSON) #some problems with mypy Cannot determine type of "WeatherJSON"
        print(f'Температура {WeatherApp.WeatherJSON["main"]["temp"]} градуса') #some problems with mypy Cannot determine type of "WeatherJSON"
        print(f'Ощущается как {WeatherApp.WeatherJSON["main"]["feels_like"]} градуса') #some problems with mypy Cannot determine type of "WeatherJSON"