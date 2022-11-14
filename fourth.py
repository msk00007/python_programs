try:
    mystring = input("Enter your string : ")
    filename = open(input("enter filename : "),"r")
    mylist = filename.readlines()
    for each in mylist:
        if mystring in each:
            print(each.strip("\n"))
except FileNotFoundError:
    print("file is not found")
finally:
    if filename:
        print("file is closed")
        filename.close()
