class complex:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def display(self):
         print("{0}+i{1}".format(self.x, self.y))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return complex(x, y)


p1 = complex(5,4)
p2 = complex(2, 3)
p3=p1+p2
p3.display()