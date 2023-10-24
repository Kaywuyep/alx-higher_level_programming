#!/usr/bin/python3


class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.postion = position


    @property
    def size(self):
        return self.__size


    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value


    @property
    def position(self):
        return self.__position


    @size.setter
    def position(self, value):
        if type(position) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position


    def area(self):
        return (self.__size ** 2)


    def my_print(self):
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                for i in range(self.__size):
                    print("#", end="")
                print()
