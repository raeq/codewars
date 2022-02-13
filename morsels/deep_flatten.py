from typing import Iterable, Any


def deep_flatten(nested: Iterable[Any]) -> Iterable[Any]:
    for value in nested:

        if isinstance(value, (str, bytes)):
            yield value
        elif isinstance(value, Iterable):
            yield from deep_flatten(value)
        else:
            yield value


for x in deep_flatten([[(1, 2), [(3, 4)]], [[5, [6]], {8, 7}], {9: 0}]):
    print(x)

print(list(deep_flatten([['apple', 'pickle'], [['pear', 'avocado']]])))
