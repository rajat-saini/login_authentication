from tkinter import *
import tkinter.messagebox
import pymysql

root=Tk()
root.title("Check Username/Password")
root.geometry("400x150+200+200")
root.resizable(0,0)

u_name=StringVar()
passwd=StringVar()

def check():
    u=u_name.get()
    p=passwd.get()

    con=pymysql.connect("localhost","root","rajat@123","homework")
    cur=con.cursor()

    query="select * from auth"
    cur.execute(query)

    data=cur.fetchall()
    print (data)
    flag=0

    for i in data:
        if(u==i[0] and p==i[1]):
            tkinter.messagebox.showinfo(title="Message", message="Login Confirmed")
            #Label(root, text="Login Confirmed", font=20).place(x=80,y=85)
            flag=1
            break
        else:
            continue

    if(flag==0):

         tkinter.messagebox.showerror(title="Warning!", message="Incorrect username or password")
        # Label(root,text="Login Failed. Incorrect username or password", font=20).place(x=60, y=85)
    con.commit()
    con.close()

l1=Label(text = "Enter username", font=20).grid(row=0, column=0)
l2=Label(text = "Enter password", font=20).grid(row=1, column=0)
e1=Entry(textvariable = u_name,font=20)
e1.grid(row=0,column=1)
e2=Entry(textvariable=passwd, font=20,show='*')
e2.grid(row=1,column=1)
b=Button(text="LOGIN",bg="yellow",command=check, width=15)
b.place(x=110, y=55)
root.mainloop()