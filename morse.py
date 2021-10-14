"""A package for Morse encoding and decoding."""

from collections import UserDict


class MorseDict(UserDict):
    def __init__(self, dictionary=None):
        self.data = {}
        if isinstance(dictionary, dict):
            self.data = dictionary

    def __getitem__(self, item):
        return_val = "?"
        try:
            return_val = self.data[item.upper().strip()]
        except KeyError as e:
            if len(item) == 1:
                return_val = "........"
            elif "." in item:
                return_val = "?"
        return return_val


class MetaMorse(type):
    _morse_tuples: list = [('A', '.='),
                           ('B', '=...'),
                           ('C', '=.=.'),
                           ('D', '=..'),
                           ('E', '.'),
                           ('F', '..=.'),
                           ('G', '==.'),
                           ('H', '....'),
                           ('I', '..'),
                           ('J', '.==='),
                           ('K', '=.='),
                           ('L', '.=..'),
                           ('M', '=='),
                           ('N', '=.'),
                           ('O', '==='),
                           ('P', '.==.'),
                           ('Q', '==.='),
                           ('R', '.=.'),
                           ('S', '...'),
                           ('T', '='),
                           ('U', '..='),
                           ('V', '...='),
                           ('W', '.=='),
                           ('X', '=..='),
                           ('Y', '=.=='),
                           ('Z', '==..'),
                           ('1', '.===='),
                           ('2', '..==='),
                           ('3', '...=='),
                           ('4', '....='),
                           ('5', '.....'),
                           ('6', '=....'),
                           ('7', '==...'),
                           ('8', '===..'),
                           ('9', '====.'),
                           ('0', '====='),
                           (' ', '=.=.=.='),
                           (',', '==..=='),
                           (':', '===...'),
                           (';', '=.=.=.'),
                           ('.', '.=.=.='),
                           ('"', '.=..=.'),
                           ('(', '=====.'),
                           (')', '.====='),
                           ('\'', '=.==.='),
                           ('@', '.==.=.'),
                           ('$', '...=..='),
                           ('_', '..==.='),
                           ('-', '=....='),
                           ('+', '.=.=.'),
                           ('?', '..==..'),
                           ('!', '=.=.=='),
                           ('/', '=..=.'),
                           ('&', '.=...'),
                           ('#', '........'),
                           ]

    _ascii_to_morse: MorseDict = MorseDict({i[0]: i[1] for i in _morse_tuples})
    _morse_to_ascii: MorseDict = MorseDict({i[1]: i[0] for i in _morse_tuples})

    @property
    def morse_tuples(cls) -> list:
        return cls._morse_tuples

    @property
    def ascii_to_morse(cls) -> MorseDict:
        return cls._ascii_to_morse

    @property
    def morse_to_ascii(cls) -> MorseDict:
        return cls._morse_to_ascii

    def __repr__(self):
        return f"{type(self).__name__}({self.data})"


class Morse(object, metaclass=MetaMorse):

    @property
    def morse_tuples(self) -> list:
        return type(self).morse_tuples

    @property
    def ascii_to_morse(self) -> MorseDict:
        return type(self).ascii_to_morse

    @property
    def morse_to_ascii(self) -> MorseDict:
        return type(self).morse_to_ascii

    @classmethod
    def encode_to_morse(cls, value: str) -> list[str]:
        return [cls.ascii_to_morse[l] for l in value]

    @classmethod
    def decode_from_morse(cls, value: str) -> list[str]:
        return [cls.morse_to_ascii[l] for l in value]

    @staticmethod
    def morse_spaced(value: list[str]) -> str:
        for character in value:
            yield character.ljust(10, ' ')

    @staticmethod
    def morse_chunks(value: str) -> str:
        for i in range(0, len(value), 10):
            yield value[i:i + 10]


m: Morse = Morse()

print(m.morse_to_ascii)
print(m.ascii_to_morse)

my_string = "Hello b@#ra^ve new w)rld."
text_string = m.encode_to_morse(my_string)
morse_string = m.decode_from_morse(''.join(text_string))

print(my_string)
print(text_string)
print(morse_string)

morse_spaced = m.morse_spaced(m.encode_to_morse(my_string))
morse_spaced = ''.join(morse_spaced)
print(morse_spaced)

for k, v in enumerate(m.morse_chunks(morse_spaced)):
    print(k, v, m.morse_to_ascii[v])
