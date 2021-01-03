class LRUCache:
    capacity: int
    cache: dict

    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.cache: dict = {}

    def get(self, key: int) -> int:
        try:
            value = self.cache.pop(key)
            self.cache.update({key: value})
            return value
        except KeyError:
            return -1

    def put(self, key: int, value: int) -> None:

        if key in self.cache.keys():
            self.cache.pop(key)
            self.cache[key] = value
        else:
            if len(self.cache) >= self.capacity:
                for k in self.cache.keys():
                    self.cache.pop(k)
                    break
            self.cache.update({key: value})

    def __repr__(self):
        return self.cache.__repr__()


obj = LRUCache(2)
obj.put(2, 6)
print(obj)
obj.put(1, 5)
print(obj)
obj.put(1, 2)
print(obj)
print(obj.get(1))
assert (obj.get(1)) == 2
print(obj)
print(obj.get(2))
assert (obj.get(2)) == 6
print(obj)
