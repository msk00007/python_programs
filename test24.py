from math import sqrt
def isprime(num):
    flag = True
    if num == 2:
        return flag 
    newrange = int(sqrt(num))
    for i in range(2,newrange+1):
        if int(num) % i == 0:
            flag = False
            break
    return flag
N = int(input("enter the number \n"))
if N>=2:
    for i in range(2,N):
        result = isprime(i)
        if result :
            print(i, end = " ")
else:
    print("not a prime number")
