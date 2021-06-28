from extra.hw_1 import Rectangle, Triangle, Square, Circle


class TestRectangle:
    figure = Rectangle(side_a=4, side_b=6)

    def test_get_rectangle_area(self):
        assert self.figure.get_rectangle_area() == 24

    def test_get_rectangle_perimeter(self):
        assert self.figure.get_rectangle_perimeter() == 20

    def test_get_name_figure_rectangle(self):
        assert self.figure.get_name_figure() == "rectangle"

    def test_get_angles_rectangle(self):
        assert self.figure.get_angles_figure() == 4

    def test_add_area(self):
        circle = Circle(10)
        circle.get_circle_area()
        assert self.figure.add_area(circle) == circle.area + self.figure.area
        assert self.figure.add_area('Not Figure instance') == TypeError


class TestSquare:
    figure = Square(side_a=4, side_b=4)

    def test_get_square_area(self):
        assert self.figure.get_rectangle_area() == 16

    def test_get_square_perimeter(self):
        assert self.figure.get_rectangle_perimeter() == 16

    def test_get_name_figure_square(self):
        assert self.figure.get_name_figure() == "square"

    def test_get_rectangle_angles_square(self):
        assert self.figure.get_angles_figure() == 4

    def test_add_area(self):
        triangle = Triangle(4, 6, 3, 4, 5)
        triangle.get_triangle_area()
        assert self.figure.add_area(triangle) == triangle.area + self.figure.area
        assert self.figure.add_area('Not Figure instance') == TypeError


class TestTriangle:
    figure = Triangle(base=4, height=6, side_a=3, side_b=4, side_c=5)

    def test_get_triangle_area(self):
        assert self.figure.get_triangle_area() == 12

    def test_get_triangle_perimeter(self):
        assert self.figure.get_triangle_area() == 12

    def test_get_name_figure_triangle(self):
        assert self.figure.get_name_figure() == "triangle"

    def test_get_angles_triangle(self):
        assert self.figure.get_angles_figure() == 3

    def test_add_area(self):
        rect = Rectangle(side_a=4, side_b=6)
        rect.get_rectangle_area()
        assert self.figure.add_area(rect) == rect.area + self.figure.area
        assert self.figure.add_area('Not Figure instance') == TypeError


class TestCircle:
    figure = Circle(radius=10)

    def test_get_circle_area(self):
        assert self.figure.get_circle_area() == 314.1592653589793

    def test_get_circle_perimeter(self):
        assert self.figure.get_circle_perimeter() == 62.83185307179586

    def test_get_name_figure_circle(self):
        assert self.figure.get_name_figure() == "circle"

    def test_get_angles_circle(self):
        assert self.figure.get_angles_figure() == 0

    def test_add_area(self):
        square = Square(4, 4)
        square.get_rectangle_area()
        assert self.figure.add_area(square) == square.area + self.figure.area
        assert self.figure.add_area('Not Figure instance') == TypeError
