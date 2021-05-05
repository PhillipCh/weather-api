import requests
import ast
from decouple import config
 

class WeatherAPI:
    def __init__(self):
        self.url = "http://api.openweathermap.org/data/2.5/weather?q={},uk&APPID={}"
        # SET local environment variable KEY to API key in .env file
        self.api_key = config('KEY')

    def get(self, city):
        response = requests.get(self.url.format(city, self.api_key))
        dict = ast.literal_eval(response.text)
                
        print(dict)



WeatherAPI().get("London")
WeatherAPI().get("New&York")


