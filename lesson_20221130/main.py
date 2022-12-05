from rich.console import Console
from rich.panel import Panel
from library import numbers_multiplication_exponent


rc = Console()


# start app
rc.print(Panel.fit('\nPlease, enter below the correct values of numbers to get the result of operation\n'
                   '[underline]Attention[/underline]:\n'
                   'a) exponent value must be <= 100\n'
                   'b) large float value of numbers can return an error',
                   style='bold yellow'))

while True:
    number1 = number2 = exp = 0.0

    try:
        number1 = float(rc.input('[bold green]First number:[/bold green] '))
        number2 = float(rc.input('[bold green]Second number:[/bold green] '))
        exp = float(rc.input('[bold green]Exponent value:[/bold green] '))
    except ValueError as err:
        rc.print(f'[bold red]Entered value is wrong.\n'
                 f'Details of error: {err}[/bold red]\n'
                 f'[bold yellow]Please try again and be careful![/bold yellow]\n')
        continue

    result = numbers_multiplication_exponent(number1, number2, exponent=exp)
    rc.print(Panel(f'The result is: {result}', style='bold white on green', title='Functions result'))
    rc.print('Have a nice day. Goodbye!\n', style='bold blue')
    exit(0)
