class complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display(self):
         print("{0}+i({1})".format(self.x, self.y))

    def __add__(self, other):
        return complex(self.x + other.x, self.y + other.y)
    def __sub__(self,other):
        return complex(round(self.x-other.x,3),round(self.y-other.y,3))
    def __mul__(self,other):
        x = self.x*other.x - (self.y*other.y)
        y = self.x*other.y + self.y*other.x
        return(complex(round(x,3),round(y,3)))

a = float(input("enter first real num \n"))
b = float(input("enter first imagiary num \n"))
c = float(input("enter second real num \n"))
d = float(input("enter secong imaginary num \n"))
p1 = complex(a,b)
p2 = complex(c, d)
p3=p1+p2
p4 = p1-p2
p5 = p1*p2
p3.display()
p4.display()
p5.display()
