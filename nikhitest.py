Array=[]
n=int(input())
for i in range(n):
    a=int(input())
    Array.append(a)
# =================
# for i in range(n//2):
#     if(Array[i]==Array[i+1]-1):
count = 0
# Array.sort()
if(n%2==0):
    x=int(Array[n//2])
    temp=x
    Array[(n//2)-1]=x
    i=int(1)
    while(((n//2)-1)-i!=-1):
        if(Array[((n//2)-1)-i]==x-1):
            x=x-1
            i=i+1
            continue
        Array[((n//2)-1)-i]=x-1
        x=x-1
        i=i+1
        count=count+1
    j=int(1)
    while(((n//2))+j!=len(Array)):
        if(Array[((n//2)+j)]==temp-1):
            temp=temp-1
            j=j+1
            continue
  
        Array[((n//2)+j)]=temp-1
        temp=temp-1
        j=j+1
        count=count+1

elif(int(n%2)==1):
    temp=int(Array[n//2])
    temp1=temp
    i=int(1)
    while((n//2)-i!=-1):
        if(Array[((n//2)-i)]==temp-1):
            temp=temp-1
            i=i+1
            continue
        Array[((n//2)-i)]=temp-1
        temp=temp-1
        i=i+1
        count=count+1
    j=int(1)
    while((n//2)+j!=len(Array)):
        if(Array[((n//2)+j)]==temp1-1):
            temp1=temp1-1
            j=j+1
            continue
        Array[((n//2)+j)]=temp1-1

        count=count+1
print(count)
print("array =", Array)

