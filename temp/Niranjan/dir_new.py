from tkinter import *
from tkinter import messagebox
import mysql.connector


#=================================================================Tkinter Window=====================================================================
root = Tk()
root.state('zoomed')
root.title("Hospital Management System")
root.geometry("1920x1080")
#===================================================================================================================================================


def swap(frame):
    frame.tkraise()


F_Home = Frame(root, bd=8, background="#212121", relief=RIDGE)
F_Home.place(x=0, y=0, width=1920, height=1080)


F_login = Frame(root, bd=8,background="#212121", relief =RIDGE)
F_login.place(x=0,y=0,width=1920,height=1080)


#================================================================LOGIN PAGE=========================================================================

label_title = Label(F_login, bd=5, relief =RIDGE, text = "HOSPITAL MANAGEMENT SYSTEM", fg="red",bg="#212121",font = ("akrobat black",50,"bold","underline",))
label_title.pack(side=TOP,fill=X)

global entry1
global entry2



lblfrm = LabelFrame(F_login,bd=8,relief=RIDGE,padx=10,fg="white",bg="#2b2d42",font = ("akrobat black",16,"bold","underline",),text="Login to your mysql Database")
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

    try:
        con = mysql.connector.connect(
            host="localhost",
            user=user,
            passwd=passw,
        )

        if con.is_connected():
            messagebox.showinfo("Success", "Welcome to Hospital Management")
            swap(F_Home)
    except:
        messagebox.showinfo("error","Inavlid Credentials")


button_login= Button(F_login,text="login",command=lambda: login(),height=3,width=13,bd=7,bg="#2b2d42",fg="white",cursor="hand2",activebackground='#2b2d42',activeforeground="white")
button_login.place(x=950,y=590,width=130,height=53)

#================================================================LOGIN PAGE ENDS HERE=======================================================================





#================================================================HOME PAGE===================================================================================


label_title = Label(F_Home, bd=5, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM",
                    fg="red", bg="#212121", font=("akrobat black", 50, "bold", "underline",))
label_title.pack(side=TOP, fill=X)





lblfrm = LabelFrame(F_Home, bd=8, relief=RIDGE, padx=10, fg="white", bg="Black", font=(
    "akrobat black", 16, "bold", "underline",), text="Welcome")
lblfrm.place(x=110, y=15, width=1680, height=920)

Label(lblfrm, bg="Black", fg="white", text="A project by Niranjan S, Hari Prasad, Yasus & Ammu Krishna (2022-23 batch)",
    font=("D3 Euronism Bold", 20,), justify=CENTER, cursor="xterm").place(x=65, y=820)




button_Administration = Button(F_Home, text="Administration", font=("D3 Euronism Bold", 19), height=3,
                            width=13, bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Administration.place(x=750, y=430, width=390, height=53)

button_PatientDetails = Button(F_Home, text="Patient Details", font=("D3 Euronism Bold", 19),  height=3,
                            width=13, bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_PatientDetails.place(x=750, y=530, width=390, height=53)

button_Exit = Button(F_Home, text="Exit",  font=("D3 Euronism Bold", 19), height=3, width=13,
                    bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Exit.place(x=750, y=630, width=390, height=53)







root.mainloop()






'''


label_title = Label(F_Home, bd=5, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM",
                    fg="red", bg="#212121", font=("akrobat black", 50, "bold", "underline",))
label_title.pack(side=TOP, fill=X)





lblfrm = LabelFrame(F_Home, bd=8, relief=RIDGE, padx=10, fg="white", bg="Black", font=(
    "akrobat black", 16, "bold", "underline",), text="Welcome")
lblfrm.place(x=110, y=15, width=1680, height=920)

Label(lblfrm, bg="Black", fg="white", text="A project by Niranjan S, Hari Prasad, Yasus & Ammu Krishna (2022-23 batch)",
    font=("D3 Euronism Bold", 20,), justify=CENTER, cursor="xterm").place(x=65, y=820)


def login():
    pass



button_Display = Button(F_Home, text="DISPLAY DETAILS", font=("D3 Euronism Bold", 18), command=login, height=3,
                            width=13, bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Display.place(x=580, y=300, width=340, height=203)

button_Add_member = Button(F_Home, text="ADD NEW MEMBER", font=("D3 Euronism Bold", 18), command=login, height=3,
                            width=13, bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Add_member.place(x=1000, y=300, width=340, height=203)

button_Delete_member = Button(F_Home, text="DELETE A MEMBER", command=login, font=("D3 Euronism Bold", 18), height=3, width=13,
                    bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Delete_member.place(x=580, y=600, width=340, height=203)

button_Exit = Button(F_Home, text="Exit", command=login, font=("D3 Euronism Bold", 18), height=3, width=13,
                    bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Exit.place(x=1000, y=600, width=340, height=203)


'''
