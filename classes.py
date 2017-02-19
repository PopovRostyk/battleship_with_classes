import string


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
        b = [['X' for i in range(10)] for i in range(10)]
        return b
field = Field().field_with_ships()


class Ship:
    def __init__(self, bow=0, horizontal=0, length=0, hit=0):
        self.bow = bow
        self.horizontal = horizontal
        self.length = length
        self._hit = hit

    def shoot_at(self, position):
        num_letter = next(item for item in position if isinstance(item, str) and item.isalpha()).lower()
        num_letter = string.ascii_lowercase[:10].find(num_letter)
        num_num = next(item for item in position if isinstance(item, int))
        field[num_num - 1][num_letter] = 'o'
        return field


class Game:
    def __init__(self, current_player=[], fields=[], players=[]):
        self._current_player = current_player
        self._fields = fields
        self.players = players

    def start_game(self):
        player = Player()
        try:
            player.name = input('Write your name: ')
            Game().players.append(player)
        
Game().start_game()
print(Game().players)