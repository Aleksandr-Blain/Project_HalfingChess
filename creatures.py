from random import Random

from character import *
from abc import ABC, abstractmethod

class Villain(Character):
    def __init__(self):
        super().__init__(Player.VILLAIN)

    def is_valid_move(self, from_coord: Coord, to_coord: Coord, board: List[List[Union[None, Character]]]) -> bool:
        if not (0 <= from_coord.x < len(board)) or not (0 <= from_coord.y < len(board[0])):
            return False  # checking if starting coords are in bounds

        if not (0 <= to_coord.x < len(board)) or not (0 <= to_coord.y < len(board[0])):
            return False  # checking if ending location is in bounds

        if board[from_coord.x][from_coord.y] != self:
            return False  # Checks if self is at starting location

        if board[to_coord.x][to_coord.y] is not None:
            return False  # Checks if end location is empty

        return True

    def is_valid_attack(self, from_coord: Coord, to_coord: Coord, board: List[List[Union[None, Character]]]) -> bool:
        return super().is_valid_attack(from_coord, to_coord, board)

    def calculate_dice(self, attack=True, lst: list = []) -> int:
        return super().calculate_dice(attack, lst)

    def deal_damage(self, target: Character, damage: int, *args, **kwargs) -> None:
        return super().deal_damage(target, damage, *args, **kwargs)


class Goblin(Villain):
    def __init__(self):
        super().__init__()
        self.health = 3
        self.temp_health = 3
        self.combat = [2, 2]


class Skeleton(Villain):
# TODO am i setting and utilizing super correctly
    def __init__(self):
        super().__init__()
        self.health = 2
        self.temp_health = 2
        self.combat = [2, 1]
        self.move = 2


class Necromancer(Villain):
    def __init__(self):
        super().__init__()
        self.combat = [1, 2]
        self.range = 3

    def raise_dead(self, target: Character):
        if not Player.VILLAIN:
            target = Player.VILLAIN

        target.__health = target.__health // 2

class Hero(Character):
    def __init__(self):
        super().__init__(Player.HERO)

    def is_valid_move(self, from_coord: Coord, to_coord: Coord, board: List[List[Union[None, Character]]]) -> bool:
        return super().is_valid_move(from_coord, to_coord, board)

    def is_valid_attack(self, from_coord: Coord, to_coord: Coord, board: List[List[Union[None, Character]]]) -> bool:
        return super().is_valid_attack(from_coord, to_coord, board)

    def calculate_dice(self, target: Character, attack=True, lst=[]) -> int:
        return super().calculate_dice(attack, lst)

    def deal_damage(self, target: Character, damage: int, *args, **kwargs) -> None:
        return super().deal_damage(target, damage, *args, **kwargs)


class Warrior(Hero):
    def __init__(self):
        super().__init__()
        self.health = 7
        self.temp_health = 7
        self.combat = [2, 4]

    def calculate_dice(self, target: Character, attack=True, lst: list = [], gob: list = []):
        # TODO how to edit calculate dice
        if lst:
            dice_rolls = lst
        else:
            dice_rolls = []
            for _ in range(2):
                dice_rolls.append(random.randint(1, 6))

        if isinstance(target, Goblin):
            dice_rolls[0] += 2

        if not gob:
            gob.extend([random.randint(1, 6) for _ in range(2)])

        return dice_rolls + gob


class Mage(Hero):
    def __init__(self):
        super().__init__()
        self.combat = [2, 2]
        self.range = 3
        self.move = 2

    def deal_damage(self, target: Character, damage: int, *args, **kwargs) -> None:
        damage += 1
        super().deal_damage(target, damage, *args, **kwargs)



class Paladin(Hero):
    def __init__(self):
        super().__init__()
        self.heal = bool
        self.health = 6
        self.temp_health = 6

    @property
    def heal(self):
        return self.heal

    @heal.setter
    def heal(self, v):
        if v:
            self.heal = True


    # TODO- How to check if something is in range or not
    def revive(self, target: Character):
        pass



class Ranger(Hero):
    class Ranger(Hero):
        def __init__(self):
            super().__init__()
            self.health = 7
            self.temp_health = 7
            self.attack = 2
            self.range = 3

        def deal_damage(self, target: Character, damage: int, *args, **kwargs) -> None:
            if target is Skeleton:
                damage -= 1
            if damage < 0:
                damage = 0
            target.temp_health -= damage

        def calculate_dice(self, attack=True, lst: list = [], gob: list = [], *args, **kwargs):
            pass











