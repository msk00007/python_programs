import sys
try:
    try:
        inputfile = open(sys.argv[1],"r")
    except:
        print("Error accured while opening the file..")
        exit()
    inputfile.seek(int(sys.argv[2]))
    print(inputfile.read())
except:
    print("Errors accured for location...")
