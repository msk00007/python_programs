class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class linkedlist():
    def __init__(self):
        self.head = None
    def insert(self,element):
        if self.head ==None:
            new_node = node(element)
            self.head = new_node
            return
        else:
            if self.head.next == None:
                new_node = node(element)
                new_node.prev = self.head
                self.head.next = new_node
                
            else:
                itr = self.head
                while itr.next != None:
                    itr = itr.next
                new_node = node(element)
                new_node.prev = itr
                itr.next = new_node
    def delete(self,delelem):
        itr = self.head
        if itr is None :
            print("list is empty...")
            return
        elif itr.data == delelem :
            self.head = itr.next
            self.head.prev = None
            itr = None
            return
        while itr is not None and itr.data is not delelem :
            itr = itr.next
        if itr is None:
            print("element is not found ...")
        else:
            itr.prev.next = itr.next
            itr = None
    def printlist(self):
        if self.head is None:
            print("list is empty cant print list...")
            return
        itr = self.head
        while itr is not None:
            print(itr.data, end = " ")
            itr = itr.next
        print()
l = linkedlist()
l.insert(55)
l.insert(5)
l.insert(56)
l.insert(555)
l.printlist()
l.delete(56)
l.printlist()
l.insert(555)
l.printlist()
