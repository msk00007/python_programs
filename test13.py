def selectionSort(l):
    print("selection sort is invoked.....")
    n=len(l)
    for i in range(n-1):
        min = i
        for j in range(i+1,n):
            if(l[min]>l[j]):
                 min=j
        if(l[i]!=l[min]):
            l[min],l[i]=l[i],l[min]
list = []
n = int(input("enter the range"))
for i in range(n):
    list.append(int(input()))
selectionSort(list)
print(list)
