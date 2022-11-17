arr=[]
for i in range(5):
    arr.append(int(input("enter: ")))
l = len(arr)
s=0
count = 1
for i in range(1,l):
    s=s+arr[i-1]
    if s>arr[i]:
        print("false")
        break
    count+=1
if count == len(arr):
    print("true")

