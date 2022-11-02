# 1. Дана довільна строка. Напишіть код, який знайде в ній і віведе на екран кількість слів,
# які містять дві голосні літери підряд.
# 2. Є два довільних числа які відповідають за мінімальну і максимальну ціну.
# Є Dict з назвами магазинів і цінами:
# { "cito": 47.999, "BB_studio" 42.999, "momo": 49.999, "main-service": 37.245,
# "buy.now": 38.324, "x-store": 37.166, "the_partner": 38.988, "store": 37.720,
# "rozetka": 38.003}.
# Напишіть код, який знайде і виведе на екран назви магазинів,
# ціни яких попадають в діапазон між мінімальною і максимальною ціною.
# Наприклад:
# lower_limit = 35.9
# upper_limit = 37.339
# > match: "x-store", "main-service"

from rich.console import Console
from rich.panel import Panel


rc = Console()
rule_style = 'bold white on blue'
success = 'bold green'
warning = 'bold yellow'
danger = 'bold red'


while True:
    rc.print(Panel('Please, select what you have to do:\n'
                   ' - press 1 to check string line for double vowel letters\n'
                   ' - press 2 to check price from dictionary\n'
                   ' - press 0 to exit',
                   title='Homework 4. 01.11.2022'))
    chosen_value = input('Your selection, e.g. 1: ')

    if chosen_value not in ['0', '1', '2']:
        rc.print(f'Your selection {chosen_value} is wrong. Please, repeat your selection.', style=warning)
        continue

    if chosen_value == '0':
        rc.print('[bold white on green]Thank you for using out application. Have a nice day![/bold white on green]')
        break

    # ex.1
    if chosen_value == '1':
        vowel_letters = ['a', 'e', 'i', 'o', 'u']
        word_list = input('Write down your text (word(s), sentence, large text): ').split()
        count_of_words = 0

        for word in word_list:
            for i in range(1, len(word)):
                if word[i-1] in vowel_letters and word[i] in vowel_letters:
                    count_of_words += 1
                    break
        rc.print(f'The count of words with double vowel letters is {count_of_words}', style=success)

    # ex.2
    else:
        shops_prices = { "cito": 47.999,
                         "BB_studio": 42.999,
                         "momo": 49.999,
                         "main-service": 37.245,
                         "buy.now": 38.324,
                         "x-store": 37.166,
                         "the_partner": 38.988,
                         "store": 37.720,
                         "rozetka": 38.003
                         }
        upper_limit = lower_limit = 0.0
        result = ''

        try:
            lower_limit = float(rc.input('Please, input [bold blue]lower limit[/bold blue] for price (e.g. 0.123): '))
            upper_limit = float(rc.input('Please, input [bold blue]upper limit[/bold blue] for price (e.g. 41.456): '))
        except Exception as err:
            rc.print(f'We got an incorrect value(s) of lover or upper limit. '
                     f'Please, be careful next time', style=danger)
            continue

        if lower_limit > upper_limit:
            rc.print(f'Lower limit of "{lower_limit}" is greater of upper limit "{upper_limit}". '
                  f'No result will be found. Please, be careful next time!', style=warning)
            continue

        for item in shops_prices.items():
            if lower_limit <= float(item[1]) <= upper_limit:
                result += f'"{item[0]}"' if not result else f', "{item[0]}"'

        message = f'[white on green]Match result[/white on green]: [bold green]{result}[/bold green]' \
            if result else '[blink bold white on red]No matches found![/blink bold white on red]'

        rc.print(message)



