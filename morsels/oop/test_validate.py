import unittest

from validate import ValidatedString, OneOf, NoneOf, Number


class MyTestCase(unittest.TestCase):
    def test_no_validators(self):
        class Component:
            name = ValidatedString(minsize=0,
                                   maxsize=None,
                                   predicate=None,
                                   must_lowercase_count=0,
                                   must_digit_count=0,
                                   must_symbol_count=0,
                                   must_uppercase_count=0,
                                   must_whitespace_count=0, )
            kind = OneOf('wood', 'metal', 'plastic')
            notkind = NoneOf(1, 2, 3)
            quantity = Number(minvalue=0)

            def __init__(self, name, kind, notkind, quantity):
                self.name = name
                self.kind = kind
                self.notkind = notkind
                self.quantity = quantity


        c = Component(name="", kind="metal", notkind=4, quantity=1)

    def test_fail_string_validation_error(self):
        class Component:
            name = ValidatedString(minsize=6,
                                   maxsize=10,
                                   predicate=None,
                                   must_lowercase_count=1,
                                   must_digit_count=1,
                                   must_symbol_count=1,
                                   must_uppercase_count=1,
                                   must_whitespace_count=1, )
            kind = OneOf('wood', 'metal', 'plastic')
            notkind = NoneOf(1, 2, 3)
            quantity = Number(minvalue=0)

            def __init__(self, name, kind, notkind, quantity):
                self.name = name
                self.kind = kind
                self.notkind = notkind
                self.quantity = quantity


        c = Component(name="a 5%Ax", kind="metal", notkind=4, quantity=1)
        with self.assertRaises(ValueError):
            c = Component(name="a A5a", kind="metal", notkind=4, quantity=1)
        with self.assertRaises(ValueError):
            c = Component(name="a A5ax", kind="metal", notkind=4, quantity=1)
        with self.assertRaises(ValueError):
            c = Component(name="a Aa%x", kind="metal", notkind=4, quantity=1)
        with self.assertRaises(ValueError):
            c = Component(name="a a5%x", kind="metal", notkind=4, quantity=1)
        with self.assertRaises(ValueError):
            c = Component(name="aaA5%x", kind="metal", notkind=4, quantity=1)
        with self.assertRaises(ValueError):
            c = Component(name="aaA5%a aA5%aaA5%aaA5%", kind="metal", notkind=4, quantity=1)

    def test_fail_oneof_validation_error(self):
        class Component:
            name = ValidatedString(minsize=6,
                                   maxsize=10,
                                   predicate=None,
                                   must_lowercase_count=1,
                                   must_digit_count=1,
                                   must_symbol_count=1,
                                   must_uppercase_count=1,
                                   must_whitespace_count=1, )
            kind = OneOf('wood', 'metal', 'plastic')
            notkind = NoneOf(1, 2, 3)
            quantity = Number(minvalue=0)

            def __init__(self, name, kind, notkind, quantity):
                self.name = name
                self.kind = kind
                self.notkind = notkind
                self.quantity = quantity


        c = Component(name="a 5%Ax", kind="wood", notkind=4, quantity=1)
        with self.assertRaises(ValueError):
            c = Component(name="a 5%Ax", kind="Wood", notkind=4, quantity=1)
        with self.assertRaises(ValueError):
            c = Component(name="a 5%Ax", kind=" wood", notkind=4, quantity=1)
        with self.assertRaises(ValueError):
            c = Component(name="a 5%Ax", kind=None, notkind=4, quantity=1)
        with self.assertRaises(ValueError):
            c = Component(name="a 5%Ax", kind="cheese", notkind=4, quantity=1)
        with self.assertRaises(TypeError):
            c = Component(name="a 5%Ax", notkind=4, quantity=1)

    def test_fail_noneof_validation_error(self):
        class Component:
            name = ValidatedString(minsize=6,
                                   maxsize=10,
                                   predicate=None,
                                   must_lowercase_count=1,
                                   must_digit_count=1,
                                   must_symbol_count=1,
                                   must_uppercase_count=1,
                                   must_whitespace_count=1, )
            kind = OneOf('wood', 'metal', 'plastic')
            notkind = NoneOf(1, 2, 3)
            quantity = Number(minvalue=0)

            def __init__(self, name, kind, notkind, quantity):
                self.name = name
                self.kind = kind
                self.notkind = notkind
                self.quantity = quantity


        c = Component(name="a 5%Ax", kind="wood", notkind=4, quantity=1)
        with self.assertRaises(ValueError):
            c = Component(name="a 5%Ax", kind="wood", notkind=1, quantity=1)
        with self.assertRaises(ValueError):
            c = Component(name="a 5%Ax", kind="wood", notkind=4 - 1, quantity=1)
        with self.assertRaises(ValueError):
            c = Component(name="a 5%Ax", kind="wood", notkind=None, quantity=1)
        with self.assertRaises(TypeError):
            c = Component(name="a 5%Ax", kind="wood", quantity=1)

    def test_fail_number_validation_error(self):
        class Component:
            name = ValidatedString(minsize=6,
                                   maxsize=10,
                                   predicate=None,
                                   must_lowercase_count=1,
                                   must_digit_count=1,
                                   must_symbol_count=1,
                                   must_uppercase_count=1,
                                   must_whitespace_count=1, )
            kind = OneOf('wood', 'metal', 'plastic')
            notkind = NoneOf(1, 2, 3)
            quantity = Number(maxvalue=50, minvalue=4)

            def __init__(self, name, kind, notkind, quantity):
                self.name = name
                self.kind = kind
                self.notkind = notkind
                self.quantity = quantity


        c = Component(name="a 5%Ax", kind="wood", notkind=4, quantity=5)
        with self.assertRaises(ValueError):
            c = Component(name="a 5%Ax", kind="wood", notkind=4, quantity=100)
        with self.assertRaises(ValueError):
            c = Component(name="a 5%Ax", kind="wood", notkind=5, quantity=3)
        with self.assertRaises(ValueError):
            c = Component(name="a 5%Ax", kind="wood", notkind=3, quantity=51)
        c = Component(name="a 5%Ax", kind="wood", notkind=5, quantity=49)
        c = Component(name="a 5%Ax", kind="wood", notkind=5, quantity=4)
        with self.assertRaises(TypeError):
            c = Component(name="a 5%Ax", kind="wood", notkind=4, quantity=None)


if __name__ == '__main__':
    unittest.main()
