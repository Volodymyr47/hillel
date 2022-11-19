# Rock Scissors Paper

from rich.console import Console
from rich.panel import Panel
from library import run_game
from constants import (
    WINNER_TITLE,
    SUCCESS_STYLE,
    ASK_PLAYER_NAME,
    GREETING_TITLE,
    GREETING,
    ASK_TO_CONTINUE,
    GOODBYE
)


rc = Console()
player_name = rc.input(ASK_PLAYER_NAME).capitalize() or 'Player'
rc.print(Panel(GREETING.format(player=player_name), title=GREETING_TITLE), style='bold green')

while True:
    rc.print('\n', Panel(run_game(player_name=player_name), title=WINNER_TITLE), style=SUCCESS_STYLE)

    ask_to_continue = rc.input(ASK_TO_CONTINUE)
    if ask_to_continue == '0':
        rc.print(GOODBYE)
        break
