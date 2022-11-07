
from rich.console import Console
from rich.panel import Panel
import json


# def get_json_params(key):
try:
    with open('lesson_20221104/config.json', 'r', encoding='utf_8') as config:
        params = json.load(config)
except Exception as err:
    print(f'Error in "get_json_params": message > {err}')
    # return params[key]


print(params.get('test'))

rc = Console()

weather_url = 'https://api.openweathermap.org/data/2.5/weather?q=' \
              '{city}&appid=47503e85fabbabc93cff28c52398ae97&units=metric'

# asd = input('Input city: ')
# print(weather_url.format(city=asd))