from exchangerate import ExchangeRate
from rich.console import Console
from rich.panel import Panel

import constant as const


rc = Console()

rc.print(Panel(const.GREATING_TEXT, title=const.GREATING_TITLE))

while True:
    user_date = rc.input(const.INPUT_REQUEST) or ''

    if user_date == 'exit':
        rc.print(const.GOODBYE)
        break

    exchange_rate = ExchangeRate(user_date)
    if exchange_rate.saved_to_file():
        rc.print(const.RESULT.format(exchange_rate.get_file_name()))
