def match(str1,str2):
    count1 = [0]*26
    count2 =[0]*26
    i=0
    while i<len(str1):
        count1[ord(str1[i])-ord("a")]+=1
        i+=1
    i=0
    while i<len(str2):
        count2[ord(str2[i])-ord("a")]+=1
        i+=1
    result = 0
    for i in range(26):
        if count1[i]<count2[i]:
            result = -1
            break
        else:
            result += (count1[i]-count2[i])
    return result
strarr=[]
arr=[]
strarr.append(input("Enter string : "))
strarr.append(input("Enter long string : "))
for each in strarr[1].split(","):
    arr.append(match(strarr[0],each))
l = len(arr)
j=0
for i in range(l):
    if arr[j]== -1:
        arr.pop(j)
    else:
        j+=1
if len(arr)==0:
    print("-1")
else:
    print(min(arr))
