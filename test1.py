list = []
for i in range(3):
    l=[]
    l.append(input("enter the name  \n"))
    l.append(int(input("enter the age \n")))
    list.append(l)
def takeSecond(elem):
    return elem[1]
list.sort(key = takeSecond)
print(list)