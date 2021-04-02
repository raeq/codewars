import string


def rotate(value, rotation=13, getstring=True):
    def _make_translation(_rotation):
        t = {}
        for c in string.ascii_lowercase:
            t[c] = chr((((ord(c) - 97) + _rotation) % 26) + 97)
        for c in string.ascii_uppercase:
            t[c] = chr((((ord(c) - 65) + _rotation) % 26) + 65)
        for d in string.digits:
            t[d] = str((int(d) + 5) % 10)

        return t

    def _translate(_value):
        try:
            _translation_table = _make_translation(rotation)
            for c in _value:
                yield _translation_table.get(c, c)
        except Exception as e:
            raise RuntimeError from e

    def _translate_to_string(_value):
        return "".join(_translate(_value))

    if getstring:
        return _translate_to_string(value)
    return _translate(value)


print(rotate("Test1 Hello3", getstring=True))
print(rotate("Grfg6 Uryyb8", getstring=True))
