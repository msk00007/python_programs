class stack():
    def __init__(self):
        self.l=[]
    def push(self,element):
        self.l.append(element)
    def pop(self):
        if(len(self.l)==0):
            print("stack is empty..")
        else:
            self.l.pop()
    def peek(self):
        if(Stack.isEmpty()):
            print("Stack is empty..")
        else:
            print(self.l[-1])
    def isEmpty(self):
        if len(self.l) == 0:
            return True
        return False
    def display(self):
        print(self.l[::-1])
    def size(self):
        return len(self.l)
    

Stack = stack()
print(Stack.isEmpty())
# Stack.push(5)
# Stack.push(6)
# Stack.push(7)
Stack.display()
Stack.pop()
Stack.display()
print(Stack.isEmpty())
print(Stack.size())
Stack.peek()
