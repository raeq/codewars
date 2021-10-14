import random


def math_operation(x):
    # inner function which uses addition
    def inner_addition():
        return x + x

    # inner functions which uses multiplication
    def inner_multiplication():
        return x * x

    # choose which of the inner functions to return, randomly
    if random.choice([1, 2]) % 2 == 0:
        return inner_addition
    return inner_multiplication


for i in range(10):
    f = math_operation(7)
    print(f, f())
