def Bsort(l):
    print("bubblesort is invoked.....")
    n=len(l)
    for i in range(n-1):
         for j in range(n-1-i):
             if(l[j]>l[j+1]):
                l[j],l[j+1]=l[j+1],l[j]

def Ssort(l):
    print("selection sort is invoked.....")
    n=len(l)
    print(n)
    for i in range(n-1):
        min = i
        for j in range(i+1,n):
            if(l[min]>l[j]):
                 min=j
        if(l[i]!=l[min]):
            l[min],l[i]=l[i],l[min]
        print(l)


def insertion(l):
    print("insertion sort is invoked.......")
    n=len(l)
    for i in range(1,n):
        temp=l[i]
        j=i-1
        while (j>=0) and (l[j]>temp):
            l[j+1]=l[j]
            j=j-1
        l[j+1]=temp



def partition(l,lb,ub):
    i=lb;
    j=ub;
    pivot=l[lb]
    while(i<j):
        while(i<=ub and l[i]<=pivot):
            i=i+1
        while(j>lb and l[j]>pivot):
            j=j-1
        if(i<j):
            t=l[i]
            l[i]=l[j]
            l[j]=t
    l[lb]=l[j]
    l[j]=pivot
    return j


def quicks(a,lb,ub):
    if(lb<ub):
        pos = partition(a,lb,ub)
        quicks(a,lb,pos)
        quicks(a,pos+1,ub)



def msort(a,lb,mid,ub):
    if(lb<ub):
        n=(ub-lb+1)
    m=[0]*n
    i=lb
    j=mid+1
    k=0
    p=lb
    while(i<=mid and j<=ub):
        if(a[i]<a[j]):
            m[k]=a[i]
            i=i+1
            k=k+1
        else:
            m[k]=a[j]
            j=j+1
            k=k+1
    while(i<=mid):
        m[k]=a[i]
        k=k+1
        i=i+1
    while(j<=ub):
        m[k]=a[j]
        k=k+1
        j=j+1
    print(m)
    for i in range(n):
        a[p]=m[i]
        p=p+1
    
     



def merge(a, lb, ub):
    if(lb<ub):
        mid = (lb+ub)//2
        merge(a,lb,mid)
        merge(a,mid+1,ub)
        msort(a,lb,mid,ub)
 
x=[]
print("enter the number of elements")
y=int(input())
print("enter the elements")
for i in range(y):
    a=int(input())
    x.append(a)
print("*****************************************")
flag=True
while flag:

    print("select the sorting method : 1-->bubbleSort...2-->selectionSort.....3-->insertionSort.....4-->quicksort....5-->mergesort..0-->exit ")
    b=int(input())
    if(b==1):
        Bsort(x)
        print(x)
    elif(b==2):
        Ssort(x)
        print(x)
    elif(b==3):
        insertion(x)
        print(x)
    elif(b==4):
        quicks(x,0,y-1)
        print("quick sort is invoked........")
        print(x)
    elif(b==5):
        merge(x,0,int(len(x)-1))
        print("merge sort is invoked........")
        print(x)
    elif(b==0):
        flag=False
        
    else:
        print("invalid selection.............")
