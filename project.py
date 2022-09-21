from cProfile import label
from tkinter import *
def flames():
    S1 = list(boy_name.get())
    S2 = list(girl_name.get())
    if ' ' in S1:
        S1.remove(' ')
    if ' ' in S2:
        S2.remove(' ')
    l1 = len(S1)
    i=0
    for j in range(l1):
        if S1[i] in S2:
            S2.remove(S1[i])
            S1.remove(S1[i])
        else:
            i+=1
            if i==len(S1):
                break 
    l = len(S1)+len(S2)
    flm = ['f','l','a','m','e','s']
    rem = len(flm)
    print(l)
    print(rem)
    while rem !=1:
        remelem = ((l%rem)-1)%rem
        if remelem != rem-1 and remelem != 0:
            for i in range(remelem):
                flm.append(flm[i])
            for i in range(remelem+1):
                flm.pop(0)
        else:
            flm.pop(remelem)
        rem = len(flm)
    if flm[0]=='a':
        label.config(text="Wow..."+boy_name.get()+" and "+girl_name.get()+" are in attraction")
    elif flm[0]=='f':
        label.config(text="Oops..."+boy_name.get()+" and "+girl_name.get()+" are just friends")
    elif flm[0]=='l':
        label.config(text="Hurray..."+boy_name.get()+" and "+girl_name.get()+" are in love")
    elif flm[0]=='m':
        label.config(text="Holymoly..."+boy_name.get()+" and "+girl_name.get()+" will mary each other")
    elif flm[0]=='e':
        label.config(text="Unfortunately..."+boy_name.get()+" and "+girl_name.get()+" will remain as enemies")
    else:
        label.config(text="OMG..."+boy_name.get()+" and "+girl_name.get()+" are like brother and sister")

    
window = Tk()
window.title("FLAMES")
window.configure(background="light pink")
window.geometry("750x450")
boy_name = StringVar()
girl_name = StringVar()
l1 = Label(window,text ="enter the boy name..",bg="light blue").grid(row=0,column=0)
e1 = Entry(window,textvariable=boy_name ,bg="light grey",bd=5).grid(row=0,column=1)
l2 = Label(window,text ="enter the girl name..",bg="light blue").grid(row=1,column=0)
e2 = Entry(window,textvariable=girl_name ,bg="light grey",bd=5).grid(row=1,column=1)
b1 = Button(window,text="flamify",command=flames,bg="light yellow").grid(row=2,column=1)
label=Label(window, text="Loading..", bg="light pink",font=('Calibri 14'))
label.grid(row=6,column=3)
window.mainloop()
