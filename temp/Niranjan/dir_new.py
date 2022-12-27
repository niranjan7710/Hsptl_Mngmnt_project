from tkinter import *
from tkinter import messagebox
import mysql.connector


# =================================================================Tkinter Window=====================================================================
root = Tk()
root.state('zoomed')
root.title("Hospital Management System")
root.geometry("1920x1080")
# ===================================================================================================================================================


def swap(frame):
    frame.tkraise()


# ======================================================================PATIENT DETAILS-Delete=========================================================================================


F_pd_del = Frame(root, bd=8, background="#212121", relief=RIDGE)
F_pd_del.place(x=0, y=90, width=1920, height=970)


label_title = Label(root, bd=5, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM",
                    fg="red", bg="#212121", font=("akrobat black", 50, "bold", "underline",))
label_title.pack(side=TOP, fill=X)

label_title_1 = Label(F_pd_del, bd=5, relief=RIDGE, text="Administration - Delete",
                    fg="red", bg="#212121", font=("akrobat black", 30, "bold", ))
label_title_1.pack(side=TOP, fill=X)


lblfrm = LabelFrame(F_pd_del, bd=8, relief=RIDGE, padx=10, fg="white", bg="Black", font=(
    "akrobat black", 16, "bold", "underline",), text="Administration - Delete")
lblfrm.place(x=160, y=95, width=1600, height=820)  

Label(lblfrm, bg="Black", fg="white", text="A project by Niranjan S, Hari Prasad, Yasus & Ammu Krishna (2022-23 batch)",
      font=("cascadia code", 20,), justify=CENTER, cursor="xterm").place(x=65, y=820)


def login():
    pass


