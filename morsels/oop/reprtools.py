import inspect


def format_arguments(*args, **kwargs):
    arg_strings = (
        repr(a)
        for a in args
    )
    kwarg_strings = (
        f"{name}={value!r}"
        for name, value in kwargs.items()
    )
    return ", ".join([*arg_strings, *kwarg_strings])


def make_repr(*, args=(), kwargs=()):
    def __repr__(self):
        arg_values = [
            getattr(self, a)
            for a in args
        ]
        kwarg_values = {
            a: getattr(self, a)
            for a in kwargs
        }
        arg_string = format_arguments(*arg_values, **kwarg_values)
        return f"{type(self).__name__}({arg_string})"

    return __repr__


def make_repr_automatically():
    def __repr__(self):
        signature = inspect.signature(self.__init__)
        kwarg_values = {
            a: getattr(self, a)
            for a in signature.parameters
            if hasattr(self, a)
        }
        signature.bind(**kwarg_values)
        arg_string = format_arguments(**kwarg_values)
        return f"{type(self).__name__}({arg_string})"

    return __repr__


def auto_repr(cls=None, /, *, args=(), kwargs=()):
    def decorator(cls):
        cls.__repr__ = make_repr(args=args, kwargs=kwargs)
        return cls

    if cls:
        cls.__repr__ = make_repr_automatically()
        return cls
    return decorator
