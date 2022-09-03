def bubble_sort(l,lb,ub):
    if(lb<ub):
        for i in range(ub):
            for j in range(0,ub-i):
                if l[j]>l[j+1]:
                    l[j],l[j+1]=l[j+1],l[j]
list = []
n=int(input("enter the range: \n"))
for i in range(n):
    list.append(input("enter the name.."))
bubble_sort(list,0,n-1)
print(list)
