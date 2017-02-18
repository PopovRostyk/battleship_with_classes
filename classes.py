import string

class Ship:
    def __init__(self, bow, horizontal, length, hit):
        self.bow = bow
        self.horizontal = horizontal
        self.length = length
        self._hit = hit

    def shoot_at(self, position):
        pass


class Player:
    def __init__(self, name):
        self._name = name

    def read_position(self, pos):
        pass


class Field:
    def __init__(self, ships=[]):
        self._ships = ships

    def shoot_at(self, tuple):
        pass
    @staticmethod

    def field_without_ships():
        lst = [string.ascii_lowercase[i] for i in range(10)]
        return lst

    def field_with_ships(self):
        lst = [[' ' for i in range(10)] for i in range(10)]
        for items in lst:
            print(items)


class Game:
    def __init__(self, current_player, fields=[], players=[]):
        self._current_player = current_player
        self._fields = fields
        self._players = players

print(Field().field_with_ships())