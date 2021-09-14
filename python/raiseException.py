class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return(f"x axis is({self.x}, {self.y})")


p = Point(1, 2)
print(str(p))
