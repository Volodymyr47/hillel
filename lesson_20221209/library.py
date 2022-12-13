from figure import Point
from rich.console import Console
from rich.prompt import Prompt
import constant as const


rc = Console()


def choice_of_task():
    choice = Prompt.ask(const.CHOICE_OF_TASK, choices=['1', '2', 'exit'], show_choices=False)
    return choice


def can_be_float(value: str) -> bool:
    try:
        float(value)
        return True
    except TypeError as terr:
        print(terr)
    except ValueError as verr:
        print(verr)
    return False


def get_point_from_input(number_of: int, figure_name: str = '') -> Point:
    if not isinstance(number_of, int):
        raise TypeError
    while True:
        rc.print(const.POINT.format(number_of=number_of, figure_name=figure_name))

        x = rc.input(const.ASK_X)
        if x == 'exit':
            exit(0)
        if not can_be_float(x):
            continue
        y = rc.input(const.ASK_Y)
        if y == 'exit':
            exit(0)
        if not can_be_float(y):
            continue
        break

    fx = float(x)
    fy = float(y)

    return Point(fx, fy)
