"""
From a text corpus, list the most frequent words according to word length.
Most frequent word of length 1 first, most frequent words of length 2 next.
If there is a tie for frequency, return the words with the same, highest frequency.
If there are no words of a specific length, no output.
"""

import re
from collections import Counter, defaultdict


text = """
Some glory in their birth, some in their skill,
Some in their wealth, some in their bodies' force,
Some in their garments, though new-fangled ill,
Some in their hawks and hounds, some in their horse;
"""


# Extract words from punctuation
def get_words(text) -> list:
    words = []
    pattern = r"\b(\w+)\b"
    matches = re.finditer(pattern, text, re.MULTILINE)
    for match in matches:
        yield (match.groups()[0].lower())


def make_lengths(my_input: dict) -> list:
    my_output = defaultdict(list)
    for k, v in my_input.items():
        my_output[len(k)].append((k, v))
    return sorted(my_output.items())


def filter_top_frequencies(my_input: list) -> list:
    my_output = []
    for i, j in my_input:
        maxi = max(j, key=lambda x: x[1])[1]
        yield (i, (list(filter(lambda x: x[1] == maxi, j))))


words = get_words(text)
make_counter = Counter(words)

lengths = make_lengths(make_counter)

top = filter_top_frequencies(lengths)
print([x for x in top])
