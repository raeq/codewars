"""
Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until
a single-digit number is produced. The input will be a non-negative integer.
"""


def digital_root(n):
    input = str(n)

    while len(input) != 1:
        temp: int = 0
        for char in input:
            temp += int(char)
        input = str(temp)

    return int(input)

print (digital_root(132189))