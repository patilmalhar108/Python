import math

class Shape:
    """Base class for all geometric shapes."""
    def __init__(self, name):
        self.name = name

    def get_area(self):
        """Must be implemented by child classes."""
        raise NotImplementedError("Subclasses must implement get_area()")

    def get_perimeter(self):
        """Must be implemented by child classes."""
        raise NotImplementedError("Subclasses must implement get_perimeter()")

class Rectangle(Shape):
    """A class representing a rectangle, inheriting from Shape."""
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def get_area(self):
        """Compute the area of the rectangle."""
        return self.width * self.height

    def get_perimeter(self):
        """Compute the perimeter of the rectangle."""
        return 2 * (self.width + self.height)

class Square(Rectangle):
    """A class representing a square, inheriting from Rectangle."""
    def __init__(self, side_length):
        # A square is a rectangle where width == height
        super().__init__(side_length, side_length)
        self.name = "Square"

# --- Example Usage ---
if __name__ == "__main__":
    rect = Rectangle(10, 5)
    print(f"{rect.name}: Area = {rect.get_area()}, Perimeter = {rect.get_perimeter()}")

    square = Square(7)
    print(f"{square.name}: Area = {square.get_area()}, Perimeter = {square.get_perimeter()}")
