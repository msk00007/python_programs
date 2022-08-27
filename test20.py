class stack():
    def __init__(self):
        self.l=[]
    def push(self,element):
        self.l.append(element)
    def pop(self):
        self.l.pop()
    def peek(self):
        print(self.l[-1])
    def isEmpty(self):
        if len(self.l) == 0:
            return True
        
        return False
    def display(self):
        print(self.l)
    

Stack = stack()
print(Stack.isEmpty())
Stack.push(5)
Stack.push(6)
Stack.push(7)
Stack.display()
Stack.pop()
Stack.display()
print(Stack.isEmpty())