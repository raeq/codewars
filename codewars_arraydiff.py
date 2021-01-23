"""
Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the
result. It should remove all values from list a, which are present in list b.
array_diff([1,2],[1]) == [2]
"""


def array_diff(a, b):
    return [_ for _ in a if _ not in b]


assert (array_diff([1, 2], [1]) == [2])
assert (array_diff([1, 2, 2], [1]) == [2, 2])
assert (array_diff([1, 2, 2], [2]) == [1])
assert (array_diff([1, 2, 2], []) == [1, 2, 2])
assert (array_diff([], [1, 2]) == [])
