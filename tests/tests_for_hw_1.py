from extra.hw_1 import Rectangle, Triangle, Square, Circle


class TestRectangle:
    def test_get_rectangle_area(self):
        rectangle = Rectangle(width=4, height=6)
        assert rectangle.get_rectangle_area() == 24

    def test_get_rectangle_perimeter(self):
        rectangle = Rectangle(width=4, height=6)
        assert rectangle.get_rectangle_perimeter() == 20

    def test_get_name_figure_rectangle(self):
        rectangle = Rectangle(width=4, height=6)
        assert rectangle.get_name_figure() == "rectangle"

    def test_get_angles_rectangle(self):
        rectangle = Rectangle(width=4, height=6)
        assert rectangle.get_angles_figure() == 4


class TestSquare:
    def test_get_square_area(self):
        square = Square(width=4, height=6)
        assert square.get_rectangle_area() == 24

    def test_get_square_perimeter(self):
        square = Square(width=4, height=6)
        assert square.get_rectangle_perimeter() == 20

    def test_get_name_figure_square(self):
        square = Square(width=4, height=6)
        assert square.get_name_figure() == "square"

    def test_get_rectangle_angles_square(self):
        square = Square(width=4, height=6)
        assert square.get_angles_figure() == 4


class TestTriangle:
    def test_get_triangle_area(self):
        triangle = Triangle(base=4, height=6, side_a=3, side_b=4, side_c=5)
        assert triangle.get_triangle_area() == 12

    def test_get_triangle_perimeter(self):
        triangle = Triangle(base=4, height=6, side_a=3, side_b=4, side_c=5)
        assert triangle.get_triangle_area() == 12

    def test_get_name_figure_triangle(self):
        triangle = Triangle(base=4, height=6, side_a=3, side_b=4, side_c=5)
        assert triangle.get_name_figure() == "triangle"

    def test_get_angles_triangle(self):
        triangle = Triangle(base=4, height=6, side_a=3, side_b=4, side_c=5)
        assert triangle.get_angles_figure() == 3


class TestCircle:
    def test_get_circle_area(self):
        circle = Circle(radius=10)
        assert circle.get_circle_area() == 314.1592653589793

    def test_get_circle_perimeter(self):
        circle = Circle(radius=10)
        assert circle.get_circle_perimeter() == 62.83185307179586

    def test_get_name_figure_circle(self):
        circle = Circle(radius=10)
        assert circle.get_name_figure() == "circle"

    def test_get_angles_circle(self):
        circle = Circle(radius=10)
        assert circle.get_angles_figure() == 0
