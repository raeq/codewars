from contextlib import ContextDecorator


class suppress(ContextDecorator):
    _suppressed: list[Exception]

    def __init__(self, *args, name=None, **kwargs):
        self.name = name
        self._suppressed = [*args]


    def __enter__(self, *args, **kwargs):
        self.exception = None
        self.traceback = None
        return self

    def __exit__(self, exc_type, exc, exc_tb):
        if exc_type:
            for suppressed in self._suppressed:
                if issubclass(exc_type, suppressed):
                    self.exception = exc
                    self.traceback = exc_tb
                    return True


context: suppress
with suppress(ValueError, RuntimeError) as context:
    print("hello")
    print(context.exception)
