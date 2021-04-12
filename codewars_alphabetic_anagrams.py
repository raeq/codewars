"""
https://www.codewars.com/kata/53e57dada0cb0400ba000688/train/python
"""
from itertools import permutations


"""
Sample words, with their rank:
ABAB = 2
AAAB = 1
BAAA = 4
QUESTION = 24572
BOOKKEEPER = 10743
"""


def listPosition(word):
    """Return the anagram list position of the word"""
    perms = set()
    for t in permutations(sorted(word), len(word)):
        perms.add(t)
        if "".join(t) == word:
            return len(perms)



testValues = {'ABAB': 2, 'A': 1, 'AAAB': 1, 'BAAA': 4, 'QUESTION': 24572, 'BOOKKEEPER': 10743}
for word in testValues:
    assert listPosition(word) == testValues[word], f"{word} != {testValues[word]}"
