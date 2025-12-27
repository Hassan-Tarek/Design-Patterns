"""
Docstring for creational.prototype

Prototype:
  is a creational design pattern that lets you copy existing objects
  without making your code dependent on their classes.
"""
from abc import ABC, abstractmethod
import copy

class Shape(ABC):
  def __init__(self, x: int, y: int):
    self.x = x
    self.y = y

  @abstractmethod
  def clone(self):
    pass

  def __str__(self):
    return f"{self.__class__.__name__}(x={self.x}, y={self.y})"


class Rectangle(Shape):
  def __init__(self, x: int, y: int, width: int, height: int):
    super().__init__(x, y)
    self.width = width
    self.height = height

  def clone(self):
    return copy.deepcopy(self)

  def __str__(self):
    return (
      f"{self.__class__.__name__}("
      f"x={self.x}, y={self.y}, "
      f"width={self.width}, height={self.height})"
    )


class Circle(Shape):
  def __init__(self, x: int, y: int, radius: int):
    super().__init__(x, y)
    self.radius = radius

  def clone(self):
    return copy.deepcopy(self)

  def __str__(self):
    return (
      f"{self.__class__.__name__}("
      f"x={self.x}, y={self.y}, radius={self.radius})"
    )


if __name__ == "__main__":
  rectangle1 = Rectangle(10, 20, 100, 200)
  rectangle2 = rectangle1.clone()

  rectangle2.width = 300

  print(rectangle1)
  print(rectangle2)

  circle1 = Circle(5, 5, 50)
  circle2 = circle1.clone()

  circle2.radius = 75

  print(circle1)
  print(circle2)
