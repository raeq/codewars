def mypow(a: int, b: int, m: int = None) -> int:
    if m:
        return pow(a, b) % m
    else:
        return pow(a, b)


if __name__ == "__main__":

    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())

    print(pow(a, b) + pow(c, d))
