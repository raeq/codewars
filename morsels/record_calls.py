from dataclasses import dataclass
from functools import wraps
from typing import Any, Optional


NO_RETURN = object()


@dataclass
class Call:
    args: tuple
    kwargs: dict
    return_value: Any = NO_RETURN
    exception: Optional[BaseException] = None


def record_calls(func):
    """Record calls to the given function."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        call = Call(args, kwargs)
        wrapper.calls.append(call)
        try:
            call.return_value = func(*args, **kwargs)
        except BaseException as e:
            call.exception = e
            raise
        return call.return_value

    wrapper.call_count = 0
    wrapper.calls = []
    return wrapper


@record_calls
def greet(name="world"):
    """Greet someone by their name."""
    return f"Hello {name}"


for i in range(50):
    print(f"Calling {greet(i)} {greet.call_count} ")
print(greet.call_count)
