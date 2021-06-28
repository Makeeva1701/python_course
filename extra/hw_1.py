import math


class Figure:
    name = None
    angles = None
    area = 0

    def get_name_figure(self):
        return self.name

    def get_angles_figure(self):
        return self.angles


class Triangle(Figure):
    name = "triangle"
    angles = 3

    def __init__(self, base, height, side_a, side_b, side_c):
        self.base = base
        self.height = height
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_triangle_area(self):
        return float(0.5 * self.base * self.height)

    def get_triangle_perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def add_area(self, figure):
        if isinstance(figure, Figure):
            return figure.area + self.area
        else:
            return TypeError


class Rectangle(Figure):
    name = "rectangle"
    angles = 4

    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def get_rectangle_area(self):
        return self.side_a * self.side_b

    def get_rectangle_perimeter(self):
        return 2 * (self.side_a + self.side_b)

    def add_area(self, figure):
        if isinstance(figure, Figure):
            return figure.area + self.area
        else:
            return TypeError


class Square(Rectangle):
    name = "square"


class Circle(Figure):
    name = "circle"
    angles = 0

    def __init__(self, radius):
        self.radius = radius

    def get_circle_area(self):
        return math.pi * self.radius ** 2

    def get_circle_perimeter(self):
        return 2 * math.pi * self.radius

    def add_area(self, figure):
        if isinstance(figure, Figure):
            return figure.area + self.area
        else:
            return TypeError
