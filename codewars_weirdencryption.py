"""
For building the encrypted string:
Take every 2nd char from the string, then the other chars, that are not every 2nd char, and concat them as new String.
Do this n times!
https://www.codewars.com/kata/57814d79a56c88e3e0000786/train/python
"""
import itertools

def two_lists_decrypt(input: list) -> str:
    i2 = input[:len(input)//2]
    i1 = input[len(input) // 2:]
    return ''.join(''.join(x) for x in itertools.zip_longest(i1, i2, fillvalue=''))

def two_lists_encrypt(input: list) -> str:
    i1 = input[0::2]
    i2 = input[1::2]
    return i2 + i1


def decrypt(encrypted_text, n):
    ret_value = encrypted_text
    if n > 0 and ret_value:
        for i in range(n):
            ret_value = two_lists_decrypt(ret_value)

    return ret_value


def encrypt(text, n):
    ret_value = text
    if n > 0 and ret_value:
        for i in range(n):
            ret_value = two_lists_encrypt(ret_value)

    return ret_value



assert(encrypt("This is a test!", 0) == "This is a test!")
assert(encrypt("This is a test!", 1) == "hsi  etTi sats!")
assert(encrypt("This is a test!", 2) == "s eT ashi tist!")
assert(encrypt("This is a test!", 3) == " Tah itse sits!")
assert(encrypt("This is a test!", 4) == "This is a test!")
assert(encrypt("This is a test!", -1) == "This is a test!")
assert(encrypt("This kata is very interesting!", 1) == "hskt svr neetn!Ti aai eyitrsig")

assert(decrypt("This is a test!", 0) == "This is a test!")
assert(decrypt("hsi  etTi sats!", 1) == "This is a test!")
assert(decrypt("s eT ashi tist!", 2) == "This is a test!")
assert(decrypt(" Tah itse sits!", 3) == "This is a test!")
assert(decrypt("This is a test!", 4) == "This is a test!")
assert(decrypt("This is a test!", -1) == "This is a test!")
assert(decrypt("hskt svr neetn!Ti aai eyitrsig", 1) == "This kata is very interesting!")

assert(encrypt("", 0) == "")
assert(decrypt("", 0) == "")
assert(encrypt(None, 0) == None)
assert(decrypt(None, 0) == None)