class rechatngle:
    
    def __init__(self,length,breadth):
        self.length= length
        self.breadth = breadth
    def area(self):
        return self.length*self.breadth
    def paremeter(self):
        return 2*(self.length+self.breadth)
    def lenofrec(self):
        return self.length
    def breofrec(self):
        return self.breadth
    
R1=rechatngle(5,6)
print(R1.area)

        
