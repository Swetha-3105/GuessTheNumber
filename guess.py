import tkinter as tk 
from tkinter import *
import random
m=tk.Tk()
m.configure(bg="pink")
num=random.randint(0,100)
#print(num)
m.title("Guess The Number!!!")
cus1 = ("Helvetica", 20, "bold italic")
cus2 = ("Helvetica", 16, "italic")
cus3 = ("Helvetica", 10, "bold italic")
cus4=("Calibri",15)
rc=("Times New Roman", 15,"italic")
li=("Comic Sans MS",15,"italic")
lh=("georgia",18,"italic")
co=("Consolas",20,"bold italic")
m.minsize(width=1200,height=1200)
#m.minsize(width=500,height=500)

def check():
    
    global count
    i=e1.get("1.0","end-1c")
    life=tk.Label(m,text=f"Life : {count}",bg="red",fg="white",font=cus1)
    life.place(x=910,y=199)
    if not i.isdigit():
        count=0
        life=tk.Label(m,text=f"life : {count}",bg="red",fg="white",font=cus1)
        life.place(x=910,y=199)
        rl1=tk.Label(m,text="ITS NOT A NUMBER ",bg="pink",fg="red",font=cus3)
        rl1.place(x=350,y=230)  
    else:
        i=int(i)  
        if i>100:
        
            count=0
            rl1=tk.Label(m,text="YOU ARE BEYOND THE LIMIT",bg="pink",fg="red",font=cus3)
            rl1.place(x=350,y=230) 
            life=tk.Label(m,text=f"Life : {count}",bg="red",fg="white",font=cus1)
            life.place(x=910,y=199)
        else:
            count-=1
            life=tk.Label(m,text=f"Life : {count}",bg="red",fg="white",font=cus1)
            life.place(x=910,y=199)
        
            i=int(i)
            if i==num:
                cong=tk.Label(m,text="Congratulations !",bg="pink",fg="dark magenta",font=co)
                cong.place(x=830,y=450)
                win=tk.Label(m,text="You Won !!!",bg="pink",fg="dark magenta",font=co)
                win.place(x=950,y=500)
                il2=tk.Label(m,image=img2,bg="pink")
                il2.place(x=260,y=350)
                il3=tk.Label(m,image=img5,bg="pink")
                il3.place(x=800,y=100)
                rl3=tk.Label(m,text="CORRECT !",bg="pink",fg="green",font=li)
                rl3.place(x=380,y=470) 
            
            
            elif i <num:
            
                rl4=tk.Label(m,text="It's Low",bg="pink",fg="blue",font=lh)
                rl4.place(x=400,y=350) 
            elif i > num:
                rl5=tk.Label(m,text="It's high",bg="pink",fg="blue",font=lh)
                rl5.place(x=400,y=350)
    if count ==0 :
        cong=tk.Label(m,text="Better Luck",bg="pink",fg="dark magenta",font=co)
        cong.place(x=830,y=450)
        win=tk.Label(m,text="Next Time :(",bg="pink",fg="dark magenta",font=co)
        win.place(x=950,y=500)
        il3=tk.Label(m,image=img4,bg="pink")
        il3.place(x=800,y=100)
        ans=tk.Label(m,text=f"It's {num} ",bg="pink",fg="blue",font=li)
        ans.place(x=500,y=280)
        il2=tk.Label(m,image=img3,bg="pink")
        il2.place(x=280,y=330)
            
        b.config(state="disabled")


count=7


l1=tk.Label(m,text="Welcome !",bg="pink",fg="black",font=cus1)
l1.place(x=550,y=20)
l2=tk.Label(m,text="Guess The Number !!!",fg="black",bg="pink",font=cus2)
l2.place(x=510,y=70)
l3=tk.Label(m,text="Enter Number : ",bg="pink",fg="black",font=cus2)
l3.place(x=150,y=150)
e1=tk.Text(m,width=30,height=1,bd=3,font=cus4)
e1.place(x=320,y=150)

l4=tk.Label(m,text="NOTE : ENTER ONLY NUMBER FROM 0 TO 100", bg="pink",fg="red",font=cus3)
l4.place(x=320,y=200)
b=tk.Button(m,text="Check!",bg="black",fg="white",font=cus2,command=check)
b.place(x=400,y=280)

img=PhotoImage(file="C:\\Users\\Technopark Computers\\Desktop\\guessgame\\heart5.png")
il=tk.Label(m,image=img,bg="pink")
il.place(x=800,y=100)
life=tk.Label(m,text=f"Life : {count}",bg="red",fg="white",font=cus1)
life.place(x=910,y=199)
img2=PhotoImage(file="C:\\Users\\Technopark Computers\\Desktop\\guessgame\\bla3.png")
img3=PhotoImage(file="C:\\Users\\Technopark Computers\\Desktop\\guessgame\\lose1.png")
img4=PhotoImage(file="C:\\Users\\Technopark Computers\\Desktop\\guessgame\\break2.png")
img5=PhotoImage(file="C:\\Users\\Technopark Computers\\Desktop\\guessgame\\winner2.png")
m.mainloop()