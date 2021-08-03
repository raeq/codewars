import string


def rotate(value, rotation=13, as_string=True):
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

    if as_string:
        return _translate_to_string(value)
    return _translate(value)


input_str = "Text in zig zag mode"
alternate = 0
build_str = ""
for c in input_str:
    alternate += 1
    if alternate % 2:
        build_str += rotate(c)
    else:
        build_str += c

print(build_str)
