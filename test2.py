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
# another method:
# use the above try block here also....
filename = input("Enter the file name\n")
file = open(filename,"r")
list = file.readlines()
list.sort()
for i in list:
    print(i.strip("\n"))


# second method....
# with open(filename) as file1:
#     list = file1.readlines()
#     list.sort()
#     for each in list:
#         print(each.strip())
