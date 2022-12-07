from abc import ABC, abstractmethod
from math import sqrt


class Point:
    x = None
    y = None

    def __init__(self, x, y):
        if not isinstance(x, (float, int)):
            print('The type of the attribute must be integer or float')
            raise TypeError

        if not isinstance(y, (float, int)):
            print('The type of the attribute must be integer or float')
            raise TypeError

        self.x = x
        self.y = y


class Figure(ABC):

    @abstractmethod
    def __init__(self):
        pass

    def area(self):
        pass

    def length(self):
        pass


class Line(Figure):
    begin = None
    end = None

    def __init__(self, begin, end):

        if not isinstance(begin, Point):
            print('The type of the attribute must be Point')
            raise TypeError

        if not isinstance(end, Point):
            print('The type of the attribute must be Point')
            raise TypeError

        self.begin = begin
        self.end = end

    def length(self):
        result = sqrt((self.begin.x - self.end.x)**2 + (self.begin.y - self.end.y)**2)
        return result


class Triangle(Figure):
    line_1 = None
    line_2 = None
    line_3 = None

    def __init__(self, point_1, point_2, point_3):

        if not isinstance(point_1, Point):
            print('The type of the attribute must be Point')
            raise TypeError

        if not isinstance(point_2, Point):
            print('The type of the attribute must be Point')
            raise TypeError

        if not isinstance(point_3, Point):
            print('The type of the attribute must be Point')
            raise TypeError

        self.line_1 = Line(point_1, point_2)
        self.line_2 = Line(point_2, point_3)
        self.line_3 = Line(point_3, point_1)

    def area(self):
        len_line1 = self.line_1.length()
        len_line2 = self.line_2.length()
        len_line3 = self.line_3.length()

        semi_prmtr = (len_line1 + len_line2 + len_line3) / 2

        result = sqrt(semi_prmtr * (semi_prmtr - len_line1) * (semi_prmtr - len_line2) * (semi_prmtr - len_line3))

        return result
