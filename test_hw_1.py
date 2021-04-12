import math


class Figure:
    def __init__(self, name, area, angles, perimeter):
        self.name = name,
        self.area = area,
        self.angles = angles,
        self.perimeter = perimeter


class Triangle(Figure):
    pass


class Rectangle(Figure):
    def __init__(self, width=1.0, height=1.0, number_of_corners=4):
        self.width = width
        self.height = height
        self.number_of_corners = number_of_corners

    def get_rectangle_area(self):
        return self.width * self.height

    def get_rectangle_perimeter(self):
        return 2 * (self.width + self.height)

    def get_rectangle_angles(self):
        return self.number_of_corners

    name = "rectangle"


class Square(Figure):
    def __init__(self, side, number_of_corners=4):
        self.side = side
        self.number_of_corners = number_of_corners

    def get_square_area(self):
        return self.side * self.side

    def get_square_perimeter(self):
        return self.side * 4

    def get_circle_angles(self):
        return self.number_of_corners

    name = "square"


class Circle(Figure):
    def __init__(self, radius=1.0, number_of_corners=0):
        self.radius = radius
        self.number_of_corners = number_of_corners

    def get_circle_area(self):
        return math.pi * self.radius ** 2

    def get_circle_perimeter(self):
        return 2 * math.pi * self.radius

    def get_circle_angles(self):
        return self.number_of_corners

    name = "circle"
