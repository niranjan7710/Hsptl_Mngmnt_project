from tkinter import *
from tkinter import messagebox

root = Tk()
root.state('zoomed')
root.title("Login")
root.geometry("1920x1080+0+0")

label_title = Label(root, bd=5, relief =RIDGE, text = "HOSPITAL MANAGEMENT SYSTEM", fg="red",bg="black",font = ("akrobat black",50,"bold","underline",))
label_title.pack(side=TOP,fill=X)


global entry1
global entry2

DataFrame = Frame(root, bd=8,background="black", relief =RIDGE)
DataFrame.place(x=0,y=90,width=1920,height=970)

lblfrm = LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=10,fg="white",bg="black",font = ("akrobat black",16,"bold","underline",),text="Login to your mysql Database")
lblfrm.place(x=400,y=95,width=1180,height=620)

Label(lblfrm,bg="black",fg="white",text="USERNAME",font = ("akrobat ",20,"bold",),justify=RIGHT,cursor="xterm").place(x=320,y=180)
textBox1 = Entry(lblfrm,font=("cascadia code mono",16,"bold"),bg="black",fg="white",bd=5, justify='center')
textBox1.insert(0,"root")
textBox1.place(x=550,y=180,width=290,height=33)

Label(lblfrm,bg="black",fg="white",text="PASSWORD",font = ("akrobat ",20,"bold",),justify=RIGHT,cursor="xterm").place(x=320,y=280)
textBox2 = Entry(lblfrm,font=("cascadia code mono",16,"bold"),bg="white",fg="black",bd=5,justify='center',show="*")
textBox2.place(x=550,y=280,width=290,height=33)


root.mainloop()

