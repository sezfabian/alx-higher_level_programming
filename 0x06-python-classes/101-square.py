#!/usr/bin/python3
""" Square module """


class Square:
    """ Square class """

    def __init__(self, size=0, position=(0, 0)):
        """ Initializes the data """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ Returns the size of a square instance """
        return self.__size

    @size.setter
    def size(self, value):
        """ Sets the size of a Square instance """
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        """ Returns the position of a square instance """
        return self.__position

    @position.setter
    def position(self, value):
        """ Sets the position of a square instance """
        if type(value) == tuple and len(value) == 2 \
                and isinstance(value[0], int) and value[0] >= 0 \
                and isinstance(value[1], int) and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """ Calculates de square's area """
        return self.__size ** 2

    def my_print(self):
        """ Prints in stdout the square with the character '#' """
        if self.__size == 0:
            print()
        else:
            print(self.__position[1] * "\n", end="")
            for i in range(self.__size):
                print(self.__position[0] * " " + self.__size * "#")

    def __str__(self):
        """ Returns a string with the square with the character '#' """
        string = ""
        if self.__size == 0:
            string += "\n"
        else:
            string += self.__position[1] * "\n"
            for i in range(self.__size):
                string += self.__position[0] * " " + self.__size * "#" + "\n"
        return(string[:-1])
