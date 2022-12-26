from tkinter import *
from tkinter import messagebox
import mysql.connector


root = Tk()
root.state('zoomed')
root.title("Home Screen")
root.geometry("1920x1080+0+0")

label_title = Label(root, bd=5, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM",
                    fg="red", bg="#212121", font=("akrobat black", 50, "bold", "underline",))
label_title.pack(side=TOP, fill=X)

DataFrame = Frame(root, bd=8, background="#212121", relief=RIDGE)
DataFrame.place(x=0, y=90, width=1920, height=970)



lblfrm = LabelFrame(DataFrame, bd=8, relief=RIDGE, padx=10, fg="white", bg="Black", font=(
    "akrobat black", 16, "bold", "underline",), text="Welcome")
lblfrm.place(x=110, y=15, width=1680, height=920)

#l = Label(lblfrm, bg="Black", fg="white", text="PATIENT DETAILS", justify=CENTER, cursor="xterm").place(x=5, y=820)


Label(lblfrm, bg="Black", fg="white", text="A project by Niranjan S, Hari Prasad, Yasus & Ammu Krishna (2022-23 batch)",
      font=("D3 Euronism Bold", 20,), justify=CENTER, cursor="xterm").place(x=65, y=820)


def login():
    pass



button_Display = Button(root, text="DISPLAY DETAILS", font=("D3 Euronism Bold", 18), command=login, height=3,
                               width=13, bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Display.place(x=580, y=300, width=340, height=203)

button_Add_member = Button(root, text="ADD NEW PATIENT", font=("D3 Euronism Bold", 18), command=login, height=3,
                               width=13, bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Add_member.place(x=1000, y=300, width=340, height=203)

button_Discharge = Button(root, text="DISCHARGE", command=login, font=("D3 Euronism Bold", 18), height=3, width=13,
                     bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Discharge.place(x=580, y=600, width=340, height=203)

button_Exit = Button(root, text="Exit", command=login, font=("D3 Euronism Bold", 18), height=3, width=13,
                     bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Exit.place(x=1000, y=600, width=340, height=203)


root.mainloop()
