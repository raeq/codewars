"""A package for Morse encoding and decoding."""
import string
from collections import UserDict


class MorseDict(UserDict):
    def __init__(self, dictionary=None):
        if isinstance(dictionary, dict):
            self.data = dictionary
        else:
            raise ValueError("MorseDict must be instantiated with a dict object.")

    def __setitem__(self, key, value):
        raise NotImplementedError("This MorseDict is frozen.")

    def __delitem__(self, key):
        raise NotImplementedError("This MorseDict is frozen.")

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
    """MetaClass to implement class properties for the Morse class."""
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
                           (' ', '       '),
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
        """Returns the list of morse tuples."""
        return cls._morse_tuples

    @property
    def ascii_to_morse(cls) -> MorseDict:
        """Returns the ascii to morse mapping dictionary."""
        return cls._ascii_to_morse

    @property
    def morse_to_ascii(cls) -> MorseDict:
        """Returns the morse to ascii mapping dictionary."""
        return cls._morse_to_ascii

    def __repr__(self):
        return f"{type(self).__name__}({self.data})"


class Morse(object, metaclass=MetaMorse):
    """The Morse class contains methods to encode and decode Morse code to ASCII."""

    @property
    def morse_tuples(self) -> list:
        """Returns the list of morse tuples."""
        return type(self).morse_tuples

    @property
    def ascii_to_morse(self) -> MorseDict:
        """Returns the ascii to morse mapping frozen dictionary."""
        return type(self).ascii_to_morse

    @property
    def morse_to_ascii(self) -> MorseDict:
        """Returns the morse to ascii mapping frozen dictionary."""
        return type(self).morse_to_ascii

    @classmethod
    def encode_to_morse(cls, value: str) -> list[str]:
        """Class method to encode each character in a string to a morse entry in a list."""
        return [cls.ascii_to_morse[l] for l in value]

    @classmethod
    def decode_from_morse(cls, value: list[str]) -> list[str]:
        """Class method to decode each morse code in a list to an ASCII entry in a list."""
        return [cls.morse_to_ascii[l] for l in value]

    @staticmethod
    def morse_spaced(value: list[str]) -> str:
        """Static method to generate a correctly spaced morse string for timing purposes.
        Use with Morse().encode_to_morse()"""
        for character in value:
            spacing = 3
            if character in string.whitespace:
                spacing = 7
            yield character + ' ' * spacing

    @staticmethod
    def morse_chunks(value: str) -> str:
        """Static method to return individual morse characters from a morse string.
        3 spaces means a new letter. 7 spaces means a new word.
        Use with Morse().decode_from_morse()"""

        for word in value.split(' ' * 7):
            for character in word.split(' ' * 3):
                yield character
            yield ''


m: Morse = Morse()

print(m.morse_to_ascii)
print(m.ascii_to_morse)

my_string = "Hello b@#ra^ve new w)rld."
text_string = m.encode_to_morse(my_string)
morse_string = m.decode_from_morse(text_string)

print(my_string)
print(text_string)
print(morse_string)

morse_spaced = m.morse_spaced(m.encode_to_morse(my_string))
morse_spaced = ''.join(morse_spaced)
print(morse_spaced)

for k, v in enumerate(m.morse_chunks(morse_spaced)):
    print(k, v, m.morse_to_ascii[v])
