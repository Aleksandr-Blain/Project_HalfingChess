from creatures import *
import random


class Dungeon:
    def __init__(self, height: int, width: int, villains: List[Villain] = []):
        if not (4 <= height <= 12):
            raise ValueError("Height must be between 4 and 12")
        if not (4 <= width <= 12):
            raise ValueError("Width must be between 4 and 12")

        self.__height == height
        self.__width == width


        @property
        def height(self):
            return self.__height

        @property
        def width(self):
            return self.__width

        @property
        def board(self):
            return self.__board

        @board.setter
        def board(self, value):
            self.__board = value

        @property
        def player(self):
            return self.__player

        @property
        def heroes(self):
            return self.__heroes

        @heroes.setter
        def heroes(self, value):
            self.__heroes = value

        @property
        def villains(self):
            return self.__villains

        @villains.setter
        def villains(self, value):
            self.__villains = value