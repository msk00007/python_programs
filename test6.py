class complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display(self):
         print("{0}+i{1}".format(self.x, self.y))

    def __add__(self, other):
        return complex(self.x + other.x, self.y + other.y)
    def __sub__(self,other):
        return complex(self.x-other.x,self.y-other.y)
    def __mul__(self,other):
        x = self.x*other.x - (self.y*other.y)
        y = self.x*other.y + self.y*other.x
        return(complex(x,y))


p1 = complex(5,4)
p2 = complex(2, 3)
p3=p1+p2
p4 = p1-p2
p5 = p1*p2
p3.display()
p4.display()
p5.display()
