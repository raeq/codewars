from functools import reduce
import operator


def solution(number):
    if number < 1: return 0

    numbers: list = []

    for i in range(1, number):
        if i % 3 == 0:
            numbers.append(i)
        elif i % 5 == 0:
            numbers.append(i)

    if numbers:
        return reduce(operator.add, numbers)
    else:
        return 0

print(solution(10))