def fibonaci(element):
    if element == 1:
        t1 = 0
        print(t1)
    else:
        t1 = 0
        t2 = 1
        for i in range(element):
            print(t1,end =" ")
            temp = t2
            t2 = t2+t1
            t1 = temp
fibonaci(5)

    