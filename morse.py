"""A package for Morse encoding and decoding."""
from collections import UserDict
from typing import NamedTuple


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
                return_val = ""
            elif "." in item:
                return_val = "#"
        return return_val


class MorseCouple(NamedTuple):
    """A couple (tuple with a length of two) representing ascii<->morse mappings."""
    ascii: str
    morse: str


class MetaMorse(type):
    """MetaClass to implement class properties for the Morse class."""
    _morse_tuples: list = [MorseCouple(ascii='A', morse='.-'),
                           MorseCouple(ascii='B', morse='-...'),
                           MorseCouple(ascii='C', morse='-.-.'),
                           MorseCouple(ascii='D', morse='-..'),
                           MorseCouple(ascii='E', morse='.'),
                           MorseCouple(ascii='F', morse='..-.'),
                           MorseCouple(ascii='G', morse='--.'),
                           MorseCouple(ascii='H', morse='....'),
                           MorseCouple(ascii='I', morse='..'),
                           MorseCouple(ascii='J', morse='.---'),
                           MorseCouple(ascii='K', morse='-.-'),
                           MorseCouple(ascii='L', morse='.-..'),
                           MorseCouple(ascii='M', morse='--'),
                           MorseCouple(ascii='N', morse='-.'),
                           MorseCouple(ascii='O', morse='---'),
                           MorseCouple(ascii='P', morse='.--.'),
                           MorseCouple(ascii='Q', morse='--.-'),
                           MorseCouple(ascii='R', morse='.-.'),
                           MorseCouple(ascii='S', morse='...'),
                           MorseCouple(ascii='T', morse='-'),
                           MorseCouple(ascii='U', morse='..-'),
                           MorseCouple(ascii='V', morse='...-'),
                           MorseCouple(ascii='W', morse='.--'),
                           MorseCouple(ascii='X', morse='-..-'),
                           MorseCouple(ascii='Y', morse='-.--'),
                           MorseCouple(ascii='Z', morse='--..'),
                           MorseCouple(ascii='1', morse='.----'),
                           MorseCouple(ascii='2', morse='..---'),
                           MorseCouple(ascii='3', morse='...--'),
                           MorseCouple(ascii='4', morse='....-'),
                           MorseCouple(ascii='5', morse='.....'),
                           MorseCouple(ascii='6', morse='-....'),
                           MorseCouple(ascii='7', morse='--...'),
                           MorseCouple(ascii='8', morse='---..'),
                           MorseCouple(ascii='9', morse='----.'),
                           MorseCouple(ascii='0', morse='-----'),
                           MorseCouple(ascii=',', morse='--..--'),
                           MorseCouple(ascii=':', morse='---...'),
                           MorseCouple(ascii=';', morse='-.-.-.'),
                           MorseCouple(ascii='.', morse='.-.-.-'),
                           MorseCouple(ascii='"', morse='.-..-.'),
                           MorseCouple(ascii='MorseCouple(ascii=', morse='-----.'),
                           MorseCouple(ascii=')', morse='.-----'),
                           MorseCouple(ascii='\'', morse='-.--.-'),
                           MorseCouple(ascii='@', morse='.--.-.'),
                           MorseCouple(ascii='$', morse='...-..-'),
                           MorseCouple(ascii='_', morse='..--.-'),
                           MorseCouple(ascii='-', morse='-....-'),
                           MorseCouple(ascii='+', morse='.-.-.'),
                           MorseCouple(ascii='?', morse='..--..'),
                           MorseCouple(ascii='!', morse='-.-.--'),
                           MorseCouple(ascii='/', morse='-..-.'),
                           MorseCouple(ascii='&', morse='.-...'),
                           MorseCouple(ascii='#', morse='........'),
                           ]
    i: MorseCouple
    _ascii_to_morse: MorseDict = MorseDict({i.ascii: i.morse for i in _morse_tuples})
    _morse_to_ascii: MorseDict = MorseDict({i.morse: i.ascii for i in _morse_tuples})

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
    def encode_to_morse(cls, value: list[str]) -> list[str]:
        """Class method to encode each character in a string to a morse entry in a list."""
        if isinstance(value, str):
            value = value.split(' ')

        for word in value:
            yield [cls.ascii_to_morse[l] for l in word]

    @classmethod
    def decode_from_morse(cls, value: list[str]) -> list[str]:
        """Class method to decode each morse code in a list to an ASCII entry in a list."""
        if isinstance(value, str):
            value = value.split(' ' * 7)
        for word in value:
            yield [cls.morse_to_ascii[l] for l in word]

    @staticmethod
    def morse_to_signal(value: list[str]) -> str:
        """Static method to generate a correctly spaced morse string for timing purposes.
        Use with Morse().encode_to_morse()"""
        for i, word in enumerate(value):
            return_val = ""
            for morse_character in word:
                for dot_or_dash in morse_character:
                    if dot_or_dash == ".":
                        return_val += '10'
                    elif dot_or_dash == "-":
                        return_val += '1110'
                return_val += '00'
            yield return_val + '0000'

    @staticmethod
    def words_to_signal(value: list[str]) -> str:
        """Static method to generate a correctly spaced morse string for timing purposes."""
        morse_words = list(Morse.encode_to_morse(value))
        yield ''.join(Morse.morse_to_signal(morse_words))

    @staticmethod
    def signal_to_morse(value: str) -> list[str]:
        """Static method to return individual morse characters from a morse string.
        3 spaces means a new letter. 7 spaces means a new word.
        Use with Morse().decode_from_morse()"""

        for word in value.split('0' * 7):
            morse_word = []
            for morse_character in word.split('0' * 3):
                chars = ""
                for seq in morse_character.split('0'):
                    if seq == '111':
                        chars += "-"
                    elif seq == "1":
                        chars += "."
                morse_word.append(chars)
            if len(morse_word) >= 1 and len(morse_word[0]) > 0:
                # only yield a word if the word isn't [''] - equivalent to a final '0000000' in the signal
                yield morse_word


m: Morse = Morse()

my_string = "Morse Code"
text_string = list(m.encode_to_morse(my_string))
morse_string = list(m.decode_from_morse(text_string))

print(my_string)
print(text_string)
print(morse_string)

morse_signal = ''.join(m.morse_to_signal(list(m.encode_to_morse(my_string))))
words_signal = m.words_to_signal(my_string)
print(''.join(words_signal))

print(morse_signal)
print(list(m.signal_to_morse(morse_signal)))