button_Display = Button(lblfrm, text="Delete  Doctor", font=("cascadia code", 18), command=login, height=3,
                        width=13, bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Display.place(x=380, y=150, width=340, height=203)

button_Add_member = Button(lblfrm, text="Delete  Nurse", font=("cascadia code", 18), command=login, height=3,
                           width=13, bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Add_member.place(x=800, y=150, width=340, height=203)

button_Delete_member = Button(lblfrm, text="Delete Other Wokers", command=login, font=("cascadia code", 18), height=3, width=13,
                              bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Delete_member.place(x=380, y=450, width=340, height=203)

button_Exit = Button(lblfrm, text="Go Back", command=lambda: swap(F_adm), font=("cascadia code", 18), height=3, width=13,
                     bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Exit.place(x=800, y=450, width=340, height=203)


# ======================================================================PATIENT DETAILS-Delete ENDS=========================================================================================



# ======================================================================PATIENT DETAILS-Add=========================================================================================
'''
F_pd_add = Frame(root, bd=8, background="#212121", relief=RIDGE)
F_pd_add.place(x=0, y=0, width=1920, height=1080)


label_title = Label(F_pd_add, bd=5, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM",
                    fg="red", bg="#212121", font=("akrobat black", 50, "bold", "underline",))
label_title.pack(side=TOP, fill=X)

label_title_1 = Label(F_pd_add, bd=5, relief=RIDGE, text="Add New - ADMINISTRATION",
                    fg="red", bg="#212121", font=("akrobat black", 30, "bold", ))
label_title_1.pack(side=TOP, fill=X)


lblfrm = LabelFrame(F_pd_add, bd=8, relief=RIDGE, padx=10, fg="white", bg="Black", font=(
    "akrobat black", 16, "bold", "underline",), text="Add New - Administration")
lblfrm.place(x=160, y=195, width=1600, height=820)  

Label(lblfrm, bg="Black", fg="white", text="A project by Niranjan S, Hari Prasad, Yasus & Ammu Krishna (2022-23 batch)",
      font=("cascadia code", 20,), justify=CENTER, cursor="xterm").place(x=65, y=820)


def login():
    pass


button_add = Button(lblfrm, text="Add New Patient", font=("cascadia code", 18), command=login, height=3,
                        width=13, bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_add.place(x=380, y=150, width=340, height=203)

button_Exit = Button(lblfrm, text="Go Back", command=lambda: swap(F_pdetails), font=("cascadia code", 18), height=3, width=13,
                     bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Exit.place(x=380, y=550, width=340, height=203)

'''

# ======================================================================PATIENT DETAILS-Add ENDS=========================================================================================





# ======================================================================PATIENT DETAILS-DISPLAY=========================================================================================

F_pd_dis = Frame(root, bd=8, background="#212121", relief=RIDGE)
F_pd_dis.place(x=0, y=0, width=1920, height=1080)


label_title = Label(F_pd_dis, bd=5, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM",
                    fg="red", bg="#212121", font=("akrobat black", 50, "bold", "underline",))
label_title.pack(side=TOP, fill=X)

label_title_1 = Label(F_pd_dis, bd=5, relief=RIDGE, text="ADMINISTRATION",
                    fg="red", bg="#212121", font=("akrobat black", 30, "bold", ))
label_title_1.pack(side=TOP, fill=X)


lblfrm = LabelFrame(F_pd_dis, bd=8, relief=RIDGE, padx=10, fg="white", bg="Black", font=(
    "akrobat black", 16, "bold", "underline",), text="DISPLAY PATIENT DETAILS")
lblfrm.place(x=400, y=225, width=1180, height=620) 

Label(lblfrm, bg="Black", fg="white", text="A project by Niranjan S, Hari Prasad, Yasus & Ammu Krishna (2022-23 batch)",
      font=("cascadia code", 20,), justify=CENTER, cursor="xterm").place(x=65, y=820)


def login():
    pass


button_Display_all = Button(lblfrm, text="DISPLAY ALL PATEINTS", font=("cascadia code", 18), command=lambda: swap(F_pd_dis), height=3,
                               width=13, bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Display_all.place(x=250, y=150, width=280, height=103)

button_Display_pid = Button(lblfrm, text="DISPLAY BY PATIENT ID", font=("cascadia code", 18), command=lambda: swap(F_pd_add), height=3,
                               width=13, bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Display_pid.place(x=630, y=150, width=280, height=103)
login
button_Display_sex = Button(lblfrm, text="DISPLAY BY SEX", command=login, font=("cascadia code", 18), height=3, width=13,
                     bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Display_sex.place(x=250, y=350, width=280, height=103)


button_Display_age = Button(lblfrm, text="DISPLAY BY AGE", font=("cascadia code", 18), height=3, width=13,command= login,
                     bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Display_age.place(x=630, y=350, width=280, height=103)


button_exit = Button(lblfrm, text="Go Back", font=("cascadia code", 18), height=3, width=13,command=lambda: swap(F_pdetails),
                     bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_exit.place(x=430, y=450, width=280, height=103)

'''

button_Display_all = Button(lblfrm, text="Display All", font=("cascadia code", 18), command=login, height=3,
                        width=13, bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Display_all.place(x=380, y=150, width=340, height=203)

button_Display_pid = Button(lblfrm, text="Display by patient id", font=("cascadia code", 18), command=login, height=3,
                           width=13, bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Display_pid.place(x=800, y=150, width=340, height=203)

button_Display_sex = Button(lblfrm, text="Display by sex", command=login, font=("cascadia code", 18), height=3, width=13,
                              bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Display_sex.place(x=380, y=450, width=340, height=203)

button_Display_age = Button(lblfrm, text="Display by age", command=login, font=("cascadia code", 18), height=3, width=13,
                              bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Display_age.place(x=800, y=450, width=340, height=203)


button_Exit = Button(lblfrm, text="Go Back", command=lambda: swap(F_pdetails), font=("cascadia code", 18), height=3, width=13,
                     bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Exit.place(x=380, y=550, width=340, height=203)

'''
# ======================================================================PATIENT DETAILS-display ENDS=========================================================================================





# ================================================================PATIENT DETAILS===================================================================================

F_pdetails = Frame(root, bd=8, background="#212121", relief=RIDGE)
F_pdetails.place(x=0, y=0, width=1920, height=1080)


label_title = Label(F_pdetails, bd=5, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM",
                    fg="red", bg="#212121", font=("akrobat black", 50, "bold", "underline",))
label_title.pack(side=TOP, fill=X)

label_title_1 = Label(F_pdetails, bd=5, relief=RIDGE, text="PATIENT DETAILS",
                    fg="red", bg="#212121", font=("akrobat black", 30, "bold", ))
label_title_1.pack(side=TOP, fill=X)


lblfrm = LabelFrame(F_pdetails, bd=8, relief=RIDGE, padx=10, fg="white", bg="Black", font=(
    "akrobat black", 16, "bold", "underline",), text="Welcome")
lblfrm.place(x=400, y=225, width=1180, height=620) 

#l = Label(lblfrm, bg="Black", fg="white", text="PATIENT DETAILS", justify=CENTER, cursor="xterm").place(x=5, y=820)


Label(F_pdetails, bg="Black", fg="white", text="A project by Niranjan S, Hari Prasad, Yasus & Ammu Krishna (2022-23 batch)",
      font=("cascadia code", 20,), justify=CENTER, cursor="xterm").place(x=200,y=1000)




button_Display = Button(lblfrm, text="DISPLAY DETAILS", font=("cascadia code", 18), command=lambda: swap(F_pd_dis), height=3,
                               width=13, bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Display.place(x=250, y=150, width=280, height=103)

button_Add_member = Button(lblfrm, text="ADD NEW PATIENT", font=("cascadia code", 18), command=lambda: swap(F_pd_add), height=3,
                               width=13, bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Add_member.place(x=630, y=150, width=280, height=103)

button_Discharge = Button(lblfrm, text="DISCHARGE", command=login, font=("cascadia code", 18), height=3, width=13,
                     bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Discharge.place(x=250, y=350, width=280, height=103)

button_Exit = Button(lblfrm, text="Go Back", font=("cascadia code", 18), height=3, width=13,command=lambda: swap(F_Home),
                     bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Exit.place(x=630, y=350, width=280, height=103)


# ================================================================PATIENT DETAILS PAGE ENDS===================================================================================















# ======================================================================ADMINISTRATION-Delete=========================================================================================

F_adm_del = Frame(root, bd=8, background="#212121", relief=RIDGE)
F_adm_del.place(x=0, y=90, width=1920, height=970)


label_title = Label(root, bd=5, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM",
                    fg="red", bg="#212121", font=("akrobat black", 50, "bold", "underline",))
label_title.pack(side=TOP, fill=X)

label_title_1 = Label(F_adm_del, bd=5, relief=RIDGE, text="Administration - Delete",
                    fg="red", bg="#212121", font=("akrobat black", 30, "bold", ))
label_title_1.pack(side=TOP, fill=X)


lblfrm = LabelFrame(F_adm_del, bd=8, relief=RIDGE, padx=10, fg="white", bg="Black", font=(
    "akrobat black", 16, "bold", "underline",), text="Administration - Delete")
lblfrm.place(x=160, y=95, width=1600, height=820)  

Label(lblfrm, bg="Black", fg="white", text="A project by Niranjan S, Hari Prasad, Yasus & Ammu Krishna (2022-23 batch)",
      font=("cascadia code", 20,), justify=CENTER, cursor="xterm").place(x=65, y=820)


def login():
    pass


button_Display = Button(lblfrm, text="Delete  Doctor", font=("cascadia code", 18), command=login, height=3,
                        width=13, bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Display.place(x=380, y=150, width=340, height=203)

button_Add_member = Button(lblfrm, text="Delete  Nurse", font=("cascadia code", 18), command=login, height=3,
                           width=13, bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Add_member.place(x=800, y=150, width=340, height=203)

button_Delete_member = Button(lblfrm, text="Delete Other Wokers", command=login, font=("cascadia code", 18), height=3, width=13,
                              bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Delete_member.place(x=380, y=450, width=340, height=203)

button_Exit = Button(lblfrm, text="Go Back", command=lambda: swap(F_adm), font=("cascadia code", 18), height=3, width=13,
                     bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Exit.place(x=800, y=450, width=340, height=203)


# ======================================================================ADMINISTRATION-Delete ENDS=========================================================================================



# ======================================================================ADMINISTRATION-Add=========================================================================================

F_adm_add = Frame(root, bd=8, background="#212121", relief=RIDGE)
F_adm_add.place(x=0, y=90, width=1920, height=970)


label_title = Label(root, bd=5, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM",
                    fg="red", bg="#212121", font=("akrobat black", 50, "bold", "underline",))
label_title.pack(side=TOP, fill=X)

label_title_1 = Label(F_adm_add, bd=5, relief=RIDGE, text="Add New - ADMINISTRATION",
                    fg="red", bg="#212121", font=("akrobat black", 30, "bold", ))
label_title_1.pack(side=TOP, fill=X)


lblfrm = LabelFrame(F_adm_add, bd=8, relief=RIDGE, padx=10, fg="white", bg="Black", font=(
    "akrobat black", 16, "bold", "underline",), text="Add New - Administration")
lblfrm.place(x=160, y=95, width=1600, height=820)  

Label(lblfrm, bg="Black", fg="white", text="A project by Niranjan S, Hari Prasad, Yasus & Ammu Krishna (2022-23 batch)",
      font=("cascadia code", 20,), justify=CENTER, cursor="xterm").place(x=65, y=820)


def login():
    pass


button_Display = Button(lblfrm, text="Add New Doctor", font=("cascadia code", 18), command=login, height=3,
                        width=13, bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Display.place(x=380, y=150, width=340, height=203)

button_Add_member = Button(lblfrm, text="Add New Doctor", font=("cascadia code", 18), command=login, height=3,
                           width=13, bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Add_member.place(x=800, y=150, width=340, height=203)

button_Delete_member = Button(lblfrm, text="Add Other Wokers", command=login, font=("cascadia code", 18), height=3, width=13,
                              bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Delete_member.place(x=380, y=450, width=340, height=203)

button_Exit = Button(lblfrm, text="Go Back", command=lambda: swap(F_adm), font=("cascadia code", 18), height=3, width=13,
                     bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Exit.place(x=800, y=450, width=340, height=203)


# ======================================================================ADMINISTRATION-Add ENDS=========================================================================================





# ======================================================================ADMINISTRATION-DISPLAY=========================================================================================

F_adm_dis = Frame(root, bd=8, background="#212121", relief=RIDGE)
F_adm_dis.place(x=0, y=90, width=1920, height=970)


label_title = Label(root, bd=5, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM",
                    fg="red", bg="#212121", font=("akrobat black", 50, "bold", "underline",))
label_title.pack(side=TOP, fill=X)

label_title_1 = Label(F_adm_dis, bd=5, relief=RIDGE, text="ADMINISTRATION",
                    fg="red", bg="#212121", font=("akrobat black", 30, "bold", ))
label_title_1.pack(side=TOP, fill=X)


lblfrm = LabelFrame(F_adm_dis, bd=8, relief=RIDGE, padx=10, fg="white", bg="Black", font=(
    "akrobat black", 16, "bold", "underline",), text="Administration")
lblfrm.place(x=160, y=95, width=1600, height=820)  

Label(lblfrm, bg="Black", fg="white", text="A project by Niranjan S, Hari Prasad, Yasus & Ammu Krishna (2022-23 batch)",
      font=("cascadia code", 20,), justify=CENTER, cursor="xterm").place(x=65, y=820)


def login():
    pass


button_Display = Button(lblfrm, text="Display Doctor Details", font=("cascadia code", 18), command=login, height=3,
                        width=13, bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Display.place(x=380, y=150, width=340, height=203)

button_Add_member = Button(lblfrm, text="Display Doctor Details", font=("cascadia code", 18), command=login, height=3,
                           width=13, bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Add_member.place(x=800, y=150, width=340, height=203)

button_Delete_member = Button(lblfrm, text="Other Wokers", command=login, font=("cascadia code", 18), height=3, width=13,
                              bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Delete_member.place(x=380, y=450, width=340, height=203)

button_Exit = Button(lblfrm, text="Go Back", command=lambda: swap(F_adm), font=("cascadia code", 18), height=3, width=13,
                     bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Exit.place(x=800, y=450, width=340, height=203)


# ======================================================================ADMINISTRATION-display ENDS=========================================================================================






# ======================================================================ADMINISTRATION=========================================================================================

F_adm = Frame(root, bd=8, background="#212121", relief=RIDGE)
F_adm.place(x=0, y=0, width=1920, height=1080)


label_title = Label(F_adm, bd=5, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM",
                    fg="red", bg="#212121", font=("akrobat black", 50, "bold", "underline",))
label_title.pack(side=TOP, fill=X)

label_title_1 = Label(F_adm, bd=5, relief=RIDGE, text="ADMINISTRATION",
                    fg="red", bg="#212121", font=("akrobat black", 30, "bold", ))
label_title_1.pack(side=TOP, fill=X)


lblfrm = LabelFrame(F_adm, bd=8, relief=RIDGE, padx=10, fg="white", bg="Black", font=(
    "akrobat black", 16, "bold", "underline",), text="Administration")
lblfrm.place(x=400, y=225, width=1180, height=620)   

Label(F_adm, bg="Black", fg="white", text="A project by Niranjan S, Hari Prasad, Yasus & Ammu Krishna (2022-23 batch)",
      font=("cascadia code", 20,), justify=CENTER, cursor="xterm").place(x=200,y=1000)


def login():
    pass


button_Display = Button(lblfrm, text="DISPLAY DETAILS", font=("cascadia code", 16), command=lambda: swap(F_adm_dis), height=3,
                        width=13, bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Display.place(x=250, y=150, width=280, height=103)

button_Add_member = Button(lblfrm, text="ADD NEW MEMBER", font=("cascadia code", 16), command=lambda: swap(F_adm_add), height=3,
                           width=13, bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Add_member.place(x=630, y=150, width=280, height=103)

button_Delete_member = Button(lblfrm, text="DELETE A MEMBER", command=lambda: swap(F_adm_del), font=("cascadia code", 16), height=3, width=13,
                              bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Delete_member.place(x=250, y=350, width=280, height=103)

button_Exit = Button(lblfrm, text="Go Back", command=lambda: swap(F_Home), font=("cascadia code", 16), height=3, width=13,
                     bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Exit.place(x=630, y=350, width=280, height=103)


# ======================================================================ADMINISTRATION ENDS=========================================================================================








# ================================================================HOME PAGE===================================================================================

F_Home = Frame(root, bd=8, background="#212121", relief=RIDGE)
F_Home.place(x=0, y=0, width=1920, height=1080)


label_title = Label(F_Home, bd=5, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM",
                    fg="red", bg="#212121", font=("akrobat black", 50, "bold", "underline",))
label_title.pack(side=TOP, fill=X)

label_title_1 = Label(F_Home, bd=5, relief=RIDGE, text="HOME PAGE",
                    fg="red", bg="#212121", font=("akrobat black", 30, "bold", ))
label_title_1.pack(side=TOP, fill=X)


lblfrm = LabelFrame(F_Home, bd=8, relief=RIDGE, padx=10, fg="white", bg="Black", font=(
    "akrobat black", 16, "bold", "underline",), text="Welcome")
lblfrm.place(x=400, y=225, width=1180, height=620)

Label(F_Home, bg="Black", fg="white", text="A project by Niranjan S, Hari Prasad, Yasus & Ammu Krishna (2022-23 batch)",
      font=("cascadia code", 20,), justify=CENTER, cursor="xterm").place(x=200,y=1000)


def close_tkinter():
    root.destroy()


button_Administration = Button(lblfrm, text="Administration", command=lambda: swap(F_adm), font=("cascadia code", 19), height=3,
                               width=13, bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Administration.place(x=400, y=150, width=390, height=53)

button_PatientDetails = Button(lblfrm, text="Patient Details",command=lambda: swap(F_pdetails), font=("cascadia code", 19),  height=3,
                               width=13, bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_PatientDetails.place(x=400, y=250, width=390, height=53)

button_Exit = Button(lblfrm, text="Exit",  font=("cascadia code", 19), height=3, width=13,command=lambda: close_tkinter(),
                     bd=7, bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_Exit.place(x=400, y=350, width=390, height=53)

# ======================================================================HOME PAGE ENDS=========================================================================================


# ================================================================LOGIN PAGE=========================================================================


F_login = Frame(root, bd=8, background="#212121", relief=RIDGE)
F_login.place(x=0, y=0, width=1920, height=1080)


label_title = Label(F_login, bd=5, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM",
                    fg="red", bg="#212121", font=("akrobat black", 50, "bold", "underline",))
label_title.pack(side=TOP, fill=X)

label_title_1 = Label(F_login, bd=5, relief=RIDGE, text="LOGIN",
                    fg="red", bg="#212121", font=("akrobat black", 30, "bold", ))
label_title_1.pack(side=TOP, fill=X)


global entry1
global entry2


lblfrm = LabelFrame(F_login, bd=8, relief=RIDGE, padx=10, fg="white", bg="#2b2d42", font=(
    "akrobat black", 16, "bold", "underline",), text="Login to your mysql Database")
lblfrm.place(x=400, y=225, width=1180, height=620)

Label(lblfrm, bg="#2b2d42", fg="white", text="USERNAME", font=(
    "akrobat ", 20, "bold",), justify=RIGHT, cursor="xterm").place(x=320, y=180)
entry1 = Entry(lblfrm, font=("cascadia code mono", 16, "bold"),
               bg="#2b2d42", fg="white", bd=5, justify='center')
entry1.insert(0, "root")
entry1.place(x=550, y=180, width=290, height=33)

Label(lblfrm, bg="#2b2d42", fg="white", text="PASSWORD", font=(
    "akrobat ", 20, "bold",), justify=RIGHT, cursor="xterm").place(x=320, y=280)
entry2 = Entry(lblfrm, font=("cascadia code mono", 16, "bold"),
               bg="#2b2d42", fg="white", bd=5, justify='center', show="*")
entry2.place(x=550, y=280, width=290, height=33)


def login():
    user = entry1.get()
    passw = entry2.get()

    swap(F_Home)


#    try:
#        con = mysql.connector.connect(
#            host="localhost",
#           user=user,
#          passwd=passw,
#        )


#        if con.is_connected():
#            messagebox.showinfo("Success", "Welcome to Hospital Management")
#            swap(F_Home)
#    except:
#        messagebox.showinfo("error", "Inavlid Credentials")


Label(F_login, bg="Black", fg="white", text="A project by Niranjan S, Hari Prasad, Yasus & Ammu Krishna (2022-23 batch)",
      font=("cascadia code", 20,), justify=CENTER, cursor="xterm").place(x=200,y=1000)



button_login = Button(lblfrm, text="login", command=lambda: login(), height=3, width=13, bd=7,
                      bg="#2b2d42", fg="white", cursor="hand2", activebackground='#2b2d42', activeforeground="white")
button_login.place(x=500, y=390, width=130, height=53)

# ================================================================LOGIN PAGE ENDS HERE=======================================================================

root.mainloop()
