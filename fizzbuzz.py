"""
Write a program that prints the numbers from 1 to 100. But for multiples of three print "Fizz" instead of the number
and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

https://blog.codinghorror.com/why-cant-programmers-program/
"""


def FizzBuzz(value: int) -> str:
    if not isinstance(value, int):
        raise ValueError(f"{value} is of type {type(value)} but it should be an int.")

    return_val: str = ""
    if value % 3 == 0:
        return_val = "Fizz"

    if value % 5 == 0:
        return_val += "Buzz"

    return return_val if return_val else str(value)


for i in range(1, 101):
    print(FizzBuzz(i))
