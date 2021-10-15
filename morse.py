"""A package for Morse encoding and decoding."""
from collections import UserDict
from time import sleep
from typing import NamedTuple

from pysinewave import SineWave


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


class MorseTriple(NamedTuple):
    """A couple (tuple with a length of two) representing ascii<->morse mappings."""
    ascii: str
    morse: str
    signal: str


class MetaMorse(type):
    """MetaClass to implement class properties for the Morse class."""
    _morse_tuples: list = [
        MorseTriple(ascii='A', morse='.-', signal='10111000'),
        MorseTriple(ascii='B', morse='-...', signal='111010101000'),
        MorseTriple(ascii='C', morse='-.-.', signal='11101011101000'),
        MorseTriple(ascii='D', morse='-..', signal='1110101000'),
        MorseTriple(ascii='E', morse='.', signal='1000'),
        MorseTriple(ascii='F', morse='..-.', signal='101011101000'),
        MorseTriple(ascii='G', morse='--.', signal='111011101000'),
        MorseTriple(ascii='H', morse='....', signal='1010101000'),
        MorseTriple(ascii='I', morse='..', signal='101000'),
        MorseTriple(ascii='J', morse='.---', signal='1011101110111000'),
        MorseTriple(ascii='K', morse='-.-', signal='111010111000'),
        MorseTriple(ascii='L', morse='.-..', signal='101110101000'),
        MorseTriple(ascii='M', morse='--', signal='1110111000'),
        MorseTriple(ascii='N', morse='-.', signal='11101000'),
        MorseTriple(ascii='O', morse='---', signal='11101110111000'),
        MorseTriple(ascii='P', morse='.--.', signal='10111011101000'),
        MorseTriple(ascii='Q', morse='--.-', signal='1110111010111000'),
        MorseTriple(ascii='R', morse='.-.', signal='1011101000'),
        MorseTriple(ascii='S', morse='...', signal='10101000'),
        MorseTriple(ascii='T', morse='-', signal='111000'),
        MorseTriple(ascii='U', morse='..-', signal='1010111000'),
        MorseTriple(ascii='V', morse='...-', signal='101010111000'),
        MorseTriple(ascii='W', morse='.--', signal='101110111000'),
        MorseTriple(ascii='X', morse='-..-', signal='11101010111000'),
        MorseTriple(ascii='Y', morse='-.--', signal='1110101110111000'),
        MorseTriple(ascii='Z', morse='--..', signal='11101110101000'),
        MorseTriple(ascii='1', morse='.----', signal='10111011101110111000'),
        MorseTriple(ascii='2', morse='..---', signal='101011101110111000'),
        MorseTriple(ascii='3', morse='...--', signal='1010101110111000'),
        MorseTriple(ascii='4', morse='....-', signal='10101010111000'),
        MorseTriple(ascii='5', morse='.....', signal='101010101000'),
        MorseTriple(ascii='6', morse='-....', signal='11101010101000'),
        MorseTriple(ascii='7', morse='--...', signal='1110111010101000'),
        MorseTriple(ascii='8', morse='---..', signal='111011101110101000'),
        MorseTriple(ascii='9', morse='----.', signal='11101110111011101000'),
        MorseTriple(ascii='0', morse='-----', signal='1110111011101110111000'),
        MorseTriple(ascii=',', morse='--..--', signal='1110111010101110111000'),
        MorseTriple(ascii=':', morse='---...', signal='11101110111010101000'),
        MorseTriple(ascii=';', morse='-.-.-.', signal='11101011101011101000'),
        MorseTriple(ascii='.', morse='.-.-.-', signal='10111010111010111000'),
        MorseTriple(ascii='"', morse='.-..-.', signal='101110101011101000'),
        MorseTriple(ascii=')', morse='.-----', signal='101110111011101110111000'),
        MorseTriple(ascii='\'', morse='-.--.-', signal='1110101110111010111000'),
        MorseTriple(ascii='@', morse='.--.-.', signal='10111011101011101000'),
        MorseTriple(ascii='$', morse='...-..-', signal='10101011101010111000'),
        MorseTriple(ascii='_', morse='..--.-', signal='10101110111010111000'),
        MorseTriple(ascii='-', morse='-....-', signal='111010101010111000'),
        MorseTriple(ascii='+', morse='.-.-.', signal='1011101011101000'),
        MorseTriple(ascii='?', morse='..--..', signal='101011101110101000'),
        MorseTriple(ascii='!', morse='-.-.--', signal='1110101110101110111000'),
        MorseTriple(ascii='/', morse='-..-.', signal='1110101011101000'),
        MorseTriple(ascii='&', morse='.-...', signal='10111010101000'),
        MorseTriple(ascii='#', morse='........', signal='101010101010101000'),
    ]
    i: MorseTriple
    _ascii_to_morse: MorseDict = MorseDict({i.ascii: i._asdict() for i in _morse_tuples})
    _morse_to_ascii: MorseDict = MorseDict({i.morse: i._asdict() for i in _morse_tuples})
    _signal_to_morse: MorseDict = MorseDict({i.signal: i._asdict() for i in _morse_tuples})

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

    @property
    def signal_to_morse(cls) -> MorseDict:
        """Returns the morse to ascii mapping dictionary."""
        return cls._signal_to_morse

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

    @property
    def signal_to_morse(self) -> MorseDict:
        """Returns the ascii to morse mapping frozen dictionary."""
        return type(self).signal_to_morse

    @classmethod
    def encode_to_morse(cls, value: list[str]) -> list[str]:
        """Class method to encode each character in a string to a morse entry in a list."""
        if isinstance(value, str):
            value = value.split(' ')

        for word in value:
            yield [cls.ascii_to_morse[l]["morse"] for l in word]

    @classmethod
    def encode_to_morse_short(cls, value: list[str]) -> list[str]:
        return list(Morse.encode_to_morse(value))

    @classmethod
    def decode_from_morse(cls, value: list[str]) -> list[str]:
        """Class method to decode each morse code in a list to an ASCII entry in a list."""
        if isinstance(value, str):
            value = value.split(' ' * 7)
        for word in value:
            yield [cls.morse_to_ascii[l]["ascii"] for l in word]

    @classmethod
    def decode_from_morse_short(cls, value: list[str]) -> list[str]:
        return list(Morse.decode_from_morse(value))

    @staticmethod
    def morse_to_signal(value: list[str]) -> str:
        """Static method to generate a correctly spaced morse string for timing purposes.
        Use with Morse().encode_to_morse()"""
        for word in value:
            return_val = ""
            for morse_code in word:
                return_val += Morse.morse_to_ascii[morse_code]["signal"]
            yield return_val + '0000'

    @staticmethod
    def words_to_signal(value: list[str]) -> str:
        """Static method to generate a correctly spaced morse string for timing purposes."""
        morse_words = list(Morse.encode_to_morse(value))
        return ''.join(Morse.morse_to_signal(morse_words))

    @staticmethod
    def signal_to_morse_triples(value: str) -> list[MorseTriple]:
        """Static method to return individual morse characters from a morse string.
        3 spaces means a new letter. 7 spaces means a new word.
        Use with Morse().decode_from_morse()"""

        for word in value.split('0' * 7):
            morse_word = []
            for morse_code in word.split('0' * 3):
                morse_code = morse_code + "000"
                morse_word.append(Morse.signal_to_morse[morse_code])
            if len(morse_word) >= 1 and len(morse_word[0]) > 0:
                # only yield a word if the word isn't [''] - equivalent to a final '0000000' in the signal
                yield morse_word

    @staticmethod
    def signal_to_audio(signal: str) -> None:

        sine_wave = SineWave(pitch=16)
        for word in signal.split("0000000"):
            for morse_code in word.split('000'):
                morse_triple: MorseTriple
                morse_dict = Morse.signal_to_morse[morse_code + "000"]
                if morse_code:
                    morse_triple = MorseTriple(signal=morse_dict["signal"], ascii=morse_dict["ascii"],
                                               morse=morse_dict["morse"])
                    print(morse_triple)
                    for signal in morse_triple.signal.split('0'):
                        if len(signal) == 3:
                            sine_wave.play()
                            sleep(0.35)
                            sine_wave.stop()
                        if len(signal) == 1:
                            sine_wave.play()
                            sleep(0.10)
                            sine_wave.stop()

                sleep(0.40)
            print("<SPACE>")
            sleep(1.20)

    @staticmethod
    def message_to_audio(message: str):
        signal = Morse.words_to_signal(message)
        Morse.signal_to_audio(signal)

m: Morse = Morse()

my_string = "Morse Code"
morse_string = list(m.encode_to_morse(my_string))
decoded_string = list(m.decode_from_morse(morse_string))

print(my_string)
print(morse_string)
print(decoded_string)

words_signal = m.words_to_signal(my_string)
print(words_signal)

Morse.message_to_audio(my_string)
