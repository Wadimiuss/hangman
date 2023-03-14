from random import shuffle

class Card():
    masti = ['Черви', 'Бубни', 'Крести', 'Пики']
    values = ['6', '7', '8', '9', '10', 'Валет', 'Дама', 'Король', 'Туз']

    def __init__(self, value, mast):
        self.mast = mast
        self.value = value

    def __lt__(self, other):
        if self.value < other.value:
            return True
        if self.value == other.value:
            return 'Ничья'
        return False

    def __gt__(self, other):
        if self.value > other.value:
            return True
        if self.value == other.value:
            return 'Ничья'
        return False

    def __repr__(self):
        return self.values[self.value] + " " + self.masti[self.mast]

class Deck():

    def __init__(self):
        self.cards = []
        for i in range(9):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def del_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

class Player():

    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.hand = None


class Game():

    def __init__(self):
        name1 = input('Введите название игрока 1: ')
        name2 = input('Введите название игрока 2: ')
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def play_game(self):
        cards = self.deck.cards
        print('Начинаем игру')
        while len(cards) >= 2:
            m = 'Нажимте Х для выхода или любую кнопку для начала игры: '
            print('==================================')
            print(self.p1.wins, self.p2.wins)
            print('==================================')
            response = input(m)
            if response == 'X':
                print('Игра окончена')
                break
            p1_hand = self.deck.del_card()
            p2_hand = self.deck.del_card()
            print(f'Игрок {self.p1.name} кладет в руку {p1_hand}, игрок2 {self.p2.name} кладет в руку {p2_hand}')
            if p1_hand > p2_hand:
                self.p1.wins += 1
                print(f'Игрок {self.p1.name} побеждает раунд')
            elif p1_hand < p2_hand:
                self.p2.wins += 1
                print(f'Игрок {self.p2.name} побеждает раунд')
            elif p1_hand == p2_hand:
                print('Ничья')
        print('==================================')
        print(self.p1.wins, self.p2.wins)
        print('==================================')
        print(f'Игра окончена побеждает {self.winner(self.p1, self.p2)}')


    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return 'Ничья'

game = Game()
game.play_game()