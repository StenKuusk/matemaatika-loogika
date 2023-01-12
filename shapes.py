"""Shapes."""
from abc import ABC, abstractmethod


class Shape(ABC):
    """General shape class."""


    def __init__(self, color: str):
        """Shape constructor."""
        self.__color = color
        pass
    def set_color(self, color: str):
        """Set the color of the shape."""
        self.color(color)
        pass

    def get_color(self) -> str:
        """Get the color of the shape."""
        return self.__color
        pass

    @abstractmethod
    def get_area(self) -> float:
        """Get area method which every subclass has to override."""
        print("Implement area")


class Circle(Shape):
    """Circle is a subclass of Shape."""

    def __init__(self, color: str, radius: float):
        """
        Circle constructor.

        The color is stored using superclass constructor:
        super().__init__(color)

        The radius value is stored here.
        """
        super().__init__(color)
        self.__radius = radius
        pass

    def __repr__(self) -> str:
        """
        Return representation of the circle.

        For this exercise, this should return a string:
        Circle (r: {radius}, color: {color})
        """
        return f"Circle (r: {self.__radius}, color: {self.get_color()})"
        pass

    def get_area(self) -> float:
        """
        Calculate the area of the circle.

        Area of the circle is pi * r * r.
        """
        circle_area = 3.14 * self.__radius * self.__radius
        return circle_area
        pass


class Square(Shape):
    """Square is a subclass of Shape."""

    def __init__(self, color: str, side: float):
        """
        Square constructor.

        The color is stored using superclass constructor:
        super().__init__(color)

        The side value is stored here.
        """
        super().__init__(color)
        self.__side = side
        pass

    def __repr__(self) -> str:
        """
        Return representation of the square.

        For this exercise, this should return a string:
        Square (a: {side}, color: {color})
        """
        return f"Square (a: {self.__side}, color: {self.get_color()})"

        pass

    def get_area(self) -> float:
        """
        Calculate the area of the square.

        Area of the square is side * side.
        """
        square_area = self.__side * self.__side
        return square_area
        pass


class Rectangle(Shape):
    def __init__(self, color: str, side_1: float, side_2: float):
        super().__init__(color)
        self.__side_1 = side_1
        self.__side_2 = side_2

    def __repr__(self):
        return f"Rectangle (a: {self.__side_1}, b: {self.__side_2}, color: {self.get_color()})"

    def get_area(self) -> float:
        rectangle_area = self.__side_1 * self.__side_2
        return rectangle_area



class Paint:
    """The main program to manipulate the shapes."""

    def __init__(self):
        """Paint constructor."""
        self.__shapes = []
        pass

    def add_shape(self, shape: Shape) -> None:
        """Add a shape to the program."""
        self.__shapes.append(shape)
        pass

    def get_shapes(self) -> list:
        """Return all the shapes."""
        return self.__shapes
        pass

    def calculate_total_area(self) -> float:
        """Calculate total area of the shapes."""
        total_area = 0
        for shape in self.__shapes:
            total_area += shape.get_area()
        return total_area
        pass

    def get_circles(self) -> list:
        """Return only circles."""
        circles = []
        for shape in self.__shapes:
            if isinstance(shape, Circle):
                circles.append(shape)
        return circles
        pass

    def get_squares(self) -> list:
        """Return only squares."""
        squares = []
        for shape in self.__shapes:
            if isinstance(shape, Square):
                squares.append(shape)
        return squares
        pass

    def get_rectangles(self) -> list:
        """Return only rectangles."""
        rectangles = []
        for shape in self.__shapes:
            if isinstance(shape, Rectangle):
                rectangles.append(shape)
        return rectangles
        pass


if __name__ == '__main__':
    paint = Paint()
    circle = Circle("blue", 10)
    print(circle)
    print(circle.get_area())
    square = Square("red", 11)
    print(square)
    print(square.get_area())
    rectangle = Rectangle("green", 4, 6)
    print(rectangle)
    print(rectangle.get_area())
    paint.add_shape(circle)
    paint.add_shape(square)
    paint.add_shape(rectangle)
    print(paint.get_shapes())
    print(paint.calculate_total_area())
    print(paint.get_circles())
    print(paint.get_squares())
