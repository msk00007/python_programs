def Bsearch(l,lb,ub,key):
    if lb<=ub:
        mid = (lb+ub)//2
        if l[mid]==key:
            return mid
        elif key<l[mid]:
            for i in range(lb,mid):
                if l[i]==key:
                    return i
        elif key>l[mid]:
            for i in range(mid+1,ub+1):
                if l[i]==key:
                    return i
    return -1
list=[]
n=int(input("Enter the range of the list \n"))
if n<=0:
    print("enter valid range..")
    exit()
print("enter the elements")
for i in range(n):
    list.append(int(input()))
key = int(input("Enter the key to search..\n"))
result = Bsearch(list,0,n-1,key)
if result != -1:
    print("key value is find at index : ",result)
else:
    print("key value is not found...")
