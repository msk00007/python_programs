def insertion(l,lb,ub):
    if(lb<=ub):
        for i in range(ub+1):
            temp = l[i]
            j=i-1
            while j>=0 and l[j]>temp:
                l[j+1]=l[j]
                j=j-1
            l[j+1]=temp

list = []
n = int(input("enter the range"))
for i in range(n):
    list.append(int(input()))
insertion(list,0,n-1)
print(list)