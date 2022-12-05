class Vehicle:
    weight = 0
    max_speed = 0
    length = 0
    width = 0
    height = 0
    power_source = ''

    def get_vehicle_info(self):
        pass


class Car(Vehicle):
    passenger_capacity = 5

    def __init__(self, model, year, made):
        self.model = model
        self.year = year
        self.made = made

    def get_vehicle_info(self):
        info = f'\nThe car is {self.model} made in {self.year} by {self.made}\n'\
               f'\nTechnical parameters:\n'\
               f'Power source: {self.power_source}\n'\
               f'Weight: {self.weight} kg\n'\
               f'Max speed: {self.max_speed} kph\n'\
               f'Length: {self.length} cm\n'\
               f'Width: {self.width} cm\n'\
               f'Height: {self.height} cm\n'\
               f'Passenger capacity: {self.passenger_capacity}\n'
        return info


class Ship(Vehicle):
    max_speed = 23
    length = 26910
    width = 2819
    height = 1850
    displacement = 52310

    def __init__(self, model, year, made):
        self.model = model
        self.year = year
        self.made = made

    def get_vehicle_info(self):
        info = f'\nThe ship is {self.model} made in {self.year} by {self.made}\n' \
               f'\nTechnical parameters:\n' \
               f'Max speed: {self.max_speed} kt\n' \
               f'Length: {self.length} cm\n' \
               f'Width: {self.width} cm\n' \
               f'Height: {self.height} cm\n' \
               f'Displacement: {self.displacement}\n'
        return info


class Plane(Vehicle):
    model = 'Myplane'
    year = 2022
    made = 'Ukraine'
    max_speed = 950
    length = 25
    width = 4
    height = 8
    power_source = 'gasoline'
    passenger_capacity = 8

    def get_vehicle_info(self):
        info = f'\nThe plane is {self.model} made in {self.year} by {self.made}\n' \
               f'\nTechnical parameters:\n' \
               f'Max speed: {self.max_speed} kph\n'\
               f'Length: {self.length} cm\n' \
               f'Width: {self.width} cm\n' \
               f'Height: {self.height} cm\n' \
               f'Passenger capacity: {self.passenger_capacity}\n'
        return info
