from vehicle import Car
from vehicle import Ship
from vehicle import Plane
from rich.console import Console
from rich.panel import Panel


rc = Console()


car = Car('BMW', 2002, 'German')
setattr(car, 'weight', 1600)
setattr(car, 'max_speed', 260)
setattr(car, 'length', 250)
setattr(car, 'width', 160)
setattr(car, 'height', 120)
setattr(car, 'power_source', 'diesel')
setattr(car, 'passenger_capacity', 5)
rc.print(Panel.fit(car.get_vehicle_info(), style='bold white on rgb(114,111,109)', title='Car'))


ship = Ship('Titanic', 1912, 'Great Britain')
rc.print(Panel.fit(ship.get_vehicle_info(), style='bold white on rgb(114,49,10)', title='Ship'))


plane = Plane()
rc.print(Panel.fit(plane.get_vehicle_info(), style='bold yellow on rgb(3,67,107)', title='Plane'))
