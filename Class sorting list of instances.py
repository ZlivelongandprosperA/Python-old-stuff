class Fruit():
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __str__(self):
        return "{}, {}".format(self.name, self.price)

L = [Fruit("Cherry", 10), Fruit("Apple", 5), Fruit("Blueberry", 20)]


for f in sorted(L, key=lambda x: x.name):
    print(f.price)

for f in sorted(L, key=lambda x: x.price):
    print(f.name)
