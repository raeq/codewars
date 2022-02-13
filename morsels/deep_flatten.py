from typing import Iterable


def deep_flatten(nested: Iterable) -> Iterable:
    for value in nested:

        if isinstance(value, (str, bytes)):
            yield value
        elif isinstance(value, Iterable):
            for nested_value in deep_flatten(value):
                yield nested_value
        else:
            yield value


for x in deep_flatten([[(1, 2), [(3, 4)]], [[5, [6]], {8, 7}], {9: 0}]):
    print(x)

print(list(deep_flatten([['apple', 'pickle'], [['pear', 'avocado']]])))
