class node:
    def __init__(self,data):
        self.data = data
        self.Next = None
class linkedlist():
    def __init__(self):
        self.head = None
    def insert(self,element):
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
    def delete(self,delelem):
        itr = self.head
        if itr is None :
            print("list is empty...")
            return
        elif itr.data == delelem :
            self.head = itr.Next
            itr = None
            return
        prev = itr
        while itr is not None and itr.data is not delelem :
            prev = itr
            itr = itr.Next
        if itr is None:
            print("element is not found ...")
            return
        elif itr.data == delelem :
            prev.Next = itr.Next
    def printlist(self):
        if self.head is None:
            print("list is empty cant print list...")
            return
        itr = self.head
        while itr is not None:
            print(itr.data, end = " ")
            itr = itr.Next
        print()
l = linkedlist()
l.insert(55)
l.insert(5)
l.insert(56)
l.insert(555)
l.printlist()
l.delete(555)
l.printlist()
l.insert(555)
l.printlist()
