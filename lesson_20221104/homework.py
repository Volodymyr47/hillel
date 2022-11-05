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
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from tabulate import tabulate

rc = Console()
success = 'bold on green'
warning = 'bold yellow'
danger = 'bold red'


while True:

    rc.print(Panel('Please, select what you have to do:\n'
                       ' - press [bold green]1[/bold green] to get names of all astronauts in orbit\n'
                       ' - press [bold green]2[/bold green] to get weather in the city\n'
                       ' - press [bold green]0[/bold green] to exit',
                       title='Homework 4. 01.11.2022'))

    task_number = Prompt.ask('Enter your number only. Default value is 1',
                             choices=['0', '1', '2'],
                             default='1',
                             show_choices=False,
                             show_default=False
                             )

    if task_number == '0':
        break

    # ex. 1
    if task_number == '1':
        url = 'http://api.open-notify.org/astros.json'
        data = requests.get(url).json()
        result_list = []
        if data['people']:
            rc.rule('[bold on blue]Astronauts, who\'s are in orbit right now[/bold on blue]')
            for astronaut in data['people']:
                result_list.append(astronaut)
            rc.print(tabulate(result_list, headers='keys', tablefmt='grid'), style=success)
    # ex. 2
    else:
        city_name = Prompt.ask('Please, write down name of city to get the weather')
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=47503e85fabbabc93cff28c52398ae97&units=metric'
        weather_data = requests.get(url).json()



