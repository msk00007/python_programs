s= input("enter the string...\n")
s2=""
for each in s[::-1]:
    s2=s2+each
flag = True
for i in range(len(s)):
    if s[i]!=s2[i]:
        flag = False
if flag:
    print("the given string is palindrome..")
else:
    print("the given string is not a palindrome.")