N = int(input())
M = int(input())
b = []
ch = []
for i in range(N):
    b.append(int(input()))
    
for i in range(N):
    ch.append(int(input()))
b1 = b.copy()
c =0
for each in b:
    c+=each
if c>M:
    x = c-M
    M=0
b.sort()

if b[0] >=x:
    b[0]=b[0]-x
    x=0
else:
    for i in range(N):
        x=x-b[i]
        b[i]=0
print(b)
for each in b:
    if  each<M:
        M=M-each
        each=0
choccount = 0
for i in range(N):
    if b[i]<b1[i]:
        I = b1[i]-b[i]
        choccount = choccount+I*ch[i]
print(choccount)