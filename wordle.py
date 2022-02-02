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


words: list[str] = [line.rstrip() for line in open("wordle.txt").readlines()]


def parse_input(user_input: str) -> list[Guess]:
    parsed_input = []

    for pair in chunked(user_input, 2):
        g = Guess(letter=pair[0].lower(),
                  result=Result(int(pair[1])))
        parsed_input.append(g)

    return parsed_input


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
