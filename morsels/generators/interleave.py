"""
For this problem, I want you to write a function called interleave which accepts two iterables of any type and return
a new iterable with each of the given items "interleaved" (item 0 from iterable 1, then item 0 from iterable 2,
then item 1 from iterable 1, and so on).
"""
from typing import Iterator


def interleave(*iterables):
    iterators = [iter(i) for i in iterables]
    while iterators:
        for iterator in list(iterators):
            try:
                yield next(iterator)
            except StopIteration:
                iterators.remove(iterator)


def interleave2(*sequences) -> Iterator:
    my_iterables = []
    stopped = []

    for iterab in sequences:
        my_iterables.append(iter(iterab))
        stopped.append(False)

    while not all(stopped):
        for idx, iterab in enumerate(my_iterables):
            try:
                if not stopped[idx]:
                    yield next(iterab)
            except StopIteration:
                stopped[idx] = True
