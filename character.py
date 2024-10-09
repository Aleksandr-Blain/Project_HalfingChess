from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional, Union, List
from enum import Enum
from random import randint
from coord import Coord



class CharacterDeath(Exception):

    def __init__(self, msg, char: Character):
        self.message = msg


class InvalidAttack(Exception):
    pass


class Player(Enum):
    VILLAIN = 0
    HERO = 1

class Character(ABC):
    @abstractmethod
    def __init__(self, player: Player):
        self.__player = player
        self.__health = 5
        self.__temp_health = 5
        self.__attack = 3
        self.__defense = 3
        self.__move = 3
        self.__range = 1

    @property
    def player(self):
        return self.__player

    @player.setter
    def player(self, new_player):
        self.__player = Player[new_player]

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, new_health: int):
        self.__health = new_health

    @property
    def temp_health(self):
        return self.__temp_health

    @temp_health.setter
    def temp_health(self, new_temp_health: int):
        self.__temp_health = new_temp_health

    @property
    def combat(self):
        return list([self.__attack, self.__defense])

    @combat.setter
    def combat(self, combat_specs: list):
        if combat_specs[0] >= 0:
            self.__attack = combat_specs[0]
        else:
            raise ValueError

        if combat_specs[1] >= 0:
            self.__defense = combat_specs[1]
        else:
            raise ValueError

    @property
    def move(self):
        return self.__move

    @move.setter
    def move(self, new_move: int):
        if new_move > 0:
            self.__move = new_move
        else:
            raise ValueError

    @property
    def range(self):
        return self.__range

    @range.setter
    def range(self, new_range: int):
        if new_range > 0:
            self.__range = new_range
        else:
            raise ValueError

    @abstractmethod
    # TODO Is this correct?
    def is_valid_move(self, from_coord: Coord, to_coord: Coord, board: List[List[Union[None, Character]]]) -> bool:
        if to_coord.x == from_coord.x and to_coord.y == from_coord.y:
            return False

        elif board[from_coord.x][from_coord.y] != self:
            return False

        elif board[to_coord.x][to_coord.y] is not None:
            return False

        elif not 0 <= from_coord.x < len(board) and 0 <= from_coord.y < len(board[0]):
            return False

        elif not 0 <= to_coord.x < len(board) and 0 <= to_coord.y < len(board[0]):
            return False

        elif board[to_coord.x][to_coord.y] is not None:
            return False

        else:
            return True

    @abstractmethod
    def is_valid_attack(self, from_coord: Coord, to_coord: Coord, board: List[List[Union[None, Character]]]) -> bool:
        if not 0 <= from_coord.x < len(board) and 0 <= from_coord.y < len(board[0]):
            return False
        elif not 0 <= to_coord.x < len(board) and 0 <= to_coord.y < len(board[0]):
            return False
        elif to_coord.x == from_coord.x and to_coord.y == from_coord.y:
            return False
        else:
            return True

    @abstractmethod
    def calculate_dice(self, attack=True, lst: list = [], *args, **kwargs) -> int:
        succesful_rolls = 0
        if attack:
            number_dice = self.__attack
        else:
            number_dice = self.__defense

        if lst:
            number_rolls = lst[:number_dice]
        else:
            for i in range(number_dice):
                number_rolls = randint(1, 6)

        for i in number_rolls:
            if i >= 4:
                succesful_rolls += i
        return succesful_rolls

    @abstractmethod
    def deal_damage(self, target: Character, damage: int, *args, **kwargs) -> None:
        target.__temp_health -= damage
        print(f'{target} was dealt {damage} damage!')

        if CharacterDeath:
            print(f'{target} was defeated!')

    def __str__(self) -> str:
        return self.__class__.__name__












