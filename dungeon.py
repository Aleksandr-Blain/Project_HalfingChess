from creatures import *
import random


class Dungeon:
    def __init__(self, height: int, width: int, villains: List[Villain]=[]):
        self.__height = height
        self.__width = width
        self.__villains = self.generate_villains

    def generate_villains(self):
        num_villains = random.randint(1, max(self.__height, self.__width))
        necromance = False
        villain_lst = list()

        for i in range(num_villains):
            percentage = random.randint(1, 10)
            if percentage <= 5:
                villain_lst.append(Goblin())
            elif 6 <= num_villains <= 8:
                villain_lst.append(Skeleton())
            else:
                if necromance:
                    villain_lst.append(Skeleton())
                else:
                    villain_lst.append(Necromancer())
                    necromance = True
            return villain_lst
