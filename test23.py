i = int(input("enter the 1st matrix no of rows \n"))
j = int(input("enter the 1st matrix no of columns \n"))
i2 = int(input("enter the 2st matrix no of rows \n"))
j2 = int(input("enter the 2st matrix no of columns \n"))
if (i!=i2) or (j!=j2):
    print("both  matrices should have same dimentions \n")
    exit()
else:
    m1 =[]
    m2 = []

    for n in range(i):
        l = []
        for k in range(j):
            l.append(int(input()))
        m1.insert(i,l)


    for m in range(i):
        for k in range(j):
            print(m1[m][k], end = " ")
    print()
    for n in range(i):
        l = []
        for k in range(j):
            l.append(int(input()))
        m2.append(l)

    for m in range(i):
        for k in range(j):
            print(m2[m][k], end = " ")
    print()
    matrix3 = []
    for m in range(i):
        l = []
        for k in range(j):
            l.append(m1[m][k]+m2[m][k])
        matrix3.append(l)
    del(l)
    for m in range(i):
        for k in range(j):
            print(matrix3[m][k], end = " ")
        


