import random
from typing import NamedTuple


class Card(NamedTuple):
    suit: str
    face: str
    face_value: int

    @property
    def description(self):
        return f"{self.face} of {self.suit} ({self.face_value})"


class Pack:
    suits: list
    cards: list
    faces: list

    def __init__(self):
        for suit in self.suits:
            for face in self.faces:
                self.cards.append(Card(suit=suit, face=face[0], face_value=face[1]))

    def __repr__(self):
        return f'{self.__class__.__name__}(suits={repr(self.suits)},faces={repr(self.faces)})'


class GermanPack(Pack):
    def __init__(self):
        self.cards: list = []
        self.faces: list = [('7', 7), ('8', 8),
                            ('9', 9), ('10', 10), ('Unterknabe', 10), ('Oberknabe', 10),
                            ('Koenig', 10), ('Ass', 11)]
        self.suits: list = ['Acorns', 'Leaves', 'Hearts', 'Bells']

        super().__init__()


class FrenchPack(Pack):
    def __init__(self):
        self.cards: list = []
        self.faces: list = [('A', 11), ('2', 2), ('3', 3), ('4', 4),
                            ('5', 5), ('6', 6), ('7', 7), ('8', 8),
                            ('9', 9), ('10', 10), ('J', 10), ('Q', 10), ('K', 10)]
        self.suits: list = ['Diamonds', 'Hearts', 'Spades', 'Clubs']

        super().__init__()


class ItalianPack(Pack):
    def __init__(self):
        self.cards: list = []
        self.faces: list = [('A', 1), ('2', 2), ('3', 3), ('4', 4),
                            ('5', 5), ('6', 6), ('7', 7), ('8', 8),
                            ('9', 9), ('10', 10), ('Fante', 10), ('Cavallo', 10),
                            ('Re', 10)]
        self.suits: list = ['Spade', 'Coppe', 'Denari', 'Bastoni']

        super().__init__()


class Talon:
    cards: list
    shuffled: bool = False

    def __init__(self, packs: int = 1, pack_choice=FrenchPack):
        self.cards = []
        self._dealt = 0

        if not packs > 0:
            packs = 1

        self._packs = packs

        if type(pack_choice) not in {type(FrenchPack), type(ItalianPack), type(GermanPack)}:
            raise ValueError(f"Expected one of "
                             f"{FrenchPack, ItalianPack, GermanPack}, not {pack_choice!r}")

        self._pack_choice = pack_choice

        for _ in range(self._packs):
            self.cards.extend(self._pack_choice().cards[::])
        self.shuffle()

    def shuffle(self):
        for _ in range(7):
            random.shuffle(self.cards)
        self.shuffled = True

    def draw(self):
        c = self.cards.pop()
        self._dealt += 1
        return c

    @property
    def available(self):
        return len(self.cards)

    @property
    def dealt(self):
        return self._dealt

    def __repr__(self):
        return f'{self.__class__.__name__}(packs={self._packs}, ' \
               f'pack_choice={self._pack_choice!r}, available={self.available}, ' \
               f'dealt={self.dealt})'


t = Talon(-1, pack_choice=FrenchPack)
print(t)
while t.cards:
    print(t.draw(), end='\r')
print(t)
