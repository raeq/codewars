"""
https://www.hackerrank.com/challenges/list-comprehensions/problem
"""


def calc(x, y, z, n):
    out = []
    for a in range(x + 1):
        for b in range(y + 1):
            for c in range(z + 1):
                if (a + b + c) != n:
                    out.append([a, b, c])

    return out


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    print(calc(x, y, z, n))
