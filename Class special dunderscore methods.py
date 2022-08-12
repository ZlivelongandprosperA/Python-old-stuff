class Point():
    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY
    def __str__(self):
        return 'Point ({}, {})'.format(self.x, self.y)
    def __add__(self, otherPoint):
        return Point(self.x + otherPoint.x,
                     self.y + otherPoint.y)
    def __sub__(self, otherPoint):
        return Point(self.x - otherPoint.x,
                     self.y - otherPoint.y)

p1 = Point(-5, 10)
p2 = Point(15, 20)
print(p1)
print(p2)
print(p1 + p2)
print(p1 - p2)