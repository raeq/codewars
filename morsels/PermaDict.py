"""
I want you to create a dictionary-like class that disallows keys to be updated (they can only be added or removed).
And your PermaDict class should have keys, values, and items methods and should be iterable just like a dictionary:
"""
import collections


class PermaDict(collections.UserDict):

    # def __init__(self, dict=None, /, **kwargs):

    def __init__(self, dict=None, *args, silent=False, **kwargs):
        self.data = {}
        self._silent = silent

        super().__init__(dict, **kwargs)

    def force_set(self, key, value):
        return super().__setitem__(key, value)

    def __setitem__(self, key, value):
        if key not in self:
            return super().__setitem__(key, value)
        if not self._silent:
            raise KeyError(f"{key!r} already in dictionary.")

    def update(self, *args, force=False, **kwargs):
        if force:
            return self.data.update(*args, **kwargs)
        else:
            return super().update(*args, **kwargs)


e = PermaDict(silent=True, not_silent=False, super_silent=True)
print(e)
assert e == {'not_silent': False, 'super_silent': True}

d = PermaDict({1: 2, 3: 4}, silent=True)
d.update([(5, 6), (1, 8), (7, 8)])
assert d == {1: 2, 3: 4, 5: 6, 7: 8}
print(d)
d[3] = 6
d[9] = 10
assert d == {1: 2, 3: 4, 5: 6, 7: 8, 9: 10}
print(d)

locations = PermaDict({'Trey': "San Diego", 'Al': "San Francisco"})
locations['Harry'] = "London"
locations.update({'Russell': "Perth", 'Katie': "Sydney"})
locations['Asheesh'] = "Boston"
locations[4] = "the number four"

print(locations)
locations.force_set('Asheesh', "San Francisco")

locations = PermaDict([('Kojo', "Houston"), ('Tracy', "Toronto")])
print(locations)
locations.force_set('Kojo', "San Francisco")
locations['Asheesh'] = "Boston"

locations = PermaDict({'David': "Boston"}, silent=True)
locations['David'] = "Amsterdam"
