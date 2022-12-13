# Доопрацюйте всі реревірки на типи даних (x, y в Point, begin, end в Line, etc) - зробіть перевірки
# за допомогою property або класса-дескриптора.
# Доопрацюйте класс Triangle з попередньої домашки наступним чином:
#  - обʼєкти классу Triangle можна порівнювати між собою (==, !=, >, >=, <, <=) за площею.
#  - перетворення обʼєкту классу Triangle на стрінг показує координати його вершин
# у форматі x1, y1 -- x2, y2 -- x3, y3

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from figure import Triangle
from library import get_point_from_input, choice_of_task
import constant as const


rc = Console()


rc.print(Panel(const.INTRODUCTION,
               style=const.WELCOME_STYLE,
               title=const.WELCOME_TITLE
               ))
while True:
    choice_result = choice_of_task()

    if choice_result == 'exit':
        break

    if choice_result == '1':
        point1 = get_point_from_input(number_of=1)
        point2 = get_point_from_input(number_of=2)
        point3 = get_point_from_input(number_of=3)

        triangle = Triangle(point1, point2, point3)
        rc.print(Panel.fit(const.AREA_RESULT.format(area=triangle.area()),
                           title=const.RESULT_TITLE,
                           style=const.RESULT_STYLE))

    if choice_result == '2':
        point1_A = get_point_from_input(number_of=1, figure_name=' A')
        point2_A = get_point_from_input(number_of=2, figure_name=' A')
        point3_A = get_point_from_input(number_of=3, figure_name=' A')

        triangle_A = Triangle(point1_A, point2_A, point3_A)

        point1_B = get_point_from_input(number_of=1, figure_name=' B')
        point2_B = get_point_from_input(number_of=2, figure_name=' B')
        point3_B = get_point_from_input(number_of=3, figure_name=' B')

        triangle_B = Triangle(point1_B, point2_B, point3_B)

        rc.print(const.FIGURE_INFO.format(vertices_A=triangle_A,
                                          vertices_B=triangle_B),
                 style=const.COMPARE_STYLE)
        rc.print(const.COMPARING_TASK)
        while True:
            ask = Prompt.ask(const.ASK_OPERATION,
                             choices=['1', '2', '3', '4', '5', '6', 'exit'],
                             show_choices=False)

            if ask == 'exit':
                break

            if ask == '1':
                rc.print(triangle_A == triangle_B)
                continue
            elif ask == '2':
                rc.print(triangle_A != triangle_B)
                continue
            elif ask == '3':
                rc.print(triangle_A > triangle_B)
                continue
            elif ask == '4':
                rc.print(triangle_A < triangle_B)
                continue
            elif ask == '5':
                rc.print(triangle_A >= triangle_B)
                continue
            elif ask == '6':
                rc.print(triangle_A <= triangle_B)
                continue
    continue
