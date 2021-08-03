class Item():

    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price


class ShoppingCart:
    items: list

    def __init__(self):
        self.items = []

    def add(self, item: Item):
        self.items.append(item)

    def total(self):
        return sum([i.price for i in self.items])

    def __len__(self):
        return len(self.items)


if __name__ == '__main__':
    pass

b = Item("bike", 1000)
h = Item("headphones", 100)
c = ShoppingCart()

print(len(c))
c.add(b)
print(c.total())
c.add(b)
print(len(c))
print(c.total())
