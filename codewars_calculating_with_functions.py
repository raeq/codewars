def number(f=None, num=0):
    if not f:
        return num
    else:
        return f(num)


def zero(f=None): return number(f, num = 0)


def one(f=None): return number(f, num = 1)


def two(f=None): return number(f, num = 2)


def three(f=None): return number(f, num = 3)


def four(f=None): return number(f, num = 4)


def five(f=None): return number(f, num = 5)


def six(f=None): return number(f, num = 6)


def seven(f=None): return number(f, num = 7)


def eight(f=None): return number(f, num = 8)


def nine(f=None): return number(f, num = 9)


def plus(y): return lambda x: x + y


def minus(y): return lambda x: x - y


def times(y): return lambda x: x * y


def divided_by(y): return lambda x: x // y


print(seven(times(five())))

assert (seven(times(five())) == 35)
assert (four(plus(nine())) == 13)
assert (eight(minus(three())) == 5)
assert (six(divided_by(two())) == 3)
