from abc import ABC, abstractmethod
import math

class Polygon():
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Polygon):
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width
    
    def perimeter(self):
        return (2 * self.__length) + (2 * self.__width)

class Square(Rectangle):
    def __init__(self, length):
        self.__length = length
        self.__width = length

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return (2 * self.__length) + (2 * self.__width)


class RightTriangle(Polygon):
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return (self.__length * self.__width) / 2

    def perimeter(self):
        return self.__length + self.__width + math.sqrt((self.__length * self.__length) + (self.__width * self.__width))


print("testing")
rect = Rectangle(2, 3)
print(rect.area())
print(rect.perimeter())
square = Square(4)
print(square.area())
print(square.perimeter())
triangle = RightTriangle(3,4)
print(triangle.area())
print(triangle.perimeter())