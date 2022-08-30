filename = input("enter the file name \n")
input_File = open(filename,"r")
line = input_File.readline()
list = []
empty_str = ""
while line!= empty_str:
    list.append(line.strip('\n'))
    line = input_File.readline()
input_File.close()
list.sort()
print(list)
