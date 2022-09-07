try:
    filename = input("enter the file name \n")
    input_File = open(filename,"r")
except:
    print("file not found error try again and give correct input.")
    exit()
line = input_File.readline()
list = []
empty_str = ""
while line!= empty_str:
    list.append(line.strip('\n'))
    line = input_File.readline()
input_File.close()
print(list)
