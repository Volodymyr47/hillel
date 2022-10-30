# 1. Напишіть код, який зформує строку, яка містить певну інформацію про символ за
# його номером у слові.
# Наприклад "The [номер символу] symbol in '[тут слово]' is '[символ з відповідним порядковим номером в слові]'".
# Слово та номер символу отримайте за допомогою input() або скористайтеся константою.
# Наприклад (слово - "Python" а номер символу 3) - "The 3 symbol in 'Python' is 't' ".
#
# 2. Вести з консолі строку зі слів за допомогою input() (або скористайтеся константою).
# Напишіть код, який визначить кількість слів, в цих даних.
#
# 3. Існує ліст з різними даними, наприклад
# lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який сформує новий list (наприклад lst2), який би містив всі числові змінні (int, float),
# які є в lst1. Майте на увазі, що данні в lst1 не є статичними можуть змінюватись від запуску до запуску.

from rich.console import Console
from rich.panel import Panel

rule_style = 'bold white on blue'
success = 'bold green'
warning = 'bold yellow'
danger = 'bold red'
lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 0.256, 3.566, 'Lorem Ipsum']
lst2 = []

while True:
    rc = Console()
    rc.print(Panel(' - press 1 to get the letter of index\n'
                   ' - press 2 to get the count of words\n'
                   ' - press 3 to get the list of numbers\n'
                   ' - press 0 to exit\n', title='Choose your variant'))
    chose_value = input('Your selection: ')
    if chose_value == '':
        continue
    if chose_value not in ['0', '1', '2', '3']:
        rc.print('Entered selection is wrong. Please try again.')
        continue
    if chose_value == '0':
        break
    if chose_value == '1':
        # ex.1
        rc.rule(f'[{rule_style}] String for letter by it index [/{rule_style}]')
        message = ''
        style = ''
        input_string = input('Please, enter your string (e.g.: World): ')
        if input_string:
            input_index = input('Please, enter your index of letter (e.g.: 2): ')
            if input_index.isdigit():
                index = int(input_index)
                if index < len(input_string):
                    result_string = input_string[index]
                    message = f'The {input_index} symbol in \"{input_string}\" is \"{result_string}\"'
                    style = success
                else:
                    message = f'There is no index = \"{input_index}\" in the string \"{input_string}\". ' \
                              f'Please, be careful at the next time'
                    style = danger
            else:
                message = f'The index of \"{input_index}\" is wrong. Please, be careful at the next time!'
                style = danger
        else:
            message = 'Sorry, but you have not entered any string.'
            style = warning
        rc.print(message, style=style)
    elif chose_value == '2':
        # ex.2
        rc.rule(f'[{rule_style}] Count of words in the string [/{rule_style}]')
        input_string = input('Please, enter your string (e.g.: I like Python): string =')
        if input_string:
            list_of_words = input_string.split()
            message = f'Count of words of string \'{input_string}\' = {len(list_of_words)}'
            style = success
        else:
            message = 'You have not entered any string!'
            style = warning
        rc.print(message, style=style)
    else:
        # ex.3
        rc.print(f'We have a list: lst1 = {lst1}\nIf we will take only "int" or "float" values, we get the next list:')
        for element in lst1:
            if type(element) in [int, float]:
                lst2.append(element)
        message = f'lst2 = :{lst2}'
        style = success
        rc.print(message, style=style)
