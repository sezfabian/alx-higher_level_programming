#!/usr/bin/python3
"""Rectangle Class Module"""


class Rectangle:
    """defines class Rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initializes Rectangle"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """returns Rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets Rectangle width value of rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """returns Rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets Rectangle height value of rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        """returns area of Rectangle"""
        return self.width * self.height

    def perimeter(self):
        """returns perimeter of Rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.height + self.width)

    def __str__(self):
        """returns class Rectangle as a string"""
        if self.height == 0 or self.width == 0:
            return ""

        rect = ""
        for i in range(self.height):
            rect += str(self.print_symbol) * self.width
            if i < self.height - 1:
                rect += '\n'
        return rect

    def __repr__(self):
        """returns accurate rep string of class instance"""
        if self.height == 0 and self.width == 0:
            return "Rectangle()"
        if self.width != 0 and self.height == 0:
            return "Rectangle({})".format(self.width)
        if self.height != 0:
            return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """Prints text on deletion of an instance of the rectangle class"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance with width == height == size"""
        return cls(size, size)
