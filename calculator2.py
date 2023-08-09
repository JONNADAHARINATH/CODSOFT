from tkinter import *
hs=Tk()
hs.title("calculator")
hs.geometry("361x410+500+200")
hs.configure(bg="#7f8274")
hs.resizable(0,0)
val=""
data=StringVar()
display=Entry(hs,text=data,bd=29,justify="right",bg="white",font=("arial",20))
display.grid(row=0,columnspan=4)


def button_click(num):
    global val
    val=val+str(num)
    data.set(val)
    
def button_clear():
    global val
    val=""
    data.set("")
    
def button_Equals():
    global val
    result=str(eval(val))
    data.set(result)
    


b_c=Button(hs,text="C",font=("arial",12,"bold"),bd=6,height=2,width=6,command=button_clear)
b_c.grid(row=1,column=0)

b_s=Button(hs,text="%",font=("arial",12,"bold"),bd=6,height=2,width=6,command=lambda: button_click("%"))
b_s.grid(row=1,column=1)

b_d=Button(hs,text="/",font=("arial",12,"bold"),bd=6,height=2,width=6,command=lambda: button_click("/"))
b_d.grid(row=1,column=2)

b_m=Button(hs,text="*",font=("arial",12,"bold"),bd=6,height=2,width=6,command=lambda: button_click("*"))
b_m.grid(row=1,column=3)




b_7=Button(hs,text="7",font=("arial",12,"bold"),bd=6,height=2,width=6,command=lambda: button_click(7))
b_7.grid(row=2,column=0)

b_8=Button(hs,text="8",font=("arial",12,"bold"),bd=6,height=2,width=6,command=lambda: button_click(8))
b_8.grid(row=2,column=1)

b_9=Button(hs,text="9",font=("arial",12,"bold"),bd=6,height=2,width=6,command=lambda: button_click(9))
b_9.grid(row=2,column=2)


b_s=Button(hs,text="-",font=("arial",12,"bold"),bd=6,height=2,width=6,command=lambda: button_click('-'))
b_s.grid(row=2,column=3)




b_4=Button(hs,text="4",font=("arial",12,"bold"),bd=6,height=2,width=6,command=lambda: button_click(4))
b_4.grid(row=3,column=0)

b_5=Button(hs,text="5",font=("arial",12,"bold"),bd=6,height=2,width=6,command=lambda: button_click(5))
b_5.grid(row=3,column=1)

b_6=Button(hs,text="6",font=("arial",12,"bold"),bd=6,height=2,width=6,command=lambda: button_click(6))
b_6.grid(row=3,column=2)


b_a=Button(hs,text="+",font=("arial",12,"bold"),bd=6,height=2,width=6,command=lambda: button_click('+'))
b_a.grid(row=3,column=3)




b_1=Button(hs,text="1",font=("arial",12,"bold"),bd=6,height=2,width=6,command=lambda: button_click(1))
b_1.grid(row=4,column=0)

b_2=Button(hs,text="2",font=("arial",12,"bold"),bd=6,height=2,width=6,command=lambda: button_click(2))
b_2.grid(row=4,column=1)

b_3=Button(hs,text="3",font=("arial",12,"bold"),bd=6,height=2,width=6,command=lambda: button_click(3))
b_3.grid(row=4,column=2)

b_do=Button(hs,text=".",font=("arial",12,"bold"),bd=6,height=2,width=6,command=lambda: button_click("."))
b_do.grid(row=4,column=3)




b_bracket1=Button(hs,text="(",font=("arial",12,"bold"),bd=6,height=2,width=6,command=lambda: button_click("("))
b_bracket1.grid(row=5,column=0)

b_bracket2=Button(hs,text=")",font=("arial",12,"bold"),bd=6,height=2,width=6,command=lambda: button_click(")"))
b_bracket2.grid(row=5,column=1)

b_z=Button(hs,text="0",font=("arial",12,"bold"),bd=6,height=2,width=6,command=lambda: button_click(0))
b_z.grid(row=5,column=2)

b_e=Button(hs,text="=",font=("arial",12,"bold"),bd=6,height=2,width=6,command=button_Equals)
b_e.grid(row=5,column=3)
hs.mainloop()