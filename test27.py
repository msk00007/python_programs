filename = input("enter the file name \n")
input_File = open(filename,"r")
line = input_File.readline()
List = {}
empty_str = ""
while line!= empty_str:
    for each in line.strip("\n").split(" "):
        if each in List:
            List[each]=List.get(each)+1
        else:
            List[each]=1
    line = input_File.readline()
input_File.close()
for i in List:
    print(i,'--> and count is ',List[i])

