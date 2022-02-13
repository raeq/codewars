from enum import Enum
from typing import NamedTuple

from more_itertools import chunked


class Result(Enum):
    NOTPRESENT = 1
    INCORRECT_LOCATION = 2
    CORRECT_LOCATION = 3


class Guess(NamedTuple):
    letter: str
    result: Result


def parse_input(user_input: str) -> list[Guess]:
    parsed_input = []

    for pair in chunked(user_input, 2):
        g = Guess(letter=pair[0].lower(),
                  result=Result(int(pair[1])))
        parsed_input.append(g)

    return parsed_input


def original(words: list[str]):
    while len(words) > 1 and (letters := parse_input(input("Letters please: "))):

        # only keep words which have this letter in this position
        for key, value in enumerate(letters):
            if value.result == Result.CORRECT_LOCATION:
                words = [word for word in words if word[key] == value.letter]

        # only keep words which have this letter somewhere
        for key, value in enumerate(letters):
            if value.result == Result.INCORRECT_LOCATION:
                words = [word for word in words if value.letter in word]

        # only keep words which do not have this letter in this position
        for key, value in enumerate(letters):
            if value.result == Result.NOTPRESENT:
                words = [word for word in words if word[key] != value.letter]

        print(len(words), "words left", sorted(words))


frequencies: dict = {
    "E": 12.02,
    "T": 9.1,
    "A": 8.12,
    "O": 7.68,
    "I": 7.31,
    "N": 6.95,
    "S": 6.28,
    "R": 6.02,
    "H": 5.92,
    "D": 4.32,
    "L": 3.98,
    "U": 2.88,
    "C": 2.71,
    "M": 2.61,
    "F": 2.3,
    "Y": 2.11,
    "W": 2.09,
    "G": 2.03,
    "P": 1.82,
    "B": 1.49,
    "V": 1.11,
    "K": 0.69,
    "X": 0.17,
    "Q": 0.11,
    "J": 0.1,
    "Z": 0.07, }


def calculate_frequency_score(word: str) -> float:
    return sum([frequencies[letter.upper()] for letter in word])


if __name__ == '__main__':

    all_words: list[str] = sorted([line.rstrip() for line in open("wordle.txt").readlines()])
    ranked_words = [(word, calculate_frequency_score(word)) for word in all_words if len(set(word)) == 5]
    ranked_words = sorted(ranked_words, key=lambda x: x[1], reverse=True)

    w = ranked_words[0]
    print(w, ranked_words[-1])
    print(len(all_words))
    for i in range(10):
        print(w[0])
        for l in w[0]:
            all_words = [word for word in all_words if l not in word]
            print(l, len(all_words))

        ranked_words = [(word, calculate_frequency_score(word)) for word in all_words if len(set(word)) == 5]
        ranked_words = sorted(ranked_words, key=lambda x: x[1], reverse=True)

        w = ranked_words[0]
        print(i, w, ranked_words[-1])
