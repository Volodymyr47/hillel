# Rock Scissors Paper

from rich.console import Console
from rich.panel import Panel

from library import run_game
from constants import WINNER_TITLE, SUCCESS_STYLE


rc = Console()


if __name__ == '__main__':
    rc.print('\n', Panel(run_game(), title=WINNER_TITLE),
             style=SUCCESS_STYLE)
