import string


def print_rangoli(n):
    c: str = ""
    d: str = ""
    lines = []
    if n == 1:
        print("a")
        return

    for i in range(1, n + 1):

        d = d + string.ascii_lowercase[n - i] + "-"
        if i > 1:
            c = d[:-3] + d[-1::-1]
        else:
            c = d

        lines.append(c.center(n * 4 - 3, "-"))

    for l in lines[:-1]:
        print(l)

    for l in lines[::-1]:
        print(l)


if __name__ == '__main__':
    n = 10  # int(input())
    print_rangoli(n)
