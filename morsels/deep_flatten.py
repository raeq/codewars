from collections.abc import Iterable as Iterable2
from typing import Iterable, Any


def deep_flatten(nested: Iterable[Any]) -> Iterable[Any]:
    """Flatten an iterable of iterables."""
    for item in nested:
        match item:
            case str() | bytes():
                yield item
            case Iterable2():
                yield from deep_flatten(item)
            case _:
                yield item


for x in deep_flatten([[(1, 2), [(3, 4)]], [[5, [6]], {8, 7}], {9: 0}]):
    print(x)

print(list(deep_flatten([['apple', 'pickle'], [['pear', 'avocado']]])))
