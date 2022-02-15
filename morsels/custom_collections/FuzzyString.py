from collections import UserString


class FuzzyString(UserString):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __eq__(self, other):
        if isinstance(other, (str, FuzzyString)):
            return str(self.data).lower() == str(other).lower()
        return NotImplemented

    def __str__(self):
        return self.data

    def __repr__(self):
        return f"{self.data!r}"

    def __lt__(self, other):
        return not self.__gt__(other)

    def __le__(self, other):
        if isinstance(other, (str, FuzzyString)):
            print(str(self.data), str(other))
            return str(self.data) >= str(other)

    def __gt__(self, other):
        if isinstance(other, (str, FuzzyString)):
            print(str(self.data), str(other))
            return str(self.data) < str(other)

    def __ge__(self, other):
        if isinstance(other, (str, FuzzyString)):
            print(str(self.data), str(other))
            return str(self.data) <= str(other)

    def __contains__(self, item):
        return str(item).lower() in str(self.data).lower()


new_delhi = FuzzyString("NeW DELhi")
new = FuzzyString("New")
delhi = FuzzyString("Delhi")
print(new in new_delhi)

greeting = FuzzyString('Hey TREY!')
assert greeting == "hey trey!"
print(repr(greeting))
print(greeting)

o_word = FuzzyString('Octothorpe')
assert o_word > 'hashtag'

tokyo = FuzzyString("tokyo")
toronto = FuzzyString("TORONTO")
assert tokyo < toronto

assert 'OCTO' in o_word
city_name = FuzzyString("New Delhi")
city_name_part = FuzzyString("w del")
# assert city_name_part in city_name
