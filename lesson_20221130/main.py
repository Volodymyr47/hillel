from rich.console import Console
from library import numbers_multiplication_in_exponent

rc = Console()

rc.print('Please, enter the correct values of numbers for get the result of operation')
while True:
    number1 = number2 = exp = 0.0
    try:
        number1 = float(rc.input('[bold green]First number:[/bold green] '))
        number2 = float(rc.input('[bold green]Second number:[/bold green] '))
        exp = float(rc.input('[bold green]Exponent value:[/bold green] '))
    except ValueError as err:
        rc.print(f'[bold red]Entered value is wrong.\n'
                 f'Details of error: {err}\n[/bold red]'
                 f'[bold orange]Please try again and be careful![/bold orange]')
        continue
    result = numbers_multiplication_in_exponent(number1, number2, exponent=exp)
    rc.print(f'The result is: {result} \n\n'
             f'Have a nice day. Goodbye!')
    exit(0)
