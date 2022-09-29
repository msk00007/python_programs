
from tkinter import*
var=Tk()
var.geometry("300x390")
var.minsize(300,390)
var.maxsize(320,390)
Label(var,text="Calculator",bg="black",fg="white",font= ("conicasansms",14,"bold"),borderwidth=10,relief= SUNKEN).pack(side = TOP,fill=X)
frame = Frame(var,bg = "light blue",borderwidth=10,relief=SUNKEN)
frame2 = Frame(var,bg = "light blue")
frame2.pack(anchor=NW,fill=X)
frame.pack(side=TOP)
def one():
    t.insert(END,'1')
def two():
    t.insert(END,'2')
def three():
    t.insert(END,'3')
def four():
    t.insert(END,'4')
def five():
    t.insert(END,'5')
def six():
    t.insert(END,'6')
def seven():
    t.insert(END,'7')
def eight():
    t.insert(END,'8')
def nine():
    t.insert(END,'9')
def zero():
    t.insert(END,'0')
def clear():
    t.delete("1.0", "end-1c")
def delete():
    t.delete("end-2c","end-1c")
def plus():
    t.insert(END,"+")
def minus():
    t.insert(END,"-")
def multi():
    if(t.get(END)!='+'): 
        t.insert(END,'*')
def devide():
    t.insert(END,"/")
def power():
    final = int(t.get("1.0","end-1c"))
    res = final*final
    clear()
    res = str(res)
    t.insert(0.0,res)
def result():
    final = t.get("1.0","end-1c")
    res = eval(final)
    # clear()
    t.insert(END,"=")
    t.insert(END,res)

t = Text(frame2,bg="light green",font="Courior 14 bold",width=15,height=3,borderwidth=3,relief=SUNKEN)
b1 = Button(frame,text = "1",bg="blue",fg="white",width=5,height=5,command=one,borderwidth=3,relief=SUNKEN)
b2 = Button(frame,text = "2",bg="blue",fg="white",width=5,height=5,command=two,borderwidth=3,relief=SUNKEN)
b3 = Button(frame,text = "3",bg="blue",fg="white",width=5,height=5,command=three,borderwidth=3,relief=SUNKEN)
b4 = Button(frame,text = "4",bg="blue",fg="white",width=5,height=5,command=four,borderwidth=3,relief=SUNKEN)
b5 = Button(frame,text = "5",bg="blue",fg="white",width=5,height=5,command=five,borderwidth=3,relief=SUNKEN)
b6 = Button(frame,text = "6",bg="blue",fg="white",width=5,height=5,command=six,borderwidth=3,relief=SUNKEN)
b7 = Button(frame,text = "7",bg="blue",fg="white",width=5,height=5,command=seven,borderwidth=3,relief=SUNKEN)
b8 = Button(frame,text = "8",bg="blue",fg="white",width=5,height=5,command=eight,borderwidth=3,relief=SUNKEN)
b9 = Button(frame,text = "9",bg="blue",fg="white",width=5,height=5,command=nine,borderwidth=3,relief=SUNKEN)
b0 = Button(frame,text = "0",bg="blue",fg="white",width=5,height=5,command=zero,borderwidth=3,relief=SUNKEN)
Button(frame,text = "CL",bg="blue",fg="white",width=5,height=5,command=clear,borderwidth=3,relief=SUNKEN).grid(row=1,column=4)
Button(frame,text = "DEL",bg="blue",fg="white",width=5,height=5,command=delete,borderwidth=3,relief=SUNKEN).grid(row=1,column=6)
Button(frame,text = "+",bg="blue",fg="white",width=5,height=5,command=plus,borderwidth=3,relief=SUNKEN).grid(row=2,column=4)
Button(frame,text = "-",bg="blue",fg="white",width=5,height=5,command=minus,borderwidth=3,relief=SUNKEN).grid(row=2,column=5)
Button(frame,text = "*",bg="blue",fg="white",width=5,height=5,command=multi,borderwidth=3,relief=SUNKEN).grid(row=2,column=6)
Button(frame,text = "/",bg="blue",fg="white",width=5,height=5,command=devide,borderwidth=3,relief=SUNKEN).grid(row=3,column=4)
Button(frame,text = "x^2",bg="blue",fg="white",width=5,height=5,command=power,borderwidth=3,relief=SUNKEN).grid(row=3,column=5)
Button(frame,text = "=",bg="blue",fg="white",width=5,height=5,command=result,borderwidth=3,relief=SUNKEN).grid(row=3,column=6)
t.pack(fill=X)
b1.grid(row=1,column=1)
b2.grid(row=1,column=2)
b3.grid(row=1,column=3)
b4.grid(row=2,column=1)
b5.grid(row=2,column=2)
b6.grid(row=2,column=3)
b7.grid(row=3,column=1)
b8.grid(row=3,column=2)
b9.grid(row=3,column=3)
b0.grid(row=1,column=5)
var.mainloop()
