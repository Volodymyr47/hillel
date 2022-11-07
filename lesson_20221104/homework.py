# Завдання 1
# урл http://api.open-notify.org/astros.json
# вивести список всіх астронавтів, що перебувають в даний момент на орбіті
# (дані не фейкові, оновлюються в режимі реального часу)

# Завдання 2
# апі погоди (всі токени я для вас вже прописав)
# https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=47503e85fabbabc93cff28c52398ae97&units=metric
# де city_name - назва міста на аглійській мові (наприклад, odesa, kyiv, lviv)
# погода змінюється, як і місто. яке ви введете
# роздрукувати тепрературу та швидкість вітру. з вказівкою міста, яке було вибране


import requests
import json
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from tabulate import tabulate
from datetime import date


rc = Console()

try:
    with open('config.json', 'r', encoding='utf_8') as config:
        value_of = json.load(config)
except Exception as err:
    print(f'Loading config error: message > {err}')

astronauts_url = value_of['astronauts_url']
weather_url = value_of['weather_url']

while True:
    rc.print(Panel(value_of['greating_and_choice'], title=value_of['greating_title']))
    task_number = Prompt.ask(value_of["choice_answer"],
                             choices=['0', '1', '2'],
                             default='1',
                             show_choices=False,
                             show_default=False
                             )
    if task_number == '0':
        rc.print(value_of['By_by'])
        break

    # ex. 1
    if task_number == '1':

        rc.print(value_of['ex1_greating'].format(today=date.today()))

        while True:
            view_selection = Prompt.ask(value_of['ex1_ask_part_num'],
                                         choices=['0', '1', '2'],
                                         default='1',
                                         show_default=False,
                                         show_choices=False
                                        )
            if view_selection == '0':
                break

            astronauts = requests.get(astronauts_url).json()
            result_list = []

            if astronauts['people']:
                if view_selection == '1':
                    rc.rule(value_of['ex1_rule'])

                    for astronaut_data in astronauts['people']:
                        result_list.append(astronaut_data)
                    rc.print(tabulate(result_list, headers='keys', tablefmt='grid'),
                             style='bold white on rgb(12,153,28)'
                             )
                else:
                    for astronaut in astronauts['people']:
                        result_list.append({'name':astronaut['name']})
                    rc.print(tabulate(result_list, headers='keys', tablefmt='grid'),
                             style='bold white on rgb(12,153,28)'
                             )
    # ex. 2
    else:
        rc.print(value_of['ex2_greating'])

        while True:
            city_name = Prompt.ask(value_of['ex2_ask_city'])
            weather_data = requests.get(weather_url.format(city=city_name))

            if city_name == '0':
                break

            if str(weather_data.status_code)[0] == '4':
                rc.print(value_of['ex2_wrong_city_val'], style=value_of['danger'])
                continue

            weather_json = weather_data.json()
            rc.print(value_of['ex2_weather_part_choice'])
            weather_part = Prompt.ask(value_of['ex2_ask_for_choice'],
                                              choices=['0', '1', '2'],
                                              default='1',
                                              show_choices=False,
                                              show_default=False
                                              )
            if weather_part == '0':
                break

            weather = []
            main_data = {}
            if weather_json.get('main'):
                main_data.update(weather_json.get('main'))

            if weather_json.get('wind'):
                main_data.update(weather_json.get('wind'))

            if weather_part == '2':
                weather.append({'Temperature': main_data['temp'],
                                'Feels like': main_data['feels_like'],
                                'Temp MIN': main_data['temp_min'],
                                'Temp MAX': main_data['temp_max'],
                                'Wind speed': main_data['speed'],
                                'Wind deg': main_data['deg'],
                                'Wind gust': main_data['gust']
                                })
                rc.print(tabulate(weather, headers='keys', tablefmt='grid'), style=value_of['success'])
                rc.print(value_of['ex2_ask_another_city'])

            else:
                if weather_json.get('clouds'):
                    main_data.update(weather_json.get('clouds'))

                weather.append({'Temperature': main_data['temp'],
                                'Feels like': main_data['feels_like'],
                                'Temp MIN': main_data['temp_min'],
                                'Temp MAX': main_data['temp_max'],
                                'Wind speed': main_data['speed'],
                                'Wind deg': main_data['deg'],
                                'Wind gust': main_data['gust'],
                                'Pressure': main_data['pressure'],
                                'Humidity': main_data['humidity'],
                                'Clouds': main_data['all']
                                })
                rc.print(tabulate(weather, headers='keys', tablefmt='grid'), style=value_of['success'])
                rc.print(value_of['ex2_ask_another_city'])
