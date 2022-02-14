import logging
from contextlib import ContextDecorator


class suppress(ContextDecorator):
    _suppressed: list[Exception]

    def __init__(self, *args, name=None, **kwargs):
        self.name = name
        self._suppressed = [*args]

    def __

    def __enter__(self, *args, **kwargs):
        print(self._suppressed)
        try:
            yield
        except (self._suppressed) as e:
            print(e)

    def __exit__(self, exc_type, exc, exc_tb):
        logging.info('Exiting: %s', self.name)


with suppress(ValueError, RuntimeError):
    print("hello")
