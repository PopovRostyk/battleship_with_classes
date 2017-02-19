import string


class Player:
    def __init__(self, name):
        self.name = name

    def read_position(self):
        pos = input('Where you want to shot: ')
        for items in pos:
            if items.isdigit():
                num = int(items)
            elif items.isalpha():
                letter = items
        return (num, letter)





class Field:
    def __init__(self, ships=[]):
        self._ships = ships

    def shoot_at(self, tuple):
        num_letter = next(item for item in tuple if isinstance(item, str) and item.isalpha()).lower()
        num_letter = string.ascii_lowercase[:10].find(num_letter)
        num_num = next(item for item in tuple if isinstance(item, int))
        field[num_num - 1][num_letter] = 'o'
        return field

    def field_without_ships(self):
        a = []
        i = 1
        a.append(string.ascii_uppercase[:10])
        print('   ', end='')
        for items in a:
            for item in items:
                print(item, end=' ')
        print(a)
        print('\n')
        print('  ', '___________________')
        b = [['X' for i in range(10)] for i in range(10)]
        print(b)
        for i in range(len(b)):
            if i == 9:
                print(i + 1, end=' ')
            else:
                print(i + 1, end='  ')
            for items in b[i]:
                for item in items:
                    print(item, end=' ')
            print('\n')
        return b

    def field_with_ships(self):
        b = [['X' for _ in range(10)] for _ in range(10)]
        return b
field = Field().field_with_ships()


class Ship:
    def __init__(self, bow=0, horizontal=0, length=0, hit=0):
        self.bow = bow
        self.horizontal = horizontal
        self.length = length
        self._hit = hit

    def shoot_at(self, position):
        pass


class Game:
    def __init__(self, current_player=[], fields=[], players=[]):
        self._current_player = current_player
        self._fields = fields
        self.players = players

    def adding_players(self):
        for i in range(2):
            player = Player(input('write name '))
            Game().players.append(player)

print(Field().shoot_at(Player('john').read_position()))
