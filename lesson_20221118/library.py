from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from datetime import datetime
import random
import socket
import constants as const

rc = Console()


def get_player_figure(rules):
    '''
    No input param.
    function return a chosen figure by player. There are only three figures to select.
    1 = rock
    2 = scissors
    3 = paper

    Returns: str
    '''
    player_figure = int(Prompt.ask('\nChoose your figure',
                                   choices=['1', '2', '3'],
                                   show_choices=False
                                   ))
    return list(rules.keys())[player_figure - 1]


def get_pc_figure(rules):
    '''
    No input param.
    function return a chosen figure by PC (random value). There are only three figures to select.
    Returns:

    '''

    pc_figure = random.choice(list(rules.keys()))
    return pc_figure


def create_score(player_1, player_2=socket.gethostname().capitalize()):

    return {player_1: 0,
            player_2: 0}


def update_players_scores(scores,  player_name=''):
    '''
    Function updates the score of entered player name as param
    Args:
        scores: a dictionary with username and score data
        player_name: str - player name which score needs to update

    Returns: dict of scores

    '''
    if player_name:
        scores[player_name] += 1
        return scores
    return scores


def get_player_name(scores, i = 0):
    '''
    Function returns player name of index 'i' from dictionary 'scores'
    Args:
        scores: a dictionary with username and score data
        i: index of list of 'scores' keys

    Returns: str (player name)

    '''
    return list(scores.keys())[i]


def get_count_iterations():
    '''
    Function is without input parameters.
    Asks user and returns count of game iterations. If user didn't enter any value, func return three (3) by default

    Returns: int (count of iterations)
    '''

    iterations_count = 3
    try:
        iterations_count = int(rc.input(const.ASK_COUNT_ITERATION))
    except:
        rc.print(const.EXCEPTION_MASSAGE, style='red')

    return iterations_count


def save_to_log(data):
    '''
    Function writes log in file games.
    If the file does not exist, it will be created automatically. The data in the file is appended
    Args:
        data: str

    Returns: None

    '''
    with open(const.LOG_FILE, 'a') as log:
        log.write(data)


def get_game_results(rules, scores, iterations = 3):
    '''
    The function receives and checks the results of one iteration of the game,
    outputs a result message, and sends the scores to update the overall scores.
    The function is launched recursively.
    Args:
        rules: rules of game (is a constant)
        scores: dict of general scores
        iterations: count of game iteration

    Returns: None

    '''

    player_1 = get_player_name(scores, 0)                               # for get players names
    player_2 = get_player_name(scores, 1)

    player_1_chose = get_player_figure(rules=rules)                                # for get players selection
    player_2_chose = get_pc_figure(rules=rules)

    save_to_log(f'iteration {iterations}\n'                             # add players and selections to log-file
                f' - {player_1}: {player_1_chose}\n'
                f' - {player_2}: {player_2_chose}\n\n'
                )

    if player_1_chose == player_2_chose:
        rc.print(Panel.fit(f'Your chosen is [bold]{player_1_chose}[/bold]\n'
                           f'PC chosen is [bold]{player_2_chose}[/bold]', title=const.TITLE_STEP),
                 style=const.INFO_STYLE)

    if rules.get(player_1_chose) == player_2_chose:
        update_players_scores(scores=scores, player_name=player_1)      # call the function to update a general
                                                                        # result for player_1
        rc.print(Panel.fit(f'Your chosen is [bold]{player_1_chose}[/bold]\n'
                           f'PC chosen is [bold]{player_2_chose}[/bold]', title=const.TITLE_STEP),
                style=const.SUCCESS_STYLE
                 )

    if rules.get(player_2_chose) == player_1_chose:
        update_players_scores(scores=scores, player_name=player_2)      # call the function to update a general
                                                                        # result for player_2
        rc.print(Panel.fit(f'Your chosen is [bold]{player_1_chose}[/bold]\n'
                           f'PC chosen is [bold]{player_2_chose}[/bold]', title=const.TITLE_STEP),
                 style=const.DANGER_STYLE)

    if iterations > 1:                                                  # do next iteration
        get_game_results(rules, scores, iterations-1)


def get_winner(general_scores):
    '''
    The function analyzes the results of the game and returns the winner or indicates a draw.
    Args:
        game_result: dict of general game scores (includes scores and players names)

    Returns: str (winner or draw)

    '''

    player_1 = get_player_name(general_scores, 0)
    player_2 = get_player_name(general_scores, 1)

    # to compare players' total scores and return result
    if general_scores.get(player_1) > general_scores.get(player_2):
        return f'The winner is {player_1} with the score {general_scores.get(player_1)}'

    if general_scores.get(player_1) < general_scores.get(player_2):
        return f'The winner is {player_2} with the score {general_scores.get(player_2)}'
    return 'The result is a draw'


def run_game(player_name):
    '''
    Application launch function.
    Does not accept or return any parameters or values
    Returns: nothing

    '''

    save_to_log(datetime.now().strftime('%d.%m.%Y %H:%m')+'\n')
    scores = create_score(player_1=player_name)
    count_of_iterations = get_count_iterations()

    get_game_results(rules=const.RULE_OF_GAMES,
                     scores=scores,
                     iterations=count_of_iterations)
    update_score = update_players_scores(scores)
    winner = get_winner(general_scores=update_score)
    save_to_log(f'We have a {const.WINNER_TITLE}: {winner} \n\n')

    return winner
