"""
Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an
array with words. You should return an array of all the anagrams or an empty array if there are none. For example:

anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']
anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']
anagrams('laser', ['lazing', 'lazy',  'lacer']) => []

"""
from collections import deque


def anagrams(word, words):
    l: int = len(word)
    words: list = [x for x in words if len(x) == l]
    ret_list: list = []

    for w in words:
        original = deque(word)

        for letter in w:
            try:
                original.remove(letter)
            except ValueError:
                break

        if len(original) == 0:
            ret_list.append(w)

    return ret_list


assert (anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) == ['aabb', 'bbaa'])
assert (anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) == ['carer', 'racer'])
