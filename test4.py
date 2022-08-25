filename = input("enter the file name \n")
input_File = open(filename,"r")
line = input_File.readline()
list = []
string = input("enter your string ")
empty_str = ""
while line!= empty_str:
    if string in line:
        list.append(line)
    line = input_File.readline()
input_File.close()
print(list)