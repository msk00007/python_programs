N = int(input())
M = int(input())
b = []
ch = []
for i in range(N):
    b.append(int(input()))
    
for i in range(N):
    ch.append(int(input()))
c =0
for each in b:
    c+=each
if c<=M:
    print("0")
else:
    ch.sort()
    i=N-1
    while M>0 and i>=0:
        if b[i]>=M:
            b[i]=b[i]-M
            M=0
        elif b[i]<M:
            M=M-b[i]
            b[i]=0
            i=i-1
    chcount=[]  
    for i in range(N):
            chcount.append(b[i]*ch[i])
    print(max(chcount))

