import sys

inputfile = open(sys.argv[1],"r")
# print("the path of the file is ",sys.argv[1])
N = int(sys.argv[2])
inputfile.read(N)
print(inputfile.read())
inputfile.close()
