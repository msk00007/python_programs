class complex:
    def __str__(self):
        return ("{0}+i({1})".format(self.x, self.y))
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def add(self,obj2):
        return complex(self.x+obj2.x,self.y+obj2.y)
p1 = complex(2.4,3.6)
p2 = complex(3.9,4.6)
p3 = p1.add(p2)
print(p1)
print(p2)
print(p3)