def Bsearch(l,lb,ub,key):
    while lb<=ub:
        mid = (lb+ub)//2
        if l[mid]==key:
            return mid
        elif key<l[mid]:
            ub = mid-1
        elif key>l[mid]:
            lb = mid+1
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
