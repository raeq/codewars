"""
https://www.hackerrank.com/challenges/utopian-tree/problem
"""


def utopianTree(n: int) -> int:
    if n == 0:
        return 1
    if n == 1:
        return 2

    if n == 2:
        return 3
    if n == 3:
        return 6

    if n == 4:
        return 7
    if n == 5:
        return 14

    if n == 6:
        return 15
    if n == 7:
        return 30

    current = 30
    for i in range(7, n):
        if i % 2:
            current = current + 1
        else:
            current = current * 2

    return current


assert (utopianTree(4) == 7)
assert (utopianTree(8) == 31)
assert (utopianTree(9) == 62)
assert (utopianTree(10) == 63)
