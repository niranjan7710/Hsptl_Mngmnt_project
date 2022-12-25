from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector


def loginpage():
        

    #def logintodb(user,passw):
        

        

    root = Tk()
    root.state('zoomed')
    root.title("Login")
    root.geometry("1920x1080+0+0")


    #ico = Image.open('hsptl.jpg')
    #photo = ImageTk.PhotoImage(ico)
    #root.wm_iconphoto(False, photo)

    label_title = Label(root, bd=5, relief =RIDGE, text = "HOSPITAL MANAGEMENT SYSTEM", fg="red",bg="#212121",font = ("akrobat black",50,"bold","underline",))
    label_title.pack(side=TOP,fill=X)


    global entry1
    global entry2

    DataFrame = Frame(root, bd=8,background="#212121", relief =RIDGE)
    DataFrame.place(x=0,y=90,width=1920,height=970)

    lblfrm = LabelFrame(DataFrame,bd=8,relief=RIDGE,padx=10,fg="white",bg="#2b2d42",font = ("akrobat black",16,"bold","underline",),text="Login to your mysql Database")
    lblfrm.place(x=400,y=125,width=1180,height=620)

    Label(lblfrm,bg="#2b2d42",fg="white",text="USERNAME",font = ("akrobat ",20,"bold",),justify=RIGHT,cursor="xterm").place(x=320,y=180)
    entry1 = Entry(lblfrm,font=("cascadia code mono",16,"bold"),bg="#2b2d42",fg="white",bd=5, justify='center')
    entry1.insert(0,"root")
    entry1.place(x=550,y=180,width=290,height=33)

    Label(lblfrm,bg="#2b2d42",fg="white",text="PASSWORD",font = ("akrobat ",20,"bold",),justify=RIGHT,cursor="xterm").place(x=320,y=280)
    entry2 = Entry(lblfrm,font=("cascadia code mono",16,"bold"),bg="#2b2d42",fg="white",bd=5,justify='center',show="*")
    entry2.place(x=550,y=280,width=290,height=33)


    def login():
        user = entry1.get()
        passw = entry2.get()

        con = mysql.connector.connect(
            host="localhost",
            user=user,
            passwd=passw,
        )

    #    if con.is_connected():
    #        messagebox.showinfo("Success", "Successfully connected to MySQL")
    #    else:
    #        messagebox.showinfo("Error", "Incorrect login credentials")
        if con.is_connected():
                messagebox.showinfo("Success", "Welcome to Hospital Management")
        else:
                messagebox.showinfo("Error", "Incorrect login credentials")




    button_login= Button(root,text="login",command=login,height=3,width=13,bd=7,bg="#2b2d42",fg="white",cursor="hand2",activebackground='#2b2d42',activeforeground="white")
    button_login.place(x=950,y=590,width=130,height=53)



    #   if passw == mysql.connector.connect(host="localhost", user="root", passwd="", db="hospital"):        
    #       messagebox.showinfo("Error","login Credentials cannot be empty")
    #
    #   elif passw == mysql.connector.connect(host="localhost", user="root", passwd=passw, db="hospital"):
    #       messagebox.showinfo("Success","login Success")#    
    #  else:
    #        messagebox.showinfo("Error","Incorrect login credentials",)




    root.mainloop()

