class deque:
    def __init__(self):
        self.l=[]
    def AddAtFront(self,element):
        self.l.insert(0,element)
    def AddAtEnd(self,element):
        self.l.append(element)
    def isEmpty(self):
        if len(self.l)==0:
            return True
        return False
    def delAtEnd(self):
        if self.isEmpty():
            print("list is empty")
            return
        else:
            delitem = self.l.pop()
            return delitem  
    def delAtFirst(self):
        if self.isEmpty():
            print("list is empty")
            return
        else:
            delitem = self.l.pop(0)
            return delitem
    def size(self):
        return len(self.l)
    def display(self):
        for each in self.l:
            print(each,end = " ")
        print()

Deque = deque()
Deque.AddAtEnd(6)
Deque.AddAtEnd(67)
Deque.AddAtFront(667)
Deque.display()
Deque.delAtEnd()
Deque.display()
        
