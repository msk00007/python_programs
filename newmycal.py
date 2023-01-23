from datetime import date,datetime
mycal = [["    " for x in range(12)] for x in range(10)]
y = int(input("Enter year : "))
weekdays = {6:"sun ",0:"mon ",1:"tue ",2:"wed ",3:"thu ",4:"fri ",5:"sat "}
months = {1:"jan ",2:"feb ",3:"mar ",4:"apr ",5:"may ",6:"jun ",7:"jul ",8:"aug ",9:"sep ",10:"oct ",11:"nov ",12:"dec "}
start = date(y,1,1)
val = start.weekday()
num = 0;
for i in range(10):
    for j in range(12):
        if i==1 and j == 2:
            mycal[i][j]=y
        elif i>2 and j>4:
            if i==3 and j==5:   
                mycal[i][j]=weekdays.get(val)
            elif i>3 and j ==5:
                val = (val+1)%7
                mycal[i][j] = weekdays.get(val)
            else:
                mycal[i][j]=weekdays.get((val+(j-5))%7)
        elif i>2 and j<=4:
            if j == 0:
                num+=1
                if num <10:
                    mycal[i][j]="0"+str(num)+"  "
            else:
                if num+7*j<32:
                    if num+7*j<10: 
                        mycal[i][j]="0"+str(num+7*j)+"  "
                    else:
                        mycal[i][j]=str(num+7*j)+"  "
for n in range(1,13,1):
    d = date(y,n,1).weekday()
    monthstartday = weekdays.get(d)
    for j in range(5,12):
        if mycal[3][j]==monthstartday:
            k=0
            while mycal[k][j]!="    ":
                k+=1
            mycal[k][j]=months.get(n) 
for i in range(10):
    for j in range(12):
        print(mycal[i][j],end = " ")
    print()
