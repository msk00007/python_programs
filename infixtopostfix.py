s=[]
s.append("(")
infix = input("Enter your infix expression : ")
infix = infix+")#"
length = len(infix)
postfix=""
def inf(ns):
    indict = {'+':1,"-":1,"*":3,"/":3,"^":6,"(":9,")":0}
    if ns in indict.keys():
        return indict[ns]
    else:
        return 7
def stk(ns):
    stkdict = {'+':2,"-":2 ,"*":4,"/":4,"^":5,"(":0,")":0}
    if ns in stkdict.keys():
        return stkdict[ns]
    else:
        return 8
for i in infix:
    if i == "#":
        break
    while inf(i)<stk(s[-1]):
        postfix = postfix+s.pop()
    if inf(i)>stk(s[-1]):
        s.append(i)
    else:
        s.pop()
# print(infix)
if len(s)==0:
    print(postfix)
else:
    print("wrong infix given")

