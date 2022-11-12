# 1. Напишіть функцію, що приймає один аргумент будь-якого типу та повертає цей аргумент,
# перетворений на float. Якщо перетворити не вдається функція має повернути 0.
#
# 2. Напишіть функцію, що приймає два аргументи. Функція повинна
#  a) якщо аргументи відносяться до числових типів (int, float) - повернути перемножене значення цих аргументів,
#  b) якщо обидва аргументи це строки (str) - обʼєднати в одну строку та повернути
#  c) у будь-якому іншому випадку повернути кортеж з цих аргументів
#
# 3. Перепишіть за допомогою функцій вашу программу "Касир в кінотеатрі", яка буде виконувати наступне:
#    Попросіть користувача ввести свсвій вік.
# - якщо користувачу менше 7 - вивести "Тобі ж <> <>! Де твої батьки?"
# - якщо користувачу менше 16 - вивести "Тобі лише <> <>, а це е фільм для дорослих!"
# - якщо користувачу більше 65 - вивести "Вам <> <>? Покажіть пенсійне посвідчення!"
# - якщо вік користувача містить 7 - вивести "Вам <> <>, вам пощастить"
# - у будь-якому іншому випадку - вивести "Незважаючи на те, що вам <> <>, білетів всеодно нема!"
#   Замість <> <> в кожну відповідь підставте значення віку (цифру) та правильну форму слова рік.
#   Для будь-якої відповіді форма слова "рік" має відповідати значенню віку користувача (1 - рік, 22 - роки, 35 - років і тд...). Наприклад :
#       "Тобі ж 5 років! Де твої батьки?"
#       "Вам 81 рік? Покажіть пенсійне посвідчення!"
#       "Незважаючи на те, що вам 42 роки, білетів всеодно нема!"

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
import constants as const


rc = Console()


def choose_your_case():
    '''
    :return: of chose case number to continue or finish the performance of app
    '''
    task_number = Prompt.ask(const.CHOICE_ANWER,
                             choices=['0', '1', '2', '3'],
                             default='1',
                             show_choices=False,
                             show_default=False
                             )
    return int(task_number)


# case 1
def get_float_number(any_value):
    '''
    Try to convert param "argument" to float
    :param argument: anything
    :return: float or 0
    '''
    rc.print(const.EX1_WARN_MESSAGE)

    try:
        result = float(any_value)
    except Exception as err:
        result = 0
    output_message = f'Your result value is: {result}'
    return output_message


# case 2
def operation_with_arguments(arg1, arg2):
    '''
    operation with arguments
    :param arg1: accept any value
    :param arg2: accept any value
    :return: if types of arg1 and arg2 are int or float -> multiplication of arguments
            if type of arguments is str -> concationation of arguments
            else return tuple of arguments
    '''

    try:
        arg1 = float(arg1)
    except ValueError:
        pass

    try:
        arg2 = float(arg2)
    except ValueError:
        pass

    if isinstance(arg1, (float)) and isinstance(arg2, (float)):
        operation = arg1 * arg2
        return f'The result of multiplication is {operation}'

    if isinstance(arg1, str) and isinstance(arg2, str):
        operation = arg1 + arg2
        return f'The result of concatenation is {operation}'
    else:
        return f'The result is tuple: {(arg1, arg2)}'


# case 3
def cashier_in_the_cinema():
    '''
    The function ask user about age inside cycle.
    If age is wrong, app repeat ask the user to input the correct value.
    :return without return.
    '''
    while True:
        age = rc.input(const.EX3_ASK_INPUT_AGE)
        if not age:
            rc.print(const.EX3_AGE_NOT_INPUT, style=const.DANGER_STYLE)
            continue

        if age == '0':
            return const.EX3_EXIT
        try:
            age = int(age)
        except Exception as err:
            rc.print(f'Input value error: {err}', style=const.DANGER_STYLE)
            continue

        if age > 150:
            rc.print(const.EX3_GOT_BAD_AGE, style=const.DANGER_STYLE)
            continue

        spelling_year = 'років'
        last_number = str(age)[-1]
        if last_number =='1':
            spelling_year = 'рік'
        if last_number in ('2','3','4'):
            spelling_year = 'роки'

        if age % 10 == 7 or age / 10 == 7:
            rc.print(const.EX3_AGE_HAVE_7.format(age=age, years=spelling_year), style=const.SUCCESS_STYLE)
            continue
        elif 65 < age < 120:
            rc.print(const.EX3_MORE_65.format(age=age, years=spelling_year), style=const.SUCCESS_STYLE)
            continue
        elif 0 < age < 7:
            rc.print(const.EX3_LESS_7.format(age=age, years=spelling_year), style=const.SUCCESS_STYLE)
            continue
        elif age < 16:
            rc.print(const.EX3_LESS_16.format(age=age, years=spelling_year), style=const.SUCCESS_STYLE)
            continue
        else:
            rc.print(const.EX3_ANOTHER_AGE.format(age=age, years=spelling_year), style=const.SUCCESS_STYLE)
            continue


def run_app():
    '''
    :param case_number: is an integer number of chose case
    :return: nothing
    '''
    while True:

        case_number = choose_your_case()
        if not case_number:
            rc.print(const.GOODBYE)
            return

        # case 1
        if case_number == 1:
            rc.print(const.EX1_GREETING)
            value = rc.input(const.EX1_ASK_ANY_VALUE)
            if not value:
                rc.print(const.EX1_INPUT_VALUE_ERROR, style=const.DANGER_STYLE)
                continue
            rc.print(get_float_number(any_value=value), style=const.WARNING_STYLE)
            rc.print(const.ASK_TO_CONTINUE)

        # case 2
        if case_number == 2:
            rc.print(const.EX2_GREETING)
            first_argument = rc.input(const.EX2_ASK_FIRST_ARG)
            if not first_argument:
                rc.print(const.EX2_ARG_INPUT_ERROR, style=const.DANGER_STYLE)
                continue

            second_argument = rc.input(const.EX2_ASK_SECOND_ARG)
            if not second_argument:
                rc.print(const.EX2_ARG_INPUT_ERROR, style=const.DANGER_STYLE)
                continue

            rc.print(operation_with_arguments(arg1=first_argument, arg2=second_argument),
                     style=const.SUCCESS_STYLE)
            rc.print(const.ASK_TO_CONTINUE)

        # # case 3
        else:
            rc.print(const.EX3_GREETING)
            cashier_in_the_cinema()
            rc.print(const.ASK_TO_CONTINUE)


rc.print(Panel(const.GREETING, title=const.GREETING_TITLE))
run_app()
