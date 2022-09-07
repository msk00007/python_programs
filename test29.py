import sys
try:
    file = sys.argv[1]
    location = sys.argv[2]
except:
    print("Error accured give correct arguments..")
    exit()
try:
    inputfile = open(sys.argv[1],"r")
except:
    print("Error occured while opening the file ")
    exit()
try:
    inputfile.seek(int(sys.argv[2]))
    print(inputfile.read())
except:
    print("Errors accured for location...")
