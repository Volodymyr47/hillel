from abc import ABC, abstractmethod
from math import sqrt


class Point:
    _coordinate_x = None
    _coordinate_y = None

    def __init__(self, value_x, value_y):
        self.x = value_x
        self.y = value_y

    def __str__(self):
        return f'{self._coordinate_x}, {self._coordinate_y}'

    @property
    def x(self):
        '''
        Property
        :return: attribute _coordinate_x
        '''
        return self._coordinate_x

    @x.setter
    def x(self, x_value):
        '''
        Checks x_value for type of int or float
        :param x_value:
        :return: None
        '''
        if not isinstance(x_value, (int, float)):
            raise TypeError('Value of x-coordinate must be integer or float')
        self._coordinate_x = x_value

    @property
    def y(self):
        '''
        Property
        :return: attribute _coordinate_y
        '''
        return self._coordinate_y

    @y.setter
    def y(self, y_value):
        '''
        Checks y_value for type of int or float
        :param y_value:
        :return: None
        '''
        if not isinstance(y_value, (int, float)):
            raise TypeError('Value of y-coordinate must be integer or float')
        self._coordinate_y = y_value


class Figure(ABC):

    @abstractmethod
    def __init__(self):
        pass

    def area(self):
        pass

    def length(self):
        pass


class Line(Figure):
    _begin = None
    _end = None

    def __init__(self, begin, end):
        self.begin = begin
        self.end = end

    @property
    def begin(self):
        return self._begin

    @begin.setter
    def begin(self, begin_value):
        if not isinstance(begin_value, Point):
            raise TypeError(f'The type of the {begin_value} must be Point')
        self._begin = begin_value

    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, end_value):
        if not isinstance(end_value, Point):
            raise TypeError(f'The type of the {end_value} must be Point')
        self._end = end_value

    def length(self):
        result = sqrt((self._begin.x - self._end.x)**2 + (self._begin.y - self._end.y)**2)
        return result


class Triangle(Figure):
    _point_1 = None
    _point_2 = None
    _point_3 = None

    def __init__(self, point_1, point_2, point_3):

        self.point_1 = point_1
        self.point_2 = point_2
        self.point_3 = point_3

    def __str__(self):
        return f'({self._point_1}) -- ({self._point_2}) -- ({self._point_3})'

    @property
    def point_1(self):
        return self._point_1

    @point_1.setter
    def point_1(self, point_1_value):
        if not isinstance(point_1_value, Point):
            raise TypeError(f'The type of the {point_1_value} must be Point')
        self._point_1 = point_1_value

    @property
    def point_2(self):
        return self._point_2

    @point_2.setter
    def point_2(self, point_2_value):
        if not isinstance(point_2_value, Point):
            raise TypeError(f'The type of the {point_2_value} must be Point')
        self._point_2 = point_2_value

    @property
    def point_3(self):
        return self._point_3

    @point_3.setter
    def point_3(self, point_3_value):
        if not isinstance(point_3_value, Point):
            raise TypeError(f'The type of the {point_3_value} must be Point')
        self._point_3 = point_3_value

    def area(self):
        len_line1 = Line(self._point_1, self._point_2).length()
        len_line2 = Line(self._point_2, self._point_3).length()
        len_line3 = Line(self._point_3, self._point_1).length()

        semi_prmtr = (len_line1 + len_line2 + len_line3) / 2

        result = sqrt(semi_prmtr * (semi_prmtr - len_line1) * (semi_prmtr - len_line2) * (semi_prmtr - len_line3))

        return result

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()
