import sys
try:
    try:
        inputfile = open(sys.argv[1],"r")
        print("the path of the file is ",sys.argv[1])
        print(inputfile.read())
    except:
        print("file is not found kindly give correct path")
    finally:
        inputfile.close()
except:
    print("some error accured while  opening the file..")
finally:
    print("try block is completed")