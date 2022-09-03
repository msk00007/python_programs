class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class doublylinkedlist():
    def __init__(self):
        self.head = None

    def enqueAtfirst(self,element):
        if self.head is None:
            new_node = node(element)
            self.head = new_node
            return
        else:
            new_node = node(element)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def enqueAtEnd(self,element):
        new_node = node(element)
        if self.head ==None:
            self.head = new_node
            return
        else:
            if self.head.next == None:
                new_node.prev = self.head
                self.head.next = new_node     
            else:
                itr = self.head
                while itr.next != None:
                    itr = itr.next
                new_node.prev = itr
                itr.next = new_node
    def dequeAtEnd(self):
        itr = self.head
        if itr is None :
            print("list is empty...")
            return
        elif itr.next == None :
            self.head = itr.next
            itr = None
            return
        while itr.next is not None :
            itr = itr.next
        itr.prev.next = itr.next
        itr = None
    def dequeAtFirst(self):
        itr = self.head
        if itr is None:
            print("list is empty .....")
        elif itr.next == None:
            self.head = itr.next
            itr = None
        else:
            itr.next.prev = itr.prev
            self.head = itr.next
            itr= None
    def display(self):
        if self.head is None:
            print("list is empty cant print list...")
            return
        itr = self.head
        while itr is not None:
            print(itr.data, end = " ")
            itr = itr.next
        print()
    def isEmpty(self):
        if self.head is None:
            return True
        return False
Queue = doublylinkedlist()
print(Queue.isEmpty())
Queue.enqueAtEnd(5)
Queue.enqueAtEnd(58)
Queue.display()
Queue.dequeAtEnd()
Queue.display()
Queue.enqueAtfirst(1)
Queue.enqueAtfirst(10)
Queue.display()
Queue.dequeAtFirst()
Queue.display()
Queue.enqueAtfirst(15)
Queue.display()
print(Queue.isEmpty())
