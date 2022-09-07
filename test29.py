import sys
try:
    file = sys.argv[1]
    location = int(sys.argv[2])
except:
    print("Error accured give correct arguments..")
    exit()
try:
    inputfile = open(file,"r")
except:
    print("Error occured while opening the file ")
    exit()
try:
    inputfile.seek(location)
    print(inputfile.read())
except:
    print("Errors accured for location...")
