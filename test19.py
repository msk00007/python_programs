

class node:
    def __init__(self,element):
        self.data = element
        self.next = None
class Queuelinked:
    def __init__(self):
        self.head = None
        self.tail = None
    def enque(self,elem):
        new_node = node(elem)
        itr = self.head
        if(itr == None):
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = self.tail.next

    def deque(self):
        if self.head == None:
            print("list is empty cannot perform deque")
        else:
            if self.head == self.tail:
                delelem = self.head.data
                self.head = None
                self.tail = None
                return delelem
            else:
                delelem = self.head.data
                self.head = self.head.next
                return delelem

    def isEmpty(self):
        if self.head == None:
            return True
        return False
    def front(self):
        if Queuelinked.isEmpty(self):
            return -1
        return self.head.data
    def display(self):
        if Queuelinked.isEmpty(self):
            print("Queue is empty cannot display")
        else:
            itr = self.head
            while(itr!=None):
                print(itr.data,end = " ")
                itr = itr.next
            print()

queue = Queuelinked()
print(queue.isEmpty())
queue.enque(4)
queue.enque(45)
queue.enque(456)
queue.display()
print(queue.deque())
queue.display()
queue.enque(4567)
queue.display()
print(queue.front())            
    
