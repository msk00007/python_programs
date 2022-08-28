import sys
def copyfile(file1,file2):
    inputfile=open(file1,"r")
    outputfile = open(file2,"w")
    line = inputfile.read()
    outputfile.write(line)
    inputfile.close()
    outputfile.close()
    outputfile = open(file2,"r")
    print(outputfile.read())

f1 = "test1.txt"
f2 = "copyfile.txt"
copyfile(sys.argv[1],sys.argv[2])

