# styles
SUCCESS_STYLE = 'bold white on green'
GREETING_STYLE = 'bold green'
INFO_STYLE = 'bold white on blue'
WINNER_STYLE = 'bold white on rgb(6,165,59)'
WARNING_STYLE = 'bold yellow'

# main
GREETING_TITLE = 'Greeting and rules'
GREETING = '[bold green]Hello.\nNow we are playing the game of "Rock Scissors Paper lizard spock"\n' \
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

FIRST_PLAYER_TYPE = '[bold]First player[/bold]:\n' \
                    ' - enter [bold blue]0[/bold blue] to select a [blue]virtual player[/blue]' \
                    '\n - enter [bold blue]1[/bold blue] to select a [blue]human player[/blue]' \
                    '\nPlease make choice'

SECOND_PLAYER_TYPE = '\n[bold]Second player[/bold]:\n' \
                     ' - enter [bold blue]0[/bold blue] to select a [blue]virtual player[/blue]' \
                     '\n - enter [bold blue]1[/bold blue] to select a [blue]human player[/blue]' \
                     '\nPlease make choice'

EXCEPTION_MASSAGE = 'Entered value is wrong.\n By default you will repeat three times'
ASK_COUNT_ITERATION = '\n[bold]How many times do you plan to play?[/bold] \n' \
                      '(only positive numbers greater than zero, e.g. 1, 3, 5 etc. Default - 3): '

ASK_FIRST_NAME = '\n[bold]Please name the first player[/bold]: '
ASK_SECOND_NAME = '\n[bold]Please name the second player[/bold]: '

ASK_TO_CONTINUE = '\nTo exit - type "exit", or another key to continue > '

WINNER_TITLE = 'WINNER!'
DRAW_TITLE = 'DRAW!'
WINNER = 'Winner of the game is {winner} with the following score:\n' \
         '[bold white]{player1}[/bold white]: [bold white]{first_player_score}[/bold white]\n' \
         '[bold white]{player2}[/bold white]: [bold white]{second_player_score}[/bold white]\n'
DRAW_RESULT = 'We have a draw with the following score:\n' \
              '[bold white]{player1}[/bold white]: [bold white]{first_player_score}[/bold white]\n' \
              '[bold white]{player2}[/bold white]: [bold white]{second_player_score}[/bold white]\n'

GOODBYE = '[bold white on green blink]Have a nice day![/bold white on green blink]'
LOG_FILE = 'games.log'
