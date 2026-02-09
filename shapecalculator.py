from abc import ABC, abstractmethod

class GeometricShape(ABC):
    """Abstract base class for all geometric shapes."""
    def __init__(self, color: str):
        self.color = color

    @abstractmethod
    def area(self) -> float:
        """Calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """Calculate the perimeter of the shape."""
        pass

    def get_description(self) -> str:
        """Return a string description of the shape."""
        return f"A {self.color} {self.__class__.__name__}"

class Rectangle(GeometricShape):
    """A class representing a rectangle, inherited from GeometricShape."""
    def __init__(self, width: float, height: float, color: str):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

class Square(Rectangle):
    """A class representing a square, inherited from Rectangle."""
    def __init__(self, side: float, color: str):
        # A square is a rectangle where width == height
        super().__init__(width=side, height=side, color=color)

    def get_description(self) -> str:
        return f"A {self.color} Square with side length {self.width}"

# --- Example Usage ---
if __name__ == "__main__":
    # Create a rectangle
    rect = Rectangle(width=10, height=5, color="red")
    print(f"Rectangle Area: {rect.area()}")          # Output: 50
    print(f"Rectangle Perimeter: {rect.perimeter()}") # Output: 30

    # Create a square (inherits area/perimeter calculation from Rectangle)
    sq = Square(side=7, color="blue")
    print(f"Square Area: {sq.area()}")               # Output: 49
    print(f"Square Perimeter: {sq.perimeter()}")      # Output: 28
    print(sq.get_description())