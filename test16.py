class node:
    def __init__(self,data):
        self.data = data
        self.Next = None
class linkedlist():
    def __init__(self):
        self.head = None
    def enqueAtEnd(self,element):
        if self.head ==None:
            new_node = node(element)
            self.head = new_node
            return
        else:
            if self.head.Next == None:
                new_node = node(element)
                self.head.Next = new_node
            else:
                itr = self.head
                while itr.Next != None:
                    itr = itr.Next
                new_node = node(element)
                itr.Next = new_node
    def enqueAtfirst(self,element):
        if self.head ==None:
            new_node = node(element)
            self.head = new_node
            return
        else:
            new_node = node(element)
            new_node.Next = self.head
            self.head = new_node

    def dequeAtEnd(self):
        itr = self.head
        if itr is None :
            print("list is empty...")
            return
        elif itr.Next is None:
            self.head = itr.Next
            itr = None
            return
        prev = itr
        while itr.Next is not None :
            prev = itr
            itr = itr.Next
        prev.Next = itr.Next
        itr = None
    def dequeAtFirst(self):
        itr = self.head
        if itr is None :
            print("list is empty...")
            return
        else:
            self.head = itr.Next
            itr = None
            return

    def display(self):
        if self.head is None:
            print("list is empty cant print list...")
            return
        itr = self.head
        while itr is not None:
            print(itr.data, end = " ")
            itr = itr.Next
        print()
    def isEmpty(self):
            if self.head is None:
                return True
            else:
                return False
dueue = linkedlist()
print(dueue.isEmpty())
dueue.enqueAtEnd(5)
dueue.enqueAtEnd(58)
dueue.enqueAtEnd(585)
dueue.display()
dueue.dequeAtEnd()
dueue.display()
dueue.enqueAtfirst(1)
dueue.enqueAtfirst(10)
dueue.display()
dueue.dequeAtFirst()
dueue.display()
dueue.dequeAtFirst()
dueue.display()
print(dueue.isEmpty())