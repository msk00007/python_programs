class stack:
    def __init__(self):
        self.list = []
    def push(self,element):
        self.list.append(element)
    def pop (self):
        self.list.pop()
    def revdisplay(self):
        print("in reverse order.....")
        for each in self.list[::-1]:
            print(each,end=" ")
        print()
    def display(self):
        for each in self.list[::]:
            print(each, end = " ")
        print()
s = stack()
print("enter the no of your string(s)")
n = int(input())
if(n<0):
    print("enter valid positive num above zero")
    exit()
for i in range(n):
    s.push(input("enter your string : "))
s.revdisplay()
s.display()
