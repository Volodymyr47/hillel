# styles
SUCCESS_STYLE = 'bold white on green'
INFO_STYLE = 'bold white on blue'
WARNING_STYLE = 'bold yellow'
DANGER_STYLE = 'bold white on red'
WINNER_STYLE = 'bold white on rgb(6,165,59)'

# main
GREETING_TITLE = 'Greeting and rules'
GREETING = '[bold green]Hello, {player}.\nNow we are playing the game of "Rock Scissors Paper lizard spock"\n' \
           'We have to follow the following rules.[/bold green]\n' \
           'You have three figures:\n' \
           ' [blue]ROCK (press "1" to select this one)[/blue]\n' \
           ' [blue]SCISSORS (press "2" to select this one)[/blue]\n' \
           ' [blue]PAPER (press "3" to select this one)[/blue]\n\n' \
           '[bold yellow]Rules:[/bold yellow]\n' \
           ' - if you chose rock and I chose scissors - you winn\n' \
           ' - if you chose scissors and I chose paper - you winn\n' \
           ' - if you chose paper and I chose rock - you winn\n' \
           ' - if we chose the same values we got a draw\n' \
           ' - else - you have lost\n' \
           'If you agree let\'s start!\n'

EXCEPTION_MASSAGE = 'Entered value is wrong.\n By default you will repeat three times'
ASK_COUNT_ITERATION = 'How many times do you plan to play? ' \
                      '(type only integer value, e.g. 1, 3, 5 etc. Default - 3): '

ASK_PLAYER_NAME = '[blue bold]Welcome.\n' \
                  'For a more comfortable game, enter your name.\n' \
                  'In another case your name will be a "Player"\n' \
                  'Your name is: [/blue bold]'

ASK_TO_CONTINUE = '\nTo exit - press "0", or another key to continue > '
TITLE_STEP = 'One step result'
WINNER_TITLE = 'WINNER!'
GOODBYE = '[bold white on green blink]Have a nice day![/bold white on green blink]'
LOG_FILE = 'games.log'

# games rules
RULE_OF_GAMES = {'ROCK': 'SCISSORS',
                 'SCISSORS': 'PAPER',
                 'PAPER': 'ROCK'
                 }


