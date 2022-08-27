from email import header


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

l = linkedlist()
l.insert(5)
l.insert(55)
l.insert(555)
itr = l.head
while itr is not None:
    print(itr.data, end = " ")
    itr = itr.Next
