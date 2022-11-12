# Rock Scissors Paper

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
import random

rules_of_game = {'rock': 'scissors',
                 'scissors': 'paper',
                 'paper': 'rock'
                 }

def get_player_figure():
    player_figure = Prompt.ask('Choose your figure',
                               choices=['rock', 'scissors', 'paper'],
                               show_choices=False
                               )
    return player_figure


def get_ai_figure():
    ai_figure = random.choice(['rock', 'scissors', 'paper'])
    return ai_figure


def define_winner(rules, player_name, ai_name):
    print('You should select only one of the next figure: "rock", "scissors" or "paper"')
    player_chose = get_player_figure()
    ai_chose = get_ai_figure()
    print(f'figures player: {player_chose}, comp: {ai_chose} \n')
    if player_chose == ai_chose:
        return {player_name: 0,
                ai_name: 0}
    for key, value in rules.items():
        if player_chose == key and ai_chose == value:
            print(f'figures player: {player_chose}, comp: {ai_chose}')
            return {player_name: 1,
                ai_name: 0}
        else:
            return {player_name: 0,
                ai_name: 1}


i = 5
while i > 0:
    print(define_winner(rules_of_game, 'Vova', 'Laptop'))
    i -= 1

def save_log(from_player, from_ai):
    pass

# print(get_ai_figure())