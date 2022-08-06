from typing import TypedDict
from requests import get

# https://openweathermap.org/api ; https://openweathermap.org/current

class CoordinatesDict(TypedDict):
    lon: float
    lat: float

class WeatherDict(TypedDict):
    id: int
    main: str
    description: str
    icon: str

class MainDict(TypedDict):
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    humidity: int

class WindDict(TypedDict):
    speed: int
    deg: int

class CloudsDict(TypedDict):
    all: int

class SysDict(TypedDict):
    type: int
    id: int
    country: str
    sunrise: int
    sunset: int

class DictionaryOfWeather(TypedDict):
    coord: CoordinatesDict
    weather: WeatherDict
    main: MainDict
    wind: WindDict
    clouds: CloudsDict
    sys: SysDict
    visibility: int
    timezone: int
    base: str
    name: str
    cod: int
    dt: int
    id: int

def GetWeather(lattitude: float, longitude:float, apiKey: str) -> DictionaryOfWeather:
    Weather = get(f"https://api.openweathermap.org/data/2.5/weather?lat={lattitude}&lon={longitude}&appid={apiKey}&lang=ru&units=metric")
    return Weather.json()