class queue():
    def __init__(self):
        self.l=[]
    def Add(self,element):
        self.l.append(element)
    def remove(self):
        self.l.pop(0)
    def peek(self):
        print(self.l[-1])
    def isEmpty(self):
        if len(self.l) == 0:
            return True
        
        return False
    def display(self):
        print(self.l)
    def size(self):
        return len(self.l)
    

Queue = queue()
print(Queue.isEmpty())
Queue.Add(5)
Queue.Add(6)
Queue.Add(7)
Queue.display()
Queue.remove()
Queue.display()
print(Queue.isEmpty())
print(Queue.size())