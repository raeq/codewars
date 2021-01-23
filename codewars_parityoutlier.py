"""
You are given an array (which will have a length of at least 3, but could be very large) containing integers. The
array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer
N. Write a method that takes the array as an argument and returns this "outlier" N.

https://www.codewars.com/kata/5526fc09a1bbd946250002dc/train/python

[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)
"""


def find_outlier(integers):
    if len(integers) < 3:
        raise AttributeError()

    evens = 0
    count = 0
    for i in integers:
        if i % 2 == 0:
            evens += 1
        if count == 2:
            break
        count += 1

    integers = set(integers)

    if evens > 1:
        for _ in integers:
            if _ % 2 == 1:
                return _

    else:
        for _ in integers:
            if _ % 2 == 0:
                return _


assert (find_outlier([0, 1, 0]) == 1)
assert (find_outlier([2, 4, 6, 8, 10, 3]) == 3)
assert (find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]) == 11)
assert (find_outlier([160, 3, 1719, 19, 11, 13, -21]) == 160)
