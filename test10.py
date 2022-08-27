def Bsort(l):
    print("bubblesort is invoked.....")
    n=len(l)
    for i in range(n-1):
         for j in range(n-1-i):
             if(l[j]>l[j+1]):
                l[j],l[j+1]=l[j+1],l[j]

list=[]
n=int(input("Enter the range of the list \n"))
print("enter the elements")
for i in range(n):
    list.append(int(input()))
print(list)
Bsort(list)
print("the sorted list is : ",list)