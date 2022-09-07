class node:
    def __init__(self,element):
        self.data = element
        self.next = None
class stacklinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
    def push(self,elem):
        new_node = node(elem)
        
        if(self head == None):
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
    def pop(self):
        if self.head == None:
            print("list is empty cannot pop")
        else:
            if self.head.next == None :
                self.head = self.head.next
                popelem = self.tail.data
                self.tail = self.head
                return popelem 
            else:
                itr = self.head
                while itr.next != self.tail:
                    itr = itr.next
                popelem = self.tail.data
                itr.next = None
                self.tail = itr
                return popelem 
    def isEmpty(self):
        if self.head is None:
            return True
        return False
    def peek(self):
        if self.tail != None:
            print(self.tail.data)
        else:
            print("Stack is empty")
   
    def stackprint(start):
        if start == None:
            return
        stacklinkedlist.stackprint(start.next)
        print(start.data,end = " ")

    def display(self):
        if self.head == None:
            print("stack is empty cannot print")
        else:
            stacklinkedlist.stackprint(self.head)
            print()

Stack = stacklinkedlist()
print(Stack.isEmpty())
Stack.push(4)
Stack.push(45)
Stack.push(456)
Stack.display()
Stack.pop()
Stack.push(4567)
Stack.display()


                
