# Доопрацюйте класс Point так, щоб в атрибути x та y обʼєктів цього класу можна було записати
# тільки обʼєкти класу int або float
# Доопрацюйте класс Line так, щоб в атрибути begin та end обʼєктів цього класу можна було записати
# тільки обʼєкти класу Point
# Створіть класс Triangle (трикутник), який задається трьома точками (обʼєкти классу Point).
# Реалізуйте перевірку даних, аналогічно до класу Line. Визначет метод, що містить площу трикутника.
# Для обчислень можна використати формулу Герона (https://en.wikipedia.org/wiki/Heron%27s_formula)

from rich.console import Console
from rich.panel import Panel
from figure import Triangle
from library import get_point_from_input
import constant as const


rc = Console()


rc.print(Panel(const.INTRODUCTION,
               style=const.WELCOME_STYLE,
               title=const.WELCOME_TITLE
               ))

point1 = get_point_from_input(number_of=1)
point2 = get_point_from_input(number_of=2)
point3 = get_point_from_input(number_of=3)

triangle = Triangle(point1, point2, point3)

rc.print(Panel.fit(const.AREA_RESULT.format(area=triangle.area()),
                   title=const.RESULT_TITLE,
                   style=const.RESULT_STYLE))
