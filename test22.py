import sys
def copyfile(file1,file2):
    try:
        inputfile=open(file1,"r")
        outputfile = open(file2,"w")
        line = inputfile.read()
        outputfile.write(line)
        inputfile.close()
        outputfile.close()
        print("data copied successfully")
    except:
        print("error accured while opening the source file")
try:
    copyfile(sys.argv[1],sys.argv[2])
except:
    print("Error accured while giving input pls run again and give correct input and parameters..")

