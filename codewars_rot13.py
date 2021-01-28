"""
Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special
characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet
should be shifted, like in the original Rot13 "implementation".
"""
import string

def rot13(message, rotation=13):

    outstr = ""
    for s in message:
        ordi = ord(s)
        modifier = 0

        if ordi >= 97 and ordi <= 122:
            modifier = 97

        elif ordi >= 65 and ordi <= 90:
            modifier = 65

        if modifier > 0:
            new_ordinal = ((ordi - modifier) + rotation) % 26
            outstr += chr(new_ordinal + modifier)

        else:
            outstr += s

    return outstr

assert(rot13("test") == "grfg")
assert(rot13("Test") == "Grfg")