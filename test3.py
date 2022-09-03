filename = input("enter the file name..")
input_file = open(filename,"r")
line = input_file.readline()
emptystr = ""
s = ""
charcount = 0
while line!= emptystr:
    for ch in line.strip('\n'):
        charcount+=1
    line = input_file.readline()
print("charcount is : ",charcount)
input_file.close()
input_file = open(filename,"r")
line = input_file.readline()
wordcount = 0
space = " "
linecount = 0;
while line!= emptystr:
    linecount += 1
    for ch in line:
        if ch == space or  ch == '\n':
            wordcount+=1
    line = input_file.readline()
print("wordcount is : ",wordcount)
print("line count is ..",linecount)
