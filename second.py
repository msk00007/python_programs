try:
    filename = open(input("enter filename : "),"r")
    mylist = filename.readlines()
    print(mylist)
    mylist.sort()
    for each in mylist:
        print(each.strip("\n"))
except FileNotFoundError:
    print("file is not found")
finally:
    if filename:
        filename.close()
    print("you reached to finally clause")