def binary_search(l,lb,ub,key):
    if(lb<=ub):
        mid = (lb+ub)//2
        if(l[mid]==key):
            return mid
        if(key<l[mid]):
            return binary_search(l,lb,mid-1,key)
        if(key>l[mid]):
            return binary_search(l,mid+1,ub,key)
    else:
        return -1

list = []
N = int(input("enter the range.\n"))
if(N<=0):
    print("enter valid range")
    exit()
for i in range(N):
    list.append(int(input("enter the element...")))
key = int(input("\n enter key to search.."))
result = binary_search(list,0,N-1,key)
if result != -1:
    print("the key is present at index = ",result)
else:
    print("\n element is not found")
