from rspgame import MainGame
from rich.prompt import Prompt
from rich.console import Console
from rich.panel import Panel
import constants as const


rc = Console()

rc.print(Panel(const.GREETING, title=const.GREETING_TITLE), style=const.GREETING_STYLE)

first_player_type = Prompt.ask(const.FIRST_PLAYER_TYPE,
                               choices=['0', '1'],
                               show_choices=False
                               )
first_player_name = rc.input(const.ASK_FIRST_NAME)

second_player_type = Prompt.ask(const.SECOND_PLAYER_TYPE,
                                choices=['0', '1'],
                                show_choices=False
                                )
second_player_name = rc.input(const.ASK_SECOND_NAME)

gamer1 = MainGame(first_player_name, is_human=int(first_player_type))
gamer2 = MainGame(second_player_name, is_human=int(second_player_type))

while True:
    count_iterations = rc.input(const.ASK_COUNT_ITERATION)
    iterations = 0
    if count_iterations:
        try:
            iterations = int(count_iterations)
        except ValueError as err:
            rc.print(err, style=const.WARNING_STYLE)
            continue

    winner = gamer1.play_game(gamer2, iterations=iterations)

    if winner:
        rc.print(Panel(const.WINNER.format(winner=winner,
                                           player1=gamer1.player,
                                           player2=gamer2.player,
                                           first_player_score=gamer1.player.get_score(),
                                           second_player_score=gamer2.player.get_score()),
                       title=const.WINNER_TITLE
                       ),
                 style=const.WINNER_STYLE)
    else:
        rc.print(Panel(const.DRAW_RESULT.format(player1=gamer1.player,
                                                player2=gamer2.player,
                                                first_player_score=gamer1.player.get_score(),
                                                second_player_score=gamer2.player.get_score()),
                       title=const.DRAW_TITLE
                       ),
                 style=const.INFO_STYLE)

    ask_to_continue = rc.input(const.ASK_TO_CONTINUE)
    if ask_to_continue == 'exit':
        rc.print(const.GOODBYE)
        break
