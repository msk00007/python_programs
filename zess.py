str1="hiiihe"
str2="hiiiee"
l1 = len(str1)
l2 = len(str2)
count = 0
if l1>l2:
    temp = str1
    str1=str2
    str2=temp
for each in str1:
    if each in str2:
        f = str2.find(each)
        str2 = str2[0:f]+str2[f+1:]
        count+=1
    else:
        print("False")
        break
if count == len(str1):
    print("True")
