from tkinter import*
from tkinter import font
from tkmacosx import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
from typing import Collection
import mysql.connector

conn=mysql.connector.connect(username='root',password='password',host='localhost',database='Mydata')
my_cursor=conn.cursor()
w=Tk()
w.geometry('600x800')
w.title(' L O G I N ')
w.resizable(0,0)


#Making gradient frame
j=0
r=10
for i in range(100):
    c=str(222222+r)
    Frame(w,width=20,height=1000,bg="#"+c).place(x=j,y=0)   
    j=j+10                                                  
    r=r+1

Frame(w,width=500,height=700,bg='white').place(x=50,y=50)


l1=Label(w,text='Username',bg='white')
l=('Consolas',20)
l1.config(font=l)
l1.place(x=100,y=400)


#e1 entry for username entry
e1=Entry(w,width=20,border=0)
l=('Consolas',20)
e1.config(font=l,width=28)
e1.place(x=100,y=430)

l2=Label(w,text='Password',bg='white')
l=('Consolas',20)
l2.config(font=l)
l2.place(x=100,y=480)

#e2 entry for password entry
e2=Entry(w,width=20,border=0,show='*')
e2.config(font=l,width=28)
e2.place(x=100,y=510)


###lineframe on entry

Frame(w,width=370,height=2,bg='#141414').place(x=100,y=460)
Frame(w,width=370,height=2,bg='#141414').place(x=100,y=540)

from PIL import ImageTk,Image



imagea=Image.open("admin.jpg")
imageb= ImageTk.PhotoImage(imagea)

label1 = Label(image=imageb,
               border=0,
               
               justify=CENTER)


label1.place(x=185, y=100)


#Command
def cmd():
    if e1.get()=='admin' and e2.get()=='password':
        messagebox.showinfo("LOGIN SUCCESSFULLY", "         W E L C O M E        ")
        w.destroy()
        import voterId
        voterId.root.mainloop()
        
    else:
        messagebox.showwarning("LOGIN FAILED","        PLEASE TRY AGAIN        ")


#Button_with hover effect
def bttn(x,y,text,ecolor,lcolor):
    def on_entera(e):
        myButton1['background'] = ecolor #ffcc66
        myButton1['foreground']= lcolor  #000d33

    def on_leavea(e):
        myButton1['background'] = lcolor
        myButton1['foreground']= ecolor

    myButton1 = Button(w,text=text,
                   width=120,
                   height=40,
                   fg=ecolor,
                   border=0,
                   bg=lcolor,
                   activeforeground=lcolor,
                   activebackground=ecolor,
                       command=cmd)
                  
    myButton1.bind("<Enter>", on_entera)
    myButton1.bind("<Leave>", on_leavea)

    myButton1.place(x=x,y=y)


bttn(220,600,'L O G I N','white','#994422')


w.mainloop()


