import math


class Figure:
    def __init__(self, name, angles):
        self.name = name,
        self.angles = angles

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


class Rectangle(Figure):
    name = "rectangle"
    angles = 4

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_rectangle_area(self):
        return self.width * self.height

    def get_rectangle_perimeter(self):
        return 2 * (self.width + self.height)


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
