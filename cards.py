import random
from typing import NamedTuple


class Card(NamedTuple):
    """
    Represents a playing card.
    The suit is usually hearts, diamonds etc.
    The face is usually J, 10, A K, 3, 4 etc
    The face value is usually the number of pips or standard expectations of a card's value
    which can change according to the rules of a card game.

    >>> c:Card = Card(suit="Spades", face="A", face_value=11)
    >>> print(c)
    Card(suit='Spades', face='A', face_value=11)
    >>> print(c.description)
    A of Spades (11)
    """
    suit: str
    face: str
    face_value: int

    @property
    def description(self):
        return f"{self.face} of {self.suit} ({self.face_value})"


class Pack:
    """
    A pack, or "deck", of cards. A standard pack has 52 cards, and is also
    known as a FrenchDeck.

    This class is abstract.
    """
    suits: list
    cards: list
    faces: list

    def __init__(self):
        self.build_pack()

    def build_pack(self):
        self.cards = []
        for suit in self.suits:
            for face in self.faces:
                self.cards.append(Card(suit=suit, face=face[0], face_value=face[1]))

    def __repr__(self):
        return f'{self.__class__.__name__}(suits={repr(self.suits)},faces={repr(self.faces)})'

    def remove_card(self, card: Card):
        self.cards.remove(card)

    def remove_random_facecard(self, face: str):
        all_faces: list = [c for c in self.cards if c.face == face]
        self.cards.remove(random.choice(all_faces))

    def add_jokers(self, quantity: int = 1):
        self.cards.append(Card(suit="Joker", face="JOKER", face_value=0))

    def remove_all_faces(self, faces: list):
        removed_faces: list = []
        faces = set(faces)

        for f in self.faces:
            if f[0] in faces:
                removed_faces.append(f)

        for f in removed_faces:
            self.faces.remove(f)
        self.build_pack()


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

    def __init__(self, packs: int = 1, pack_choice=FrenchPack()):
        self.cards = []
        self._dealt = 0

        if not packs > 0:
            packs = 1

        self._packs = packs

        self._pack_choice = pack_choice

        for _ in range(self._packs):
            self.cards.extend(self._pack_choice.cards[::])

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


# Build Agram Pack https://bicyclecards.com/how-to-play/agram/
# The kings, queens, jacks, the 2s of all suits and the ace of spades are removed from the deck. The cards of each suit
# rank, from high to low: A, 10, 9, 8, 7, 6, 5, 4, 3. Because the ace of spades (called "Chief"') is removed from the
# deck, the highest card in the spade suit is the 10.

agram = FrenchPack()
agram.remove_all_faces(["K", "Q", "J", "2"])
agram.remove_card(Card(suit='Spades', face='A', face_value=11))

t = Talon(-1, pack_choice=agram)
t.shuffle()

print(t)
for c in t.cards:
    print(c)

# Build Old Maid Pack https://bicyclecards.com/how-to-play/old-maid/
# The standard 52-card pack is used, however, one of the four queens is removed, leaving a total of 51 cards.

oldmaid = FrenchPack()
oldmaid.remove_random_facecard("Q")

t = Talon(-1, pack_choice=oldmaid)

print(len(t.cards))
for c in t.cards:
    print(c)

# Build the Continental Rummy Deck
# Use two 52-card decks and add in 1 Joker per pack, for a total of 106 cards

cont_rummy = FrenchPack()
cont_rummy.add_jokers(1)

t = Talon(packs=2, pack_choice=cont_rummy)

print(len(t.cards))
for c in t.cards:
    print(c)
