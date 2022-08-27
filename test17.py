class node:
    def __init__(self,data):
        self.data = data
        self.front = None
        self.rear = None
class linkedlist():
    def __init__(self):
        self.head = None

    def enqueAtfirst(self,element):
        if self.head is None:
            new_node = node(element)
            self.head = new_node
            return
        else:
            new_node = node(element)
            new_node.front = self.head
            self.head.rear = new_node
            self.head = new_node

    def enqueAtEnd(self,element):
        if self.head ==None:
            new_node = node(element)
            self.head = new_node
            return
        else:
            if self.head.front == None:
                new_node = node(element)
                new_node.rear = self.head
                self.head.front = new_node
                
            else:
                itr = self.head
                while itr.front != None:
                    itr = itr.front
                new_node = node(element)
                new_node.rear = itr
                itr.front = new_node
    def dequeAtEnd(self):
        itr = self.head
        if itr is None :
            print("list is empty...")
            return
        elif itr.front == None :
            self.head = itr.front
            itr = None
            return
        while itr.front is not None :
            itr = itr.front
        itr.rear.front = itr.front
        itr = None
    def dequeAtFirst(self):
        itr = self.head
        if itr is None:
            print("list is empty .....")
            return
        elif itr.front == None:
            self.head = itr.front
            itr = None
            return
        else:
            itr.front.rear = itr.rear
            self.head = itr.front
    def display(self):
        if self.head is None:
            print("list is empty cant print list...")
            return
        itr = self.head
        while itr is not None:
            print(itr.data, end = " ")
            itr = itr.front
        print()
    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False
Queue = linkedlist()
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
print(Queue.isEmpty())