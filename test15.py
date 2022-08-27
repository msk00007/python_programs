class node:
    def __init__(self,data):
        self.data = data
        self.front = None
        self.rear = None
class linkedlist():
    def __init__(self):
        self.head = None
    def insert(self,element):
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
    def delete(self,delelem):
        itr = self.head
        if itr is None :
            print("list is empty...")
            return
        elif itr.data == delelem :
            self.head = itr.front
            itr = None
            return
        while itr is not None and itr.data is not delelem :
            itr = itr.front
        if itr is None:
            print("element is not found ...")
            return
        elif itr.data == delelem and itr.front == None:
            itr.rear.front = None
            itr = None
        else:
            itr.rear.front = itr.front
            itr = None
    def printlist(self):
        if self.head is None:
            print("list is empty cant print list...")
            return
        itr = self.head
        while itr is not None:
            print(itr.data, end = " ")
            itr = itr.front
        print()
l = linkedlist()
l.insert(55)
l.insert(5)
l.insert(56)
l.insert(555)
l.printlist()
l.delete(5)
l.printlist()
l.insert(555)
l.printlist()