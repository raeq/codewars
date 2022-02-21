from abc import ABC, abstractmethod


class Validator(ABC):

    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        self.validate(value)
        setattr(obj, self.private_name, value)

    @abstractmethod
    def validate(self, value):
        pass


class OneOf(Validator):

    def __init__(self, *options):
        self.options = set(options)

    def validate(self, value):
        if not value or value not in self.options:
            raise ValueError(f'Expected {value!r} to be one of {self.options!r}')


class NoneOf(Validator):

    def __init__(self, *options):
        self.options = set(options)

    def validate(self, value):
        if not value or value in self.options:
            raise ValueError(f'Expected {value!r} to not be one of {self.options!r}')


class Number(Validator):

    def __init__(self, minvalue=None, maxvalue=None):
        self.minvalue = minvalue
        self.maxvalue = maxvalue

    def validate(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f'Expected {value!r} to be an int or float')
        if self.minvalue is not None and value < self.minvalue:
            raise ValueError(
                f'Expected {value!r} to be at least {self.minvalue!r}'
            )
        if self.maxvalue is not None and value > self.maxvalue:
            raise ValueError(
                f'Expected {value!r} to be no more than {self.maxvalue!r}'
            )


class ValidatedString(Validator):

    def __init__(self, minsize=None, maxsize=None, predicate=None,
                 must_uppercase_count=0,
                 must_lowercase_count=0,
                 must_symbol_count=0,
                 must_whitespace_count=0,
                 must_digit_count=0,
                 ):

        self.minsize = minsize
        self.maxsize = maxsize
        self.predicate = predicate
        self.must_symbol_count = must_symbol_count
        self.must_uppercase_count = must_uppercase_count
        self.must_lowercase_count = must_lowercase_count
        self.must_whitespace_count = must_whitespace_count
        self.must_digit_count = must_digit_count

    def validate(self, value):
        import string

        if not isinstance(value, str):
            raise TypeError(f'Expected {value!r} to be an str')
        if self.minsize is not None and len(value) < self.minsize:
            raise ValueError(
                f'Expected {value!r} to be no smaller than {self.minsize!r}'
            )
        if self.maxsize is not None and len(value) > self.maxsize:
            raise ValueError(
                f'Expected {value!r} to be no bigger than {self.maxsize!r}'
            )
        if self.predicate is not None and not self.predicate(value):
            raise ValueError(
                f'Expected {self.predicate} to be true for {value!r}'
            )
        if self.must_symbol_count and sum([True for x in value if x in string.punctuation]) \
                < self.must_symbol_count:
            raise ValueError(
                f'Expected at least {self.must_symbol_count} symbols in {value!r}'
            )
        if self.must_uppercase_count and sum([True for x in value if x in string.ascii_uppercase]) \
                < self.must_uppercase_count:
            raise ValueError(
                f'Expected at least {self.must_uppercase_count} uppercase in {value!r}'
            )
        if self.must_lowercase_count and sum([True for x in value if x in string.ascii_lowercase]) \
                < self.must_lowercase_count:
            print(self.must_lowercase_count, sum([True for x in value if x in string.ascii_lowercase]))
            raise ValueError(
                f'Expected at least {self.must_lowercase_count} lowercase in {value!r}'
            )
        if self.must_whitespace_count and sum([True for x in value if x in string.whitespace]) \
                < self.must_whitespace_count:
            raise ValueError(
                f'Expected at least {self.must_whitespace_count} whitespace in {value!r}'
            )
        if self.must_digit_count and sum([True for x in value if x in string.digits]) \
                < self.must_digit_count:
            raise ValueError(
                f'Expected at least {self.must_digit_count} digits in {value!r}'
            )
